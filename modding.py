#To do
#Custom match settings - https://media.discordapp.net/attachments/358098420130643969/457675735667310592/unknown.png
#Version 0.9 - 02/08/2018
import discord
from redbot.core import commands
import random
import schedule
import time
import asyncio
import json
from datetime import datetime, timedelta

BaseCog = getattr(commands, "Cog", object)

mod_logs = []
timeout_logs = []
root_path = "/root/.local/share/Red-DiscordBot/cogs/CogManager/cogs/modding/"

def logs_save():
	print("Saving Logs...")
	with open(root_path + "modlog.json", "w+") as file:
		json.dump(mod_logs, file)
	with open(root_path + "timeoutlog.json", "w+") as file:
		json.dump(timeout_logs, file)

def logs_load():
	mod_logs.extend(json.load(open(root_path + "modlog.json")))
	timeout_logs.extend(json.load(open(root_path + "timeoutlog.json")))
		
logs_load()

class Base(BaseCog):
	def __init__(self, bot):
		self.bot = bot
		self.path = "/root/.local/share/Red-DiscordBot/cogs/CogManager/cogs/modding/"
		self.mRoles = ["Moderator", "WackyBot", "You know who"]
		self.streamSnipers = ["One", "Two", "Three"]
		self.svr = self.bot.get_guild(355750209730641920)
		self.timeout_role = discord.utils.get(self.svr.roles, id=475261440953942029)
		
	
	async def unban_check(self, channel):
		now = datetime.now()
		for idx, log in enumerate(timeout_logs):
			if(log[3] == str(now.date())):
				if(int(now.time().hour) >= 0):
					user = self.svr.get_member(log[1])
					await user.remove_roles(self.timeout_role)
					timeout_logs[idx][3] = "Expired"
					logs_save()
	
	def roleCheck(self, user):
		return (set([str(role) for role in user.roles]).intersection(self.mRoles))
	
	async def on_message(self, message):
		if(message.guild is None and message.author.id != 424179093094006785):
			await message.channel.send("DMs are not allowed")
		else:
			if(Base.roleCheck(self, message.author)):
				await Base.unban_check(self, message.channel)
			
			if(str(message.channel) == "wacky_roster"):
				if(Base.roleCheck(self, message.author)):
					return
				if(message.author.id == 424179093094006785):
					return
				else:
					if(message.content == "!addme"):
						return
					else:
						await message.delete()
						
			if(str(message.channel) == "access"):
				if(message.content == "!acceptrules"):
					return
				else:
					await message.delete()
					
			if(str(message.channel) == "general_chat"):
				if "http" in message.content or "www" in message.content:
					if(Base.roleCheck(self, message.author)):
						return
					else:
						message.delete()
						m = await message.channel.send(message.author.mention + " please read the #rules. No links allowed in #general_chat. Thank you!")
						await asyncio.sleep(10)
						await m.delete()
						
	''' TALK COMMAND '''
	@commands.command(pass_context=True)
	async def talk(self, ctx, channel: discord.TextChannel, msg=""):				#Declare command name and arguments
		await ctx.message.delete()													#Delete the message that was sent
		if(Base.roleCheck(self, ctx.author)):										#Check if user has authority to use command
			try:																	#Attempt the following
				await channel.send(msg)												#Send 'msg' to the 'channel'
				f = open(self.path + "talk.txt", "a+")								#Open/Create 'talk.txt'
				f.write(str(ctx.author.name) + " used talk in #" + str(channel.name) + " to say: " + str(msg) + "\r\n") #Write a new line with details of the mod, msg and channel
				f.close()															#Close 'talk.txt'
			except:																	#If any of the 4 above fails
				tm = await ctx.send("Cannot send messages to #%s" % channel.name)	#Write a message in the current channel saying it's not possible to send the message
				asyncio.sleep(3)													#Wait for 3 seconds
				tm.delete()															#Delete the message
				
	''' STREAM SNIPER COMMANDS '''
	@commands.command(pass_context=True)
	async def ss(self, ctx, usr=None):
		if(Base.roleCheck(self, ctx.author)):
			if usr == None:
				await ctx.send("**Stream Snipers:**```\n" + ('\n'.join(self.streamSnipers)) + "```")
			else:
				await ctx.send(usr)
	
	''' MODERATOR COMMANDS '''
	@commands.command(pass_context=True)
	async def userinfo(self, ctx, *, user: discord.Member = None):
		if(Base.roleCheck(self, ctx.author) == False): return
		"""Show information about a user.
		This includes fields for status, discord join date, server
		join date, voice state and previous names/nicknames.
		If the user has no roles, previous names or previous nicknames,
		these fields will be omitted.
		"""
		author = ctx.author
		guild = ctx.guild

		if not user:
			user = author

		#  A special case for a special someone :^)
		special_date = datetime(2016, 1, 10, 6, 8, 4, 443000)
		is_special = user.id == 96130341705637888 and guild.id == 133049272517001216

		roles = sorted(user.roles)[1:]

		joined_at = user.joined_at if not is_special else special_date
		since_created = (ctx.message.created_at - user.created_at).days
		if joined_at is not None:
			since_joined = (ctx.message.created_at - joined_at).days
			user_joined = joined_at.strftime("%d %b %Y %H:%M")
		else:
			since_joined = "?"
			user_joined = "Unknown"
		user_created = user.created_at.strftime("%d %b %Y %H:%M")
		voice_state = user.voice
		member_number = (
			sorted(guild.members, key=lambda m: m.joined_at or ctx.message.created_at).index(user)
			+ 1
		)

		created_on = ("{}\n({} days ago)").format(user_created, since_created)
		joined_on = ("{}\n({} days ago)").format(user_joined, since_joined)

		activity = ("Chilling in {} status").format(user.status)
		if user.activity is None:  # Default status
			pass
		elif user.activity.type == discord.ActivityType.playing:
			activity = ("Playing {}").format(user.activity.name)
		elif user.activity.type == discord.ActivityType.streaming:
			activity = ("Streaming [{}]({})").format(user.activity.name, user.activity.url)
		elif user.activity.type == discord.ActivityType.listening:
			activity = ("Listening to {}").format(user.activity.name)
		elif user.activity.type == discord.ActivityType.watching:
			activity = ("Watching {}").format(user.activity.name)

		if roles:
			roles = ", ".join([x.name for x in roles])
		else:
			roles = None

		data = discord.Embed(description=activity, colour=user.colour)
		data.add_field(name=("Joined Discord on"), value=created_on)
		data.add_field(name=("Joined this server on"), value=joined_on)
		if roles is not None:
			data.add_field(name=("Roles"), value=roles, inline=False)
		if voice_state and voice_state.channel:
			data.add_field(
				name=("Current voice channel"),
				value="{0.name} (ID {0.id})".format(voice_state.channel),
				inline=False,
			)
		data.set_footer(text=("Member #{} | User ID: {}").format(member_number, user.id))

		name = str(user)
		name = " ~ ".join((name, user.nick)) if user.nick else name

		if user.avatar:
			avatar = user.avatar_url_as(static_format="png")
			data.set_author(name=name, url=avatar)
			data.set_thumbnail(url=avatar)
		else:
			data.set_author(name=name)

		await ctx.send(embed=data)


	@commands.command(pass_context=True)
	async def warn(self, ctx, link, user: discord.Member, reason: str):
		if(Base.roleCheck(self, ctx.author)):
			log_count = len(mod_logs)
			date = datetime.now().date()
			new_log = UserLog(ctx, date, log_count, link, user, reason)
			await new_log.save(ctx)
		
	
	@commands.command(pass_context=True)
	async def view(self, ctx, id=0):
		await ctx.message.delete()
		if(Base.roleCheck(self, ctx.author)):
			if id > (len(mod_logs)-1): id = (len(mod_logs)-1)
			if len(mod_logs) < 1:
				await ctx.send("Moderator logs are currently empty!")
				return
			case = mod_logs[id]
			user = self.svr.get_member(case[1])
			case_object = UserLog(ctx, case[6], id, case[3], user, case[4])
			await case_object.view(ctx)
		
	@commands.command(pass_context=True)
	async def list(self, ctx, user: discord.User, full=False):
		await ctx.message.delete()
		if(Base.roleCheck(self, ctx.author)):
			if len(mod_logs) < 1:
				await ctx.send("Moderator logs are currently empty!")
				return
			user_logs = [log for log in mod_logs if log[1] == user.id]
			await ctx.send(f"{user.mention} has a log count of: {len(user_logs)}")
			if full:
				for log in user_logs:
					case_object = UserLog(ctx, log[6], log[0], log[3], user, log[4])
					await case_object.view(ctx)
					
	@commands.command(pass_context=True)
	async def timeout(self, ctx, link, user: discord.Member, days, reason):
		ut = UserTimeout(ctx, user, link, days, reason)
		await user.add_roles(self.timeout_role)
		await ut.timeout(ctx)
					
	@commands.command(pass_context=True)
	async def listto(self, ctx, user: discord.Member, all=False):
		list_a = timeout_logs[::-1]
		if all:
			for item in list_a:
				if(item[1] == user.id):
					username = self.svr.get_member(item[1])
					embed = discord.Embed(title=f"Timeout Logs Case #{(item[0] + 1)}", colour=discord.Colour(0x307b8), url=item[6], description="Evidence Link")
					embed.add_field(name="Case ID", value=f"{(item[0] + 1)}/{len(timeout_logs)}", inline=True)
					embed.add_field(name=f"by {item[5]}", value=f"on {item[2]} | Expires: {item[3]}", inline=True)
					embed.add_field(name=f"Record against {user.name}#{user.discriminator} for", value=item[4])
					await ctx.send(embed=embed)
		else:
			item = next((i for i in list_a if i[1] == user.id), None)
			if item != None:
				embed = discord.Embed(title=f"Timeout Logs Case #{(item[0] + 1)}", colour=discord.Colour(0x307b8), url=item[6], description="Evidence Link")
				embed.add_field(name="Case ID", value=f"{(item[0] + 1)}/{len(timeout_logs)}", inline=True)
				embed.add_field(name=f"by {item[5]}", value=f"on {item[2]} | Expires: {item[3]}", inline=True)
				embed.add_field(name=f"Record against {user.name}#{user.discriminator} for", value=item[4])
				await ctx.send(embed=embed)
		


class UserLog():
	def __init__(self, ctx, date, log_count, link, user_object, reason):
		self.ID = log_count
		self.link = link
		self.user_object = user_object
		self.user = self.user_object.id
		self.name = self.user_object.name
		self.reason = reason
		self.moderator = ctx.author.name
		self.date = str(date)
		
	
	async def save(self, ctx):
		log_case = [self.ID, self.user, self.name, self.link, self.reason, self.moderator, self.date]
		mod_logs.append(log_case)
		logs_save()
		tm = await ctx.send("Entry saved")
		user_logs = [log for log in mod_logs if log[1] == self.user]
		if len(user_logs) > 2: await ctx.send(f"{self.user_object.mention} has a log count of: {len(user_logs)}")
		await asyncio.sleep(3)
		try:
			await tm.delete()
		except:
			None
	
	
	async def view(self, ctx):
		if len(self.link) > 3:
			embed = discord.Embed(title=f"Moderator Logs Case #{(self.ID + 1)}", colour=discord.Colour(0x84f2b2), description=f"[Evidence Link]({self.link})")
		else:
			embed = discord.Embed(title=f"Moderator Logs Case #{(self.ID + 1)}", colour=discord.Colour(0x84f2b2))
		embed.set_footer()
		embed.add_field(name="Case ID", value=f"{(self.ID + 1)}/{(len(mod_logs))}", inline=True)
		embed.add_field(name=f"by {self.moderator}", value=f"on {self.date}", inline=True)
		embed.add_field(name=f"Record against {self.user_object.name}#{self.user_object.discriminator} for:", value=self.reason, inline=False)
		await ctx.send(embed=embed)
		
class UserTimeout():
	def __init__(self, ctx, user: discord.Member, link, days, reason):
		self.user = user
		self.user_id = user.id
		self.days = days
		self.reason = reason
		self.id = len(timeout_logs)
		self.link = link
	
	async def timeout(self, ctx):
		unban_date = datetime.now().date() + timedelta(days=(int(self.days)+1))
		timeout_logs.append([self.id, self.user_id, str(datetime.now().date()), str(unban_date), self.reason, ctx.author.name, self.link])
		logs_save()
		tm = await ctx.send("Entry saved")
		await asyncio.sleep(3)
		try:
			await tm.delete()
		except:
			None
		

