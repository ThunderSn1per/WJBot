#To do
#Custom match settings - https://media.discordapp.net/attachments/358098420130643969/457675735667310592/unknown.png
#Version 0.9 - 02/08/2018
import discord
from redbot.core import commands
import random
import threading
import time
import asyncio
import json
from datetime import datetime, timedelta
from pprint import pprint

BaseCog = getattr(commands, "Cog", object)

class subr(BaseCog):
	def __init__(self, bot):
		self.bot = bot
		self.rSwitch = 1																		#Toggle Switch to open/close roster - 0/1 = Close/Open
		self.mRoles = ["Roster Manager", "You know who", "WackyBot", "Moderator"]				#Moderator roles
		self.pRoles = ["Stealth", "Pro", "Chicken Dinner", "Prestige", "Elite"]					#Patreon Roles
		self.sRoles = ["Twitch Subscriber"]														#Supporter Roles
		self.channels = ["wacky_roster"]														#Channels
		self.customs = [] 																		#List of players who opt-in
		self.chosen = []																		#List of players who have been picked to prevent duplicates
		self.teams = []
		self.events = ["Event Lobby", "Event Duo", "Event Squad", "Event 5+ Squad"]				#List of event voice chat categories
		self.pwdate = "18:04"																	#String for the last update to the password
		self.passw = ""																			#Password for customs
		self.svr = self.bot.get_guild(355750209730641920)										#Variable for Server ID
		self.wacky = self.svr.get_member(290455355316764682)									#Variable for WackyJacky101's ID
		self.thunder = self.svr.get_member(201303438452064256)									#Variable for ThunderSn1per's ID
		self.wackyclub = self.svr.get_channel(378590577769316352)								#Variable for #the_wacky_club's ID
		self.suppann = self.svr.get_channel(506534514219024384)									#Variable for #supporter_announcements' ID
		self.discordbans = self.svr.get_channel(377116857812910080)								#Unused variable currently
		self.botlog = self.svr.get_channel(370677704174993417)									#Variable for #bot_log's ID
		self.waitr = self.svr.get_channel(406520047134048256)									#Variable for 'Waiting Room for WJ Stream' voice channel
		self.streamr = self.svr.get_channel(373851080011939850)									#Variable for 'WJ Stream' voice channel
		self.rm = self.svr.get_role(421679811577118720)											#Variable for 'Roster Manager' role
		self.bans = []																			#Array for bans
		self.champs = []																		#Array for Champions
		self.path = "/root/.local/share/Red-DiscordBot/cogs/CogManager/cogs/roster/"			#Path for main cog, used to keep all external data links in one folder
		self.discordBans = []
		self.bansLog = []
		self.passmsg = None
		self.blacklist = [168309055578701824]													#Blacklisted IDs of users that will NEVER be picked for customs
		subr.load(self)																			#Run the load() function
	
	async def openRoster(self, ctx, pw):
		#await ctx.send(self.svr) #Do we have the server saved?
		subr.load(self) #Load preferences
		curd = str(datetime.now().strftime("%d:%m")) #Current Date
		if(curd != self.pwdate) and (pw==1): #if it's a new day and pw=1 THEN Set a new password
			#SETTING A NEW PASSWORD#
			self.pwdate = curd #Not a new day anymore
			subr.save(self)
			tempp = str(random.randint(0,1000)) #Random 3 digit number for password
			self.passw = "wj" + tempp.rjust(3,"0") #Concatenate wjxxx
			await self.wacky.send("Password for customs has been set to - %s" % self.passw)
			self.passmsg = await self.suppann.send("The supporter password for customs is **'%s'** - Please remember do **NOT** share this password with anyone and enjoy the customs!" % self.passw)
		self.waitr = self.svr.get_channel(406520047134048256) #Waiting Room ID
		subr.load(self)
		self.rSwitch = 1
		#Customs Roster Channel Permissions
		for a in self.svr.roles:
			if (str(a) in self.sRoles) or (str(a) in self.pRoles):
				try:
					await ctx.channel.set_permissions(a, send_messages = True, read_messages = True)
				except:
					None
		#Event Category Permissions
		for x in self.svr.channels:
			if str(x) in self.events:
				await x.set_permissions(self.svr.default_role, read_messages = True)
		#Waiting Room Permissions
		await self.svr.get_channel(406520047134048256).set_permissions(self.svr.default_role, read_messages = True, connect = False)
	
	async def closeRoster(self, msg: discord.Message):
		self.rSwitch = 0														#Turns the Roster off
		self.bloc = 0															#Allows the @here message upon opening
		for a in self.svr.roles:												#----- Denies users read/send messages permissions
			if (str(a) in self.sRoles) or (str(a) in self.pRoles):				#---/
				await msg.channel.set_permissions(a, send_messages = False, read_messages = True)
	
	async def banCheck(self, passive=0):
		if str(datetime.now().strftime("%H")) == "00":
			curdate = str(datetime.now().strftime("%d-%m-%Y"))
			count = -1
			for m in self.bans:
				count += 1
				if m[2] == curdate:
					role = discord.utils.get(self.svr.roles, id=475261440953942029)
					tu = self.svr.get_member(int(m[0]))
					await tu.remove_roles(role)
					try: await tu.send("You are no longer timed out, please adhere to the rules in future")
					except: None
					pprint(self.bansLog)
					self.bansLog.append(m[0])
					pprint(self.bansLog)
					del self.bans[count]
					subr.save(self)
			await asyncio.sleep(3600)
			subr.banCheck(self, 0)
		else:
			await asyncio.sleep(3600)
			subr.banCheck(self, 0)
	
	def save(self):
		with open(self.path + "roster.json", 'w') as outfile:
			json.dump(self.customs, outfile)
		with open(self.path + "chosen.json", 'w') as outfile:
			json.dump(self.chosen, outfile)
		dict = {"pwdate" : self.pwdate, "champs" : self.champs}
		with open(self.path + "misc.json", 'w') as outfile:
			json.dump(dict, outfile)
		with open(self.path + "dBans.json", 'w') as outfile:
			json.dump(self.discordBans, outfile)
		with open(self.path + "fBans.json", 'w') as outfile:
			json.dump(self.faceitBans, outfile)
		with open(self.path + "bansLog.json", 'w') as outfile:
			json.dump(self.bansLog, outfile)
		with open(self.path + "bans.json", 'w') as outfile:
			json.dump(self.bans, outfile)
		with open(self.path + "teams.json", "w") as outfile:
			json.dump(self.teams, outfile)
			
	def load(self):
		self.customs = json.load(open(self.path + "roster.json"))
		self.chosen = json.load(open(self.path + "chosen.json"))
		dict = json.load(open(self.path + "misc.json"))
		self.bans = json.load(open(self.path + "bans.json"))
		self.discordBans = json.load(open(self.path + "dBans.json"))
		self.faceitBans = json.load(open(self.path + "fBans.json"))
		self.bansLog = json.load(open(self.path + "bansLog.json"))
		self.teams = json.load(open(self.path + "teams.json"))
		
		if(self.pwdate=="18:04"):
			subr.banCheck(self, passive=0)
		
		self.pwdate = dict["pwdate"]
		self.champs = dict["champs"]
	
	def roleCheck(self, user):
		uRoles = []
		for u in user.roles:
			uRoles.append(str(u))
		return (set(uRoles).intersection(self.mRoles))
	
	def channelTest(self, ctx):
		if(ctx.message.guild is None):
			return 0
		else:
			return 1
	
	def checkBlacklist(self, ctx):
		uid = ctx.author.id
		return (uid in self.blacklist)
	
	def teamCheck(self, id):
		for sl in self.teams:
			if id in sl:
				return (self.teams.index(sl))
		return "clear"
		
	def clearEmptyTeams(self):
		for p in self.customs:							#
			if(isinstance(p, list)):					#
				for q in self.chosen:					#Remove players who have already played
					if q in p:							#
						p.remove(q)		#
			else:
				if p in self.chosen:
					self.customs.remove(p)
					
		for a in self.customs:							#
			if isinstance(a, list):						#Clears empty teams
				if(len(a) == 1 and a[0][:2] == "wj"):	#
					self.customs.remove(a)				#
		subr.save(self)									#Save after clearing empty teams
		
	
	async def on_message(self, message):
		if(message.guild is None and message.author.id != 424179093094006785):
			await message.channel.send("DMs are not allowed")
		else:
			if(str(message.channel) == "wacky_roster") and (self.rSwitch == 1):
				if(subr.roleCheck(self, message.author)):
					return
				if(message.author.id == 424179093094006785):
					return
				else:
					if(message.content == "!addme"):
						return
					else:
						await message.delete()
						
			if(str(message.channel.name) == "access"):
				if(message.content == "!acceptrules"):
					return
				else:
					await message.delete()
					
			if(str(message.channel.name) == "general_chat"):
				if "http" in message.content or "www" in message.content:
					if(subr.roleCheck(self, message.author)):
						return
					else:
						message.delete()
						m = await message.channel.send(message.author.mention + " please read the #rules. No links allowed in #general_chat. Thank you!")
						await asyncio.sleep(5)
						await m.delete()
	
	async def on_member_join(self, member):																				#Server will still need a landing-page. Some users may have disabled receiving private messages from server users which cancels this
		try:
			await member.send("**Welcome to the WackyJacky101 community!**\n\n\
If you are looking for the **supporter password** for custom games, please read this important information:\n\
1. Link Discord to your Twitch/Patreon accounts (if you haven't done it yet) under Settings -> Connections.\n\
2. Wait for up to an hour for the automatic sync to get your Twitch subscriber role\n\
3. After you have your role, you will find the password pinned in #the_wacky_club (how to see pinned messages: <https://tinyurl.com/yd662tfg>) \n\n\
If you weren't in need of this information we apologize for the ping - thank you for joining us! :heart: \n\n\
Best regards from WackyJacky101 and the moderator team\n\n\
PS. You will not be able to chat for the first 10 minutes. While you wait, please familiarize yourself with the **#rules**. Thanks!")
		except:
			return
	
	@commands.command(pass_context=True)
	async def acceptrules(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if(str(ctx.channel.name)=="access"):
				await ctx.message.delete()
				r = self.svr.get_role(501014583511613460)
				await ctx.author.add_roles(r)
	
	@commands.command(pass_context=True, no_pm=True)
	async def addme(self, ctx):
		###### START OF CHECKS ######
		if(subr.checkBlacklist(self, ctx) == 1):
			try:
				await ctx.author.send("You have been blacklisted and cannot join Wacky's roster. If you don't know why, please PM a moderator on Discord.")
			except:
				None
			return
		if(subr.teamCheck(self, ctx.author.id) == "clear"):
			None
		else:
			tm = await ctx.send(ctx.author.mention + " you are already part of a team please leave the team (!removeme) to join solo")
			await asyncio.sleep(3)
			await tm.delete()
		###### END OF CHECKS ######
		if(subr.channelTest(self, ctx) == 1):
			if(str(ctx.message.channel.name) in self.channels) == 0:
				return
			await ctx.message.delete()
			user = ctx.author
			
			if(ctx.author.id == 290455355316764682):
				await ctx.send("@here " + ctx.author.mention + " has just attempted to add himself to the Roster. Wacky wants to play himself? :sma:")
				return
			
			if user.id in self.customs:												#Check user is already opted in
				try:
					await ctx.author.send("You're already added to the Roster")				#Reply that user is already opted in
				except:
					await ctx.send(user.mention + " - You're already added to the Roster, cannot DM this user.")
			elif user.id in self.chosen:
				try:
					await ctx.author.send("You have already been picked and cannot play again")
				except:
					await ctx.send(user.mention + " - You have already been picked. Cannot DM this user.")
			elif self.rSwitch == 1:																#Otherwise, make sure Roster is on
				self.customs.append(user.id)												#Add user to list
				subr.save(self)
				await ctx.send(user.mention + " added to the Roster!")							#Message chat to say user is added
			else:
				try:
					await ctx.author.send("Roster is closed")									#Otherwise, Roster is closed
				except:
					await ctx.send(user.mention + " - Roster is closed, cannot DM this user.")
	
	@commands.command(pass_context=True)
	async def teamCreate(self, ctx):
		await ctx.message.delete()
		###### START OF CHECKS ######
		if(subr.checkBlacklist(self, ctx) == 1):
			try:
				await ctx.author.send("You have been blacklisted and cannot join Wacky's roster. If you don't know why, please PM a moderator on Discord.")
			except:
				None
			return
		if ctx.author.id in self.customs:
			tm = await ctx.send(ctx.author.mention + " you are on the Roster as a solo player, please remove yourself (!removeme) first.")
			await asyncio.sleep(3)
			await tm.delete()
			return
		if ctx.author.id in self.chosen:
			tm = await ctx.send(ctx.author.mention + " you have already been picked to play on Wacky's team once. You cannot do so again today.")
			await asyncio.sleep(3)
			await tm.delete()
			return
		###### END OF CHECKS ######
		
		tc = subr.teamCheck(self, ctx.author.id)
		if(subr.channelTest(self, ctx) == 1):
			#Check if user is in team already
			if(tc == "clear"):								#User is not on a team
				while True:										#┌--- Checks team ID is doesn't exist and regenerates if it does
					tempp = str(random.randint(0,1000)) 		#|	#Random 3 digit number for password
					team = "wj" + tempp.rjust(3,"0") 			#|	#Concatenate wjxxx
					if(subr.teamCheck(self, team) == "clear"):	#|
						break									#|
				
				newTeam = [team, ctx.author.id]				#Creates a new list with the assigned team name in index 0 and the "leader" in index 1
				self.teams.append(newTeam)					#Adds the list to self.teams
				self.customs.append(team)
				await ctx.send(ctx.author.mention + " added to the Roster")
				subr.save(self)
				try:										#Try to DM user with info
					await ctx.author.send("You've created a team on the Roster, your team is " + team + ". Let your team mates know to join using this team name!")
				except:										#Temp, auto-delete message that tells user to allow DMs
					tm = await ctx.send(ctx.author.mention + " - You have created a team, but are not set to receive DMs from users of this Discord. Please fix this and rerun the command to receive your team name")
					await asyncio.sleep(10)
					await tm.delete()
			else:
				try:										#Try to DM user with info
					await ctx.author.send("You're already on a team, your team is " + self.teams[tc][0] + ". Let your team mates know to join using this team name!")
				except:										#Temp, auto-delete message that tells user to allow DMs
					tm = await ctx.send(ctx.author.mention + " - You have created a team, but are not set to receive DMs from users of this Discord. Please fix this and rerun the command to receive your team name")
					await asyncio.sleep(10)
					await tm.delete()
					
	@commands.command(pass_context=True)
	async def teamJoin(self, ctx, tj=""):
		await ctx.message.delete()
		###### START OF CHECKS ######
		if(subr.checkBlacklist(self, ctx) == 1):
			try:
				await ctx.author.send("You have been blacklisted and cannot join Wacky's roster. If you don't know why, please PM a moderator on Discord.")
			except:
				None
			return
		if ctx.author.id in self.customs:
			tm = await ctx.send(ctx.author.mention + " you are on the Roster as a solo player, please remove yourself (!removeme) first.")
			await asyncio.sleep(3)
			await tm.delete()
			return
		if ctx.author.id in self.chosen:
			tm = await ctx.send(ctx.author.mention + " you have already been picked to play on Wacky's team once. You cannot do so again today.")
			await asyncio.sleep(3)
			await tm.delete()
			return
		###### END OF CHECKS ######
		
		if(tj==""): return
		tc = subr.teamCheck(self, ctx.author.id)
		if(subr.channelTest(self, ctx) == 1):
			if(tc == "clear"):									#User is not on a team
				tji = subr.teamCheck(self, tj)					#Find and store index of team to join
				if(tji == "clear"): return
				team = self.teams[tji][0]
				if(len(self.teams[tji])>3):																		#Checks if team is full
					tm = await ctx.send(ctx.author.mention + " cannot join this team as it is already full")	#Mentions user telling them team is full
					await asyncio.sleep(5)																		#\
					tm.delete()																					#Deletes previous message
					return																						#Ends running of command
				#If team is not full
				self.teams[tji].append(ctx.author.id)			#Adds user to team
				await ctx.send(ctx.author.mention + " added to the Roster")
				subr.save(self)
				try:
					await ctx.author.send("You have joined team - " + team + "!")			#Attempt DM
				except:
					tm = await ctx.send(ctx.author.mention + " you have joined a team!")	#Mention in channel and elete message after 3 seconds
					await asyncio.sleep(3)													#
					tm.delete()																#
			else:											#User is already on a team
				try:
					await ctx.author.send("You are already on a team, please type !teamLeave if you want to leave the team")			#Attempt DM
				except:
					tm = await ctx.send(ctx.author.mention + " is already on a team, please type !teamLeave if you want to leave the team")	#Mention in channel and elete message after 3 seconds
					await asyncio.sleep(3)																									#
					tm.delete()																												#
	
	@commands.command(pass_context=True)
	async def removeme(self, ctx):																#Command to remove yourself from the roster
		if(subr.channelTest(self, ctx) == 1):
			await ctx.message.delete()
			a = ctx.author
			tc = subr.teamCheck(self, ctx.author.id)
			if a.id in self.chosen:
				try:
					await ctx.author.send("You have already been picked, you can't be be picked again.")
				except:
					None
				return
			elif(a.id in self.customs):
				self.customs.remove(a.id)
				#self.chosen.append(str(a.id)) #-Blocks re-adding
				subr.save(self)
				def is_mentioned(m):
					return ctx.author in m.mentions
				await ctx.channel.purge(limit=100, check=is_mentioned)
				subr.save(self)
				try:
					await ctx.author.send("You have been removed from the Roster")
				except:
					rt = await ctx.send(user.mention + " - You have been removed from the Roster, cannot DM this user.")
					await asyncio.sleep(3)
					await rt.delete()
			#Check Teams#
			elif(tc != "clear"):
				self.teams[tc].remove(ctx.author.id)
				def is_mentioned(m):
					return ctx.author in m.mentions
				await ctx.channel.purge(limit=100, check=is_mentioned)
				subr.save(self)
				if(len(self.teams[tc])<2):
					self.customs.remove(self.teams[tc][0])
					del self.teams[tc]
				subr.save(self)
				try:
					await ctx.author.send("You have been removed from the Roster")
				except:
					tm = await ctx.send(user.mention + " - You have been removed from the Roster, cannot DM this user.")
					await asyncio.sleep(3)
					await tm.delete()
			else:
				try:
					await ctx.author.send("You are not on the Roster")
				except:
					rt = await ctx.send(ctx.author.mention + " - You are not on the roster, cannot DM this user.")
					await asyncio.sleep(3)
					await rt.delete()
	
	@commands.command(pass_context=True)
	async def unpick(self, ctx, usr: discord.Member):
		if(subr.channelTest(self, ctx) == 1):
			await ctx.message.delete()
			if(subr.roleCheck(self, ctx.author)):
				uid = usr.id
				if uid in self.chosen:
					self.customs.append(uid)
					self.chosen.remove(uid)
					await ctx.send(usr.mention + " is back on the Roster!")
				else:
					await ctx.author.send(usr.mention + " is not on the chosen list and cannot be unpicked")
	
	@commands.command(pass_context=True)
	async def pick(self, ctx, limit=1):
		if(subr.channelTest(self, ctx) == 1):									#Check for DM Channel
			if(subr.roleCheck(self, ctx.author)):								#Check for user rights
				if(len(self.customs) < 1):										#\
					await ctx.send("Roster is empty")							#Checks is Rsoter is empty
					return														#/
					
				if(limit > 3): limit = 3										#Pick no more than 3
				totalPicked = 0													#Variable for total players picked
				rounds = 0														#Limit of iterations before manual intervention
				tm = []															#Array for users that cannot be pinged
				pps = []
				
				while(totalPicked < limit):										#Begin loop until players picked is the same as limit
					subr.clearEmptyTeams(self)								#To-Do = Check for players who have played to remove their ID
					if(len(self.customs) == 0):
						await ctx.send("Roster is empty")
						break
						
					rounds+=1													#Increment rounds
					
					if((limit - totalPicked) == 3):
						await ctx.send("Picking 3 ...")
						solos = [s for s in self.customs if isinstance(s, int)]
						solos = solos + ([s[1] for s in self.customs if(isinstance(s, list) and len(s) == 2)])
						qTeams = []												#Temporary array to hold new teams
						hTeam = []
						for u in self.customs:
							try:
								isTeam = u[0][:2]
							except:
								continue
							if(isTeam == "wj"):
								h = len([x for x in u if isinstance(x, int)])
								if(h == 3):
									qTeams.append(u)
								elif(h == 2):
									#h = len([x for x in hTeam if isinstance(x, int)])
									hTeam = [s for s in u if isinstance(s, int)]
									if(len(solos)>0):
										hTeam.append(solos[0])
									qTeams.append(hTeam)
									hTeam = []
								else:
									continue
						ran = random.randint(0, (len(qTeams)-1))
						pps = qTeams[ran]
					elif((limit - totalPicked) == 2):
						await ctx.send("Picking 2 ...")
						solos = [s for s in self.customs if isinstance(s, int)]
						solos = solos + ([s[1] for s in self.customs if(isinstance(s, list) and len(s) == 2)])
						qTeams = []
						
						for u in self.customs:
							try:
								isTeam = u[0][:2]
							except:
								continue
							h = len([x for x in u if isinstance(x, int)])
							if(h == 2):
								qTeams.append(u)
						temp = None
						if len(solos) % 2 == 1:
							qTeams.append(solos.pop())
						qTeams = qTeams + [solos[i:i+2] for i in range(0, len(solos), 2)]
						ran = random.randint(0, (len(qTeams)-1))
						pps = qTeams[ran]
					elif((limit - totalPicked) == 1):
						await ctx.send("Picking 1 ...")
						solos = [s for s in self.customs if isinstance(s, int)]
						solos = solos + ([s[1] for s in self.customs if(isinstance(s, list) and len(s) == 2)])
						ran = random.randint(0, (len(solos)-1))
						pps = solos[ran]
					
					#Automated Moving#
					await ctx.send(qTeams)
					pickedNames = []
					pickedUsers = []
					tm = []
					if(isinstance(pps, int)):
						pps = [pps]
					
					if(limit==1):
						a = self.svr.get_member(pps)
						pickedNames.append(a.mention)
						pickedUsers.append(pps)
						self.chosen.append(pps)
						subr.save(self)
					else:
						await ctx.send(pps)
						for u in pps:
							try:
								isTeamName = u[:2]
							except:
								isTeamName = None
							if(isTeamName == "wj"):
								continue
							a = self.svr.get_member(u)
							pickedNames.append(a.mention)
							pickedUsers.append(u)
							self.chosen.append(u)
							try:
								await a.send("You have been picked for WackyJacky101's Custom Match Team! Please join the Waiting Room voice chat! <https://discord.gg/aYdYxBn>")							#Attempt to DM the user with a link to quickly join the voice chat channel.
							except:
								tm.append(a.mention) #Add to temp message for mentioning
							
					try:
						await ctx.send(", ".join(pickedNames) + ": Please join the Waiting Room voice chat") #Tag all users in one message
					except:
						try:
							await self.thunder.send(str(pickedNames)) #Send names to Thunder in DM for debugging
						except:
							None
				
					#Can't DM#
					if(len(tm)>0):
						tempmess = await ctx.send(", ".join(tm) + ": Cannot receive DMs from WJBot. Please change these under Server Settings")
						await asyncio.sleep(10)
						await tempmess.delete()
					
					await asyncio.sleep(10)
					for i in self.waitr.members:
						for j in pickedUsers:
							if(i.id == j):
								totalPicked = totalPicked + 1
								await i.edit(voice_channel = self.streamr)
								
					if(rounds==3):
						await ctx.send("Picking Complete. Players missing from current team: " + str(limit-totalPicked))
						break
						
	
	@commands.command(pass_context=True)
	async def npick(self, ctx, limit=1):
		if(subr.channelTest(self, ctx) == 1):									#Check for DM Channel
			if(subr.roleCheck(self, ctx.author)):								#Check for user rights
			
				if(len(self.customs) < 1):										#\
					await ctx.send("Roster is empty")							#Checks if Roster is empty
					return														#/
					
				if(limit > 3): limit = 3										#Pick no more than 3
				totalPicked = 0													#Variable for total players picked
				rounds = 0														#Limit of iterations before manual intervention
				tm = []															#Array for users that cannot be pinged
				
				while(totalPicked < limit):										#Begin loop until players picked is the same as limit
					tagged = 0													#Tracking users that have successfully been picked and awaiting notification
					pickedUsers = []											#Array for picked users
					pickedNames = []											#Array for picked users names
					rounds+=1													#Increment rounds
					
					while(tagged < (limit-totalPicked)):
						if(len(self.customs) == 0):
							await ctx.send("Roster is empty")
							break
						
						ran = random.randint(0, (len(self.customs)-1))
						
						##If a team is picked##
						try:
							isTeam = self.customs[ran][:2]
						except:
							isTeam = None
						if(isTeam == "wj"):
							tp = subr.teamCheck(self, self.customs[ran])		#\
							tp = self.teams[tp][1:]								#Pulls team members into new list
							if(len(tp)>(limit - totalPicked - tagged)):			#Check it won't pick too many players in total
								rounds = rounds + 1								#If so, repick
								continue										#and increment rounds to prevent infinite loop
							
							del self.customs[ran]								#Clear team from customs array, can't be repicked
														
							for u in tp:										#Iterate each player in the team
								try:
									mem = self.svr.get_member(u)				#Store user data
								except:
									await self.thunder.send("Issue with ID: " + u)	#If an issue occurs, ping Thunder with ID
									continue
								
								self.chosen.append(u)							#Add to chosen list, can't readd themselves
								subr.save(self)									#Save data
								
								try:
									pickedUsers.append(u)
									pickedNames.append(mem.mention)
									def is_mentioned(m):										#\
										return mem in m.mentions								# - Removes all mentions in the last 100 messages of the chosen member
									await ctx.channel.purge(limit=100, check=is_mentioned)		#/
								except:
									await self.thunder.send("ID: " + u + " has produced an error")	#DM Thunder if an error occurs with ID or user
									
								try:
									await mem.send("You have been picked for WackyJacky101's Custom Match Team! Please join the Waiting Room voice chat! <https://discord.gg/aYdYxBn>")							#Attempt to DM the user with a link to quickly join the voice chat channel.
								except:
									tm.append(mem.mention) #Add to temp message for mentioning
									
								tagged = tagged + 1			#Increment tagged as player successfully picked
						else:	#SOLOS#
							u = self.customs[ran]
							self.chosen.append(u)
							self.customs.remove(u)
							subr.save(self)
							
							mem = self.svr.get_member(u)
							
							try:
								pickedUsers.append(u)
								pickedNames.append(mem.mention)
								def is_mentioned(m):										#\
									return mem in m.mentions								# - Removes all mentions in the last 100 messages of the chosen member
								await ctx.channel.purge(limit=100, check=is_mentioned)	#/
							except:
								await self.thunder.send("ID: " + u + " has produced an error")	#DM Thunder if an error occurs with ID or user
								
							try:
								await mem.send("You have been picked for WackyJacky101's Custom Match Team! Please join the Waiting Room voice chat! <https://discord.gg/aYdYxBn>")							#Attempt to DM the user with a link to quickly join the voice chat channel.
							except:
								tm.append(mem.mention) 	#Add to temp message for mentioning
								
							tagged = tagged + 1			#Increment tagged as player successfully picked
					
					if(tagged==0):
						if(rounds==3):
							break
					else:
						#Automated Moving
						try:
							await ctx.send(", ".join(pickedNames) + ": Please join the Waiting Room voice chat")	#Tag all users in one message about joining the voice channel
						except:
							try:
								await self.thunder.send(str(pickedNames))		#If above fails, try to send Thunder a list of the names
							except:
								None
						
						#Can't DM#
						if(len(tm)>0):
								tempmess = await ctx.send(", ".join(tm) + ": Cannot receive DMs from WJBot. Please change these under Server Settings")
								await asyncio.sleep(10)
								await tempmess.delete()
								tm = []
						
						await asyncio.sleep(90)
						for i in self.waitr.members:
							for j in pickedUsers:
								if (i.id == j):
									totalPicked = totalPicked + 1
									await i.edit(voice_channel = self.streamr)
									
						if(totalPicked == limit):
							None
						elif(rounds == 3):
							await ctx.send(self.rm.mention + " - Picking Complete - " + str(limit-totalPicked) + " players missing from current team!")
							break
	
	@commands.command(pass_context=True)
	async def xpick(self, ctx, limit=1):
		if(subr.channelTest(self, ctx) == 1):
			if (subr.roleCheck(self, ctx.author)):
				if(limit > 3): limit = 3
				pickedUsers = []
				totalPicked = 0
				rounds = 0
				if(len(self.customs)>0):
					while(totalPicked < limit):
						tagged = 0
						pickedUsers = []
						pickedNames = []
						rounds+=1
						tm = []
						while(tagged < (limit-totalPicked)):						#While Tagged count is less than 'limit' minus total players moved
							mem = None
							if(len(self.customs)) == 0:								#If there are no more players on the roster, break
								await ctx.send("Roster is empty")
								break
							ran = random.randint(0, (len(self.customs)-1))			#Pick a random index between 0 and the length of the self.customs array
							
							#### If team picked ####
							if(self.customs[ran][:2] == "wj"):
								continue
							else:
								return
							mem = self.svr.get_member(self.customs[ran])			#Retry obtaining members info
							
							self.chosen.append(self.customs[ran])					# Remove player's ability to rejoin the roster or get picked again
							del self.customs[ran]									#/
							subr.save(self)
							
							try:														#\
								pickedUsers.append(mem.id)								# - Stores player's info in new arrays for ease of access
								pickedNames.append(mem.mention)							#/
								def is_mentioned(m):									#\
									return mem in m.mentions							# - Removes all mentions in the last 100 messages of the chosen member
								await ctx.channel.purge(limit=100, check=is_mentioned)	#/
							except:
								try:
									await self.thunder.send("Error - " + mem.id + " | " + mem.discriminator) #If the above fails, message Thunder with some debug information
								except:
									try:
										await self.thunder.send(self.customs[ran] + " has produced an error")
									except:
										await self.thunder.send("Something broke")
										
							
								
							try:
								await mem.send("You have been picked for WackyJacky101's Custom Match Team! Please join the Waiting Room voice chat! <https://discord.gg/aYdYxBn>")							#Attempt to DM the user with a link to quickly join the voice chat channel.
							except:
								tm.append(mem.mention)							#Adds user mention to variable so they can be mentioned as NOT having DMs enabled.
							tagged = tagged + 1
							
						try:
							await ctx.send(", ".join(pickedNames) + ": Please join the Waiting Room voice chat")	#Tag all users in one message about joining the voice channel
						except:
							try:
								await self.thunder.send(str(pickedNames))		#If above fails, try to send Thunder a list of the names
							except:
								None
						#Can't DM
						if(len(tm)>0):
							tempmess = await ctx.send(", ".join(tm) + ": Cannot receive DMs from WJBot.")
							await asyncio.sleep(10)
							await tempmess.delete()
							tm = []
						#Auto Move#
						await asyncio.sleep(90)									#Gives 90 seconds to join voice channel
						for i in self.waitr.members:							#Cycle through the users in the waiting room
							for j in pickedUsers:								#Check all users that have been picked in the roster
								if str(i.id) == str(j):							#If user is in the voice chat AND been picked in the roster
									totalPicked = totalPicked + 1				#Increment totalPicked by 1 so we don't pick more than necessary
									await i.edit(voice_channel = self.streamr)	#Move user to Stream Room voice chat with Wacky
									
						if(str(totalPicked) == str(limit)):
							None
							#await self.thunder.send("Your team of " + str(totalPicked) + " is ready and waiting for the next round in voice chat")
						elif(rounds == 3):
							await ctx.send(self.rm.mention + " - Picking complete - " + str(limit-totalPicked) + " remaining.")
							#Mentions Roster Manager as roster has run through 3 times and still not got a full team
							break
	
	@commands.command(pass_context=True)
	async def timeout(self, ctx, usr: discord.Member, days, reason):
		if(subr.channelTest(self, ctx) == 1):
			ctx.message.delete()
			if(subr.roleCheck(self, ctx.author)) and (str(ctx.channel.name)) == "club_distruptions_log":
				role = discord.utils.get(self.svr.roles, id=475261440953942029)
				await usr.add_roles(role)
				curdate = str(datetime.now().strftime("%d:%m:%y"))
				bandate = str(datetime.now() + timedelta(days=(int((days)))+1))
				bandate = bandate[8:10] + "-" + bandate[5:7] + "-" + bandate[0:4]
				list = [usr.id, str(usr.name), bandate, reason, str(ctx.author.name), curdate]
				self.bans.append(list)
				with open(self.path + "bans.json", 'w') as outfile:
					json.dump(self.bans, outfile)
				subr.save(self)
				bc = self.bansLog.count(str(usr.id))
				await ctx.send(usr.name + " has been timed out by " + str(ctx.author.name) + " for " + days + " days for the reason of: " + reason)
				await ctx.author.send(usr.name + "'s total timeouts now stands at: " + str(bc + 1))
	
	@commands.command(pass_context = True)
	async def banChecks(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			await subr.banCheck(self, passive=1)
	
	@commands.group(pass_context=True, no_pm=True)
	async def roster(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if(subr.roleCheck(self, ctx.author)):
				if ctx.invoked_subcommand is None:
					try:
						await ctx.author.send("Invalid argument, please type !rhelp for help with commands you can use")
					except:
						None
	
	@roster.group(pass_context=True, no_pm=True, name="close")
	async def roster_close(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				await subr.closeRoster(self, ctx.message)
				await ctx.send("@here The Roster is now closed! Please DM the bot using !removeme if you wish to be removed from the Roster", filter=None)	#Display message mentioning all the Roster is now closed
	
	@roster.group(pass_context=True, name="list")
	async def roster_list(self, ctx, spt=""):
		if(subr.channelTest(self, ctx) == 1):
			if(subr.roleCheck(self, ctx.message.author)):
				count = len(self.customs)																#Count for the remaining player not self.chosen
				noms = []
				if spt == "names":																		#-\
					for nom in self.customs:
						if type(nom) is Discord.member:
							noms.append(self.svr.get_member(nom).mention)
						else:
							noms.append(nom)
					noms = "Customs Roster Total: " + str(count) + "\n" + ", ".join(noms)				#--Begins the start of the send_message but stores to avoid pinging up to 21 times!
					
					try:
						await ctx.author.send(noms)													#Finally sends the store as a DM/send_message to the user that called the command
					except:
						return
				else:
					await ctx.send("Customs Roster total: " + str(count) + "%s" %(" participant" if count == 1 else " participants"))				#Shows total players left in chat
	
	@roster.group(pass_context=True, no_pm=True, name="reset")
	async def roster_reset(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			self.customs = []
			self.chosen = []
			self.teams = []
			subr.save(self)
			await ctx.send("Roster has been reset")
	
	@roster.group(pass_context=True, no_pm=True, name="history")
	async def roster_history(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				his = "Roster Players Already Selected:\n\n"										#Begins the string so all is sent as one message
				try:
					await ctx.author.send(his + ", ".join(self.chosen))	#Finally DMs moderator with all players in the roster who have already played
				except:
					cl = await ctx.send("Cannot DM user")
					await asyncio.sleep(3)
					cl.delete()
	
	@roster.group(pass_context=True, no_pm=True, name="end")
	async def roster_end(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				del self.customs[:]																#\
				del self.chosen[:]																#-- Resets self.customs and self.chosen lists
				subr.save(self)
				for a in self.svr.roles:														#----- Denies users read/send messages permissions
					if (str(a) in self.sRoles) or (str(a) in self.pRoles):						#---/
						role = a																#--/
						await ctx.channel.set_permissions(a, send_messages = False, read_messages = False)
				for x in self.svr.channels:
					if str(x) in self.events:
						await x.set_permissions(self.svr.default_role, read_messages = False)
					if str(x) == "event-chat":
						await x.set_permissions(self.svr.default_role, read_messages = False)
				await self.svr.get_channel(406520047134048256).set_permissions(self.svr.default_role, read_messages = False, connect = False)
	
	@roster.group(pass_context=True, no_pm=True, name="open")
	async def roster_open(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				await subr.openRoster(self, ctx, 1)											
				await ctx.send("@here Roster for playing with Wacky is now open until further notice. Please type !addme to join, and remember to do !removeme if you can't attend after all. For more information about the queue system please read the pinned message", filter=None)
	
	@roster.group(pass_context=True, no_pm=True, name="silent") #Silently open/close the Roster
	async def roster_silent(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			await ctx.message.delete()
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				if self.rSwitch == 0:					#Open
					await subr.openRoster(self, ctx, 0)
					await ctx.send("The Roster is now open! Please type !addme to join. For more information about the queue system please read the pinned message.", filter=None)
				else:									#Close
					await subr.closeRoster(self, ctx)
					await ctx.send("The Roster is now closed! Please DM the bot using !removeme if you wish to be removed from the Roster", filter=None)
	
	@roster.group(pass_context=True, no_pm=True, name="load") #Load the current Roster, this is used in case the Bot restarts - Automatically called when opening the roster or using silent
	async def roster_load(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				subr.load(self)
				await ctx.author.send("Roster loaded successfully")
	
	@roster.group(pass_context=True, no_pm=True, name="clear")			#Clear the channel of all messages (except pinned) only if the channel is in self.channels
	async def roster_clear(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			if((subr.roleCheck(self, ctx.message.author)) and (str(ctx.message.channel.name) in self.channels)):
				def is_pinned(m):
					if m.pinned == True:
						return 0
					else:
						return 1
				await ctx.channel.purge(limit=200, check=is_pinned)
				cl = await ctx.send("Messages Cleared")
				await asyncio.sleep(3)
				await cl.delete()
	
	@roster.group(pass_context=True, name="status")
	async def roster_status(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			await ctx.message.delete()
			if(subr.roleCheck(self, ctx.author)):
				whis = "Roster Status:"
				if self.rSwitch == 0:
					whis = whis + "\nClosed | "
				else:
					whis = whis + "\nOpen | "
				
				whis = whis + str(len(self.customs)) + " Participants " if len(self.customs) != 1 else whis + str(len(self.customs)) + " Participant "
				
				await ctx.author.send(whis)
	
	@roster.group(pass_context=True, name="vo")
	async def roster_vo(self, ctx):
		self.customs.append(ctx.author.id)
		subr.save(self)
		#await ctx.send(discord.utils.find(lambda s: s.name == "Roster Manager", self.svr.roles).id)
	
	@roster.group(pass_context=True, name="pass")
	async def roster_pass(self, ctx):
		if(subr.channelTest(self, ctx) == 1):
			ctx.message.delete()
			if (subr.roleCheck(self, ctx.author)):
				def bot_post(m):
					if m.author.id == "424179093094006785":
						return 0
					else:
						return 1
				await ctx.channel.purge(limit=5, check=bot_post)			
				tempp = str(random.randint(0,1000)) #Random 3 digit number for password
				self.passw = "wj" + tempp.rjust(3,"0") #Concatenate wjxxx
				await self.wacky.send("Password for customs has been set to - %s" % self.passw)
				self.passmsg = await self.suppann.send("@here The supporter password for customs is **'%s'** - Please remember do **NOT** share this password with anyone and enjoy the customs!" % self.passw)
	
	@commands.command(pass_context=True)
	async def rhelp(self, ctx):																							#Whispers users/mod the commands they can use
		try:
			if (subr.roleCheck(self, ctx.author)):
				#Moderators
				await ctx.author.send("**WackyJacky101 Customs Roster Commands:**\n\n\
	`If you are in any doubt as to how to control the roster, please contact Thunder or Alli\n\
			`")
			else:
				#Users
				try:
					await ctx.author.send("**WackyJacky101 Customs Roster Commands:**\n\n\
	`!addme    - Put your name into the Roster to play on Wacky's team. Good Luck! Roster must open.\n\
!removeme - Remove your name from the Roster.`")
				except:
					return
		except:
			try:
				await ctx.author.send(subr.roleCheck(self, ctx.author))
			except:
				return