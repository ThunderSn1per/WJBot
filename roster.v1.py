





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-RPWwIpqyjxv5EpuWKUKyeZeWz9QEzIbAWTiYOuxGieUq7+AMiZbsLeQMfEdyEIUoNjLagHK0BEm92BmXnvaH4Q==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-40c1c9d8ff06284fb441108e6559f019.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-3CnDMoFJPvbM39ryV5wc51yRo/6j6eQPt5SOlYaoBZhR9rVL/UZH3ME+wt72nsTlNFaSQ3nXT/0F4sxE1zbA6g==" rel="stylesheet" href="https://github.githubassets.com/assets/github-38162889e1878fa3b887aa360e70ab6c.css" />
    
    
    
    

  <meta name="viewport" content="width=device-width">
  
  <title>WJBot/roster.py at master · ThunderSn1per/WJBot</title>
    <meta name="description" content="Custom Python bot for WackyJacky101 Discord. Contribute to ThunderSn1per/WJBot development by creating an account on GitHub.">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars1.githubusercontent.com/u/47704288?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="ThunderSn1per/WJBot" /><meta property="og:url" content="https://github.com/ThunderSn1per/WJBot" /><meta property="og:description" content="Custom Python bot for WackyJacky101 Discord. Contribute to ThunderSn1per/WJBot development by creating an account on GitHub." />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6Mzc0MDcwMjEwOjg3ZTJjYmQzODI1MTFiNjk3NTQ1ZTMyYjZlNDQ1MGZkZWM4N2Q2MWQ2OTRiOTlhMzkzZjAyNjVjYWU3YWIyODI=--e2abb9fed654496f5e7a3c8cb5c3cc9da8dc10b4">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="CB5E:6032:D6A4FC:199577D:5C705DD9" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

      <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
    <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

  <meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="CB5E:6032:D6A4FC:199577D:5C705DD9" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="47704288" /><meta name="octolytics-actor-login" content="ThunderSn1per" /><meta name="octolytics-actor-hash" content="099969c400dfa008f88c3611fea60c979519cfdb653a88c7c44536e76d277f01" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="554445c303b8963e18d8a399d8b65c18">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="ThunderSn1per">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ODIyOTY1YmRhN2Q4N2NkMjEyNWNhMGZmNzQ2NDg0M2Q5Zjk3MzBiMTFjZjEzMTVjZmUzODU0NTFkZjRjNWY2Znx7InJlbW90ZV9hZGRyZXNzIjoiODIuMjUuMjMyLjM2IiwicmVxdWVzdF9pZCI6IkNCNUU6NjAzMjpENkE0RkM6MTk5NTc3RDo1QzcwNUREOSIsInRpbWVzdGFtcCI6MTU1MDg2NzkzNCwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MARKETPLACE_PLAN_RESTRICTION_EDITOR,NOTIFY_ON_BLOCK,RELATED_ISSUES,MARKETPLACE_BROWSING_V2">

  <meta name="html-safe-nonce" content="6a6bdc5b43d8251ac6479066c308a7067cdb41f2">

  <meta http-equiv="x-pjax-version" content="fe602614af4c1a740e12e3bc8fce8de2">
  

      <link href="https://github.com/ThunderSn1per/WJBot/commits/master.atom" rel="alternate" title="Recent Commits to WJBot:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/ThunderSn1per/WJBot git https://github.com/ThunderSn1per/WJBot.git">

  <meta name="octolytics-dimension-user_id" content="47704288" /><meta name="octolytics-dimension-user_login" content="ThunderSn1per" /><meta name="octolytics-dimension-repository_id" content="171069354" /><meta name="octolytics-dimension-repository_nwo" content="ThunderSn1per/WJBot" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="171069354" /><meta name="octolytics-dimension-repository_network_root_nwo" content="ThunderSn1per/WJBot" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="true" />


    <link rel="canonical" href="https://github.com/ThunderSn1per/WJBot/blob/master/roster.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://github.githubassets.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    


        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 ">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <nav class="d-flex" aria-label="Global">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="171069354" data-scoped-search-url="/ThunderSn1per/WJBot/search" data-unscoped-search-url="/search" action="/ThunderSn1per/WJBot/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <label class="form-control header-search-wrapper header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations#csrf-token=vvPADUMbq6f3aXw3YyxhCLdUYVXiDl0Z9mBFwG9KYofbvB8FsCCSsR3nKvNjnNBHawJsWZZmyPskRMFL8daMlg=="
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0 0 13 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 0 0 0-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"/></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
              <li class="position-relative">
                <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
                   Marketplace
</a>                  
              </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </nav>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:47704288" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown">
    <details class="details-overlay details-reset d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>
      <details-menu class="dropdown-menu dropdown-menu-sw">
        
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="ThunderSn1per/WJBot">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/ThunderSn1per/WJBot/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>


      </details-menu>
    </details>
  </li>

  <li class="dropdown">

    <details class="details-overlay details-reset d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@ThunderSn1per" class="avatar float-left mr-1" src="https://avatars1.githubusercontent.com/u/47704288?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>
      <details-menu class="dropdown-menu dropdown-menu-sw">
        <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/ThunderSn1per" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">ThunderSn1per</strong></a></div>
        <div role="none" class="dropdown-divider"></div>

        <div class="px-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
          
<div class="js-user-status-container user-status-compact" data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link no-underline js-toggle-user-status-edit toggle-user-status-edit width-full" aria-haspopup="dialog" role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:47704288,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:47704288,&quot;client_id&quot;:&quot;2024442839.1539125268&quot;,&quot;originating_request_id&quot;:&quot;CB5E:6032:D6A4FC:199577D:5C705DD9&quot;,&quot;originating_url&quot;:&quot;https://github.com/ThunderSn1per/WJBot/blob/master/roster.py&quot;}}" data-hydro-click-hmac="0ca2803414b4203f7ae964c833f2b5722548b4faa217c5d8c3215e4958838bc7">
      <div class="f6 d-inline-block v-align-middle  user-status-emoji-only-header  circle lh-condensed user-status-header " style="max-width: 29px">
        <div class="user-status-emoji-container flex-shrink-0 mr-1">
          <div><g-emoji class="g-emoji" alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji></div>
        </div>
      </div>
      <div class="d-inline-block v-align-middle user-status-message-wrapper f6 lh-condensed ws-normal pt-1">
            Working from home
      </div>
</summary>    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="X1lN7dGZbkn4ZfwNHPS7YCeFXvkwyPh5q74g3bx6Gj4qeMZWwoQbZ/tEEFNtzd8ZajiPNUbIN4QTCAqZzVMybg==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value=":house:">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container js-suggester-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker bg-white btn-open-emoji-picker">
                  <span class="js-user-status-original-emoji" hidden><div><g-emoji class="g-emoji" alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji></div></span>
                  <span class="js-user-status-custom-emoji"><div><g-emoji class="g-emoji" alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji></div></span>
                  <span class="js-user-status-no-emoji-icon" hidden>
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 0 1-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 0 1-1.45-2.17A6.59 6.59 0 0 1 1.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 0 1 8 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"/></svg>
                  </span>
                </button>
              </span>
              <input type="text" autocomplete="off" autofocus data-maxlength="80" class="js-suggester-field d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field" placeholder="What's happening?" name="message" required value="Working from home" aria-label="What is your current status?">
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div class="suggester-container">
              <div class="suggester js-suggester js-navigation-container" data-url="/autocomplete/user-suggestions" data-no-org-url="/autocomplete/user-suggestions" data-org-url="/suggestions" hidden>
              </div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions" hidden>
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true" id="limited-availability-truncate-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit"  class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button"  class="width-full js-clear-user-status-button btn ml-2 js-user-status-exists">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

        </div>
        <div role="none" class="dropdown-divider"></div>

        <a role="menuitem" class="dropdown-item" href="/ThunderSn1per" data-ga-click="Header, go to profile, text:your profile">Your profile</a>
        <a role="menuitem" class="dropdown-item" href="/ThunderSn1per?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

        <a role="menuitem" class="dropdown-item" href="/ThunderSn1per?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

        <a role="menuitem" class="dropdown-item" href="/ThunderSn1per?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
          <a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a>

        <div role="none" class="dropdown-divider"></div>
        <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="15GC+Fhtx8Gv1awIUsk7D24BD5bGbdqzcas5M0sgs6Z1eepEWTSZPn7rQmNPwrPD99zPzLnvDS4oWKtm4mE5kg==" />
          
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
            Sign out
          </button>
</form>      </details-menu>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="9XN0Mfy6Fx/tnmHsVN/w6Ywo4teAeNPke+9k90NY2ftXmxyN/eNJ4Dygj4dJ1HglFfUijf/6BHkiHPai6hlTzw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">

</div>



  <div role="main" class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      


  





  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">

  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="2MvhcdRx4G0wv6kx6u8axGTZXGJlWAUIVPrzch5cyabpaz2HHQnF2rms0tbaS6XUJq9J0OKCffI9OEi+WOPW4g==" />      <input type="hidden" name="repository_id" id="repository_id" value="171069354" class="form-control" />

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="btn btn-sm btn-with-count select-menu-button" data-ga-click="Repository, click Watch settings, action:blob#show">
          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
              Watch
          </span>
        </summary>
        <details-menu class="select-menu-modal position-absolute mt-5" style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"/></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
      <a class="social-count js-social-count"
        href="/ThunderSn1per/WJBot/watchers"
        aria-label="0 users are watching this repository">
        0
      </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/ThunderSn1per/WJBot/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="e5QNobZLTxZ6JbuFimYmKUhZ2+rQg9VEapQjeidflxLr3vu3AklzF0tmKnbKZQTjBWVOtjrJWui8yl6btFxfPg==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar ThunderSn1per/WJBot"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/ThunderSn1per/WJBot/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/ThunderSn1per/WJBot/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="elnkZG+Wg2gUD2D0HEmcXpHepH2iYfrzjxr/70QpQbM1F34O55DOg+rtemyqYGSB5zOwgfZbzjC+GfROwwfFNw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star ThunderSn1per/WJBot"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star v-align-text-bottom" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/ThunderSn1per/WJBot/stargazers"
           aria-label="0 users starred this repository">
          0
        </a>
</form>  </div>

  </li>

  <li>
        <span class="btn btn-sm btn-with-count disabled tooltipped tooltipped-sw" aria-label="Cannot fork because you own this repository and are not a member of any organizations.">
          <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
          Fork
</span>
    <a href="/ThunderSn1per/WJBot/network/members" class="social-count"
       aria-label="0 users forked this repository">
      0
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=47704288" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ThunderSn1per">ThunderSn1per</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/ThunderSn1per/WJBot">WJBot</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /ThunderSn1per/WJBot" href="/ThunderSn1per/WJBot">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /ThunderSn1per/WJBot/issues" href="/ThunderSn1per/WJBot/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /ThunderSn1per/WJBot/pulls" href="/ThunderSn1per/WJBot/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>


    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /ThunderSn1per/WJBot/projects" href="/ThunderSn1per/WJBot/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>

    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /ThunderSn1per/WJBot/wiki" href="/ThunderSn1per/WJBot/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse alerts security people /ThunderSn1per/WJBot/pulse" href="/ThunderSn1per/WJBot/pulse">
      <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
      Insights
</a>
    <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_settings repo_branch_settings hooks integration_installations repo_keys_settings issue_template_editor /ThunderSn1per/WJBot/settings" href="/ThunderSn1per/WJBot/settings">
      <svg class="octicon octicon-gear" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8.77v-1.6l-1.94-.64-.45-1.09.88-1.84-1.13-1.13-1.81.91-1.09-.45-.69-1.92h-1.6l-.63 1.94-1.11.45-1.84-.88-1.13 1.13.91 1.81-.45 1.09L0 7.23v1.59l1.94.64.45 1.09-.88 1.84 1.13 1.13 1.81-.91 1.09.45.69 1.92h1.59l.63-1.94 1.11-.45 1.84.88 1.13-1.13-.92-1.81.47-1.09L14 8.75v.02zM7 11c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z"/></svg>
      Settings
</a>
</nav>


  </div>
<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
    



  
    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/ThunderSn1per/WJBot/blob/f25f5ea694b2f904c36cf0328a89be4b6e05890e/roster.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v21:3396669636eecc04397c464f8867875b -->

    

    <div class="file-navigation">
      
<details class="details-reset details-overlay select-menu branch-select-menu float-left">
  <summary class="btn btn-sm select-menu-button css-truncate"
           data-hotkey="w"
           
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target">master</span>
  </summary>

  <details-menu class="select-menu-modal position-absolute" style="z-index: 99;" src="/ThunderSn1per/WJBot/ref-list/master/roster.py?source_action=show&amp;source_controller=blob" preload>
    <include-fragment class="select-menu-loading-overlay anim-pulse">
      <svg height="32" class="octicon octicon-octoface" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"/></svg>
    </include-fragment>
  </details-menu>
</details>

      <div class="BtnGroup float-right">
        <a href="/ThunderSn1per/WJBot/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
      <div id="blob-path" class="breadcrumb">
        <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/ThunderSn1per/WJBot"><span>WJBot</span></a></span></span><span class="separator">/</span><strong class="final-path">roster.py</strong>
      </div>
    </div>


    
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/ThunderSn1per/WJBot/commit/f25f5ea694b2f904c36cf0328a89be4b6e05890e" data-pjax>
          f25f5ea
        </a>
        <relative-time datetime="2019-02-17T20:48:52Z">Feb 17, 2019</relative-time>
      </span>
      <div>
        <a rel="author" data-skip-pjax="true" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=47704288" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ThunderSn1per"><img class="avatar" src="https://avatars1.githubusercontent.com/u/47704288?s=40&amp;v=4" width="20" height="20" alt="@ThunderSn1per" /></a>
        <a class="user-mention" rel="author" data-hovercard-type="user" data-hovercard-url="/hovercards?user_id=47704288" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ThunderSn1per">ThunderSn1per</a>
          <a data-pjax="true" title="Test and Change 17/02/2019

Following the roster breaking during customs, testing almost every command in this script to make sure it&#39;s working as much as possible" class="message" href="/ThunderSn1per/WJBot/commit/f25f5ea694b2f904c36cf0328a89be4b6e05890e">Test and Change 17/02/2019</a>
      </div>

    <div class="commit-tease-contributors">
      
<details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark float-left mr-2" id="blob_contributors_box">
  <summary
      class="btn-link"
      aria-haspopup="dialog"
      
      
      >
    
    <span><strong>1</strong> contributor</span>
  </summary>
  <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast " aria-label="Users who have contributed to this file">
    <div class="Box-header">
      <button class="Box-btn-octicon btn-octicon float-right" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <h3 class="Box-title">Users who have contributed to this file</h3>
    </div>
    
        <ul class="list-style-none overflow-auto">
            <li class="Box-row">
              <a class="link-gray-dark no-underline" href="/ThunderSn1per">
                <img class="avatar mr-2" alt="" src="https://avatars1.githubusercontent.com/u/47704288?s=40&amp;v=4" width="20" height="20" />
                ThunderSn1per
</a>            </li>
        </ul>

  </details-dialog>
</details>
      
    </div>
  </div>





    <div class="file ">
      
<div class="file-header">

  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/ThunderSn1per/WJBot/raw/master/roster.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/ThunderSn1per/WJBot/blame/master/roster.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/ThunderSn1per/WJBot/commits/master/roster.py">History</a>
    </div>


        <a class="btn-octicon tooltipped tooltipped-nw"
           href="https://desktop.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/ThunderSn1per/WJBot/edit/master/roster.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="5cWbgSSfnuScCIPDvM2Ub6kRRuLSnwiueVovDEHGAajWK17gMLAbqKtr3yja/fDdKSX3bch+FD3kTFiL6Y4ApQ==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Edit this file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/ThunderSn1per/WJBot/delete/master/roster.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="AjR8N8GWyGDBjzZjgHCt8nwEU4zaD0/E5M7n/vU6JSrpwJjxEL6y8ujQQYQ6+33q2Z9pRfP9culRMeQ5IgFNQQ==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Delete this file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      581 lines (526 sloc)
      <span class="file-info-divider"></span>
    25.8 KB
  </div>
</div>

      

  <div itemprop="text" class="blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>To do</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Custom match settings - https://media.discordapp.net/attachments/358098420130643969/457675735667310592/unknown.png</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Version 0.9 - 02/08/2018</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> discord</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> redbot.core <span class="pl-k">import</span> commands</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> random</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> threading</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> asyncio</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> datetime <span class="pl-k">import</span> datetime, timedelta</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> pprint <span class="pl-k">import</span> pprint</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">BaseCog <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(commands, <span class="pl-s"><span class="pl-pds">&quot;</span>Cog<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">object</span>)</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">subr</span>(<span class="pl-e">BaseCog</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">bot</span>):</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bot <span class="pl-k">=</span> bot</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.rSwitch <span class="pl-k">=</span> <span class="pl-c1">1</span>																		<span class="pl-c"><span class="pl-c">#</span>Toggle Switch to open/close roster - 0/1 = Close/Open</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.mRoles <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Roster Manager<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>You know who<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>WackyBot<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Moderator<span class="pl-pds">&quot;</span></span>]				<span class="pl-c"><span class="pl-c">#</span>Moderator roles</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.pRoles <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Stealth<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Pro<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Chicken Dinner<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Prestige<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Elite<span class="pl-pds">&quot;</span></span>]					<span class="pl-c"><span class="pl-c">#</span>Patreon Roles</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.sRoles <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Twitch Subscriber<span class="pl-pds">&quot;</span></span>]														<span class="pl-c"><span class="pl-c">#</span>Supporter Roles</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.channels <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>wacky_roster<span class="pl-pds">&quot;</span></span>]														<span class="pl-c"><span class="pl-c">#</span>Channels</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.customs <span class="pl-k">=</span> [] 																		<span class="pl-c"><span class="pl-c">#</span>List of players who opt-in</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.chosen <span class="pl-k">=</span> []																		<span class="pl-c"><span class="pl-c">#</span>List of players who have been picked to prevent duplicates</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.teams <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.events <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>Event Lobby<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Event Duo<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Event Squad<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Event 5+ Squad<span class="pl-pds">&quot;</span></span>]				<span class="pl-c"><span class="pl-c">#</span>List of event voice chat categories</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.pwdate <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>18:04<span class="pl-pds">&quot;</span></span>																	<span class="pl-c"><span class="pl-c">#</span>String for the last update to the password</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.passw <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>																			<span class="pl-c"><span class="pl-c">#</span>Password for customs</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.svr <span class="pl-k">=</span> <span class="pl-c1">self</span>.bot.get_guild(<span class="pl-c1">355750209730641920</span>)										<span class="pl-c"><span class="pl-c">#</span>Variable for Server ID</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.wacky <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_member(<span class="pl-c1">290455355316764682</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for WackyJacky101&#39;s ID</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.thunder <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_member(<span class="pl-c1">201303438452064256</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for ThunderSn1per&#39;s ID</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.wackyclub <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">378590577769316352</span>)								<span class="pl-c"><span class="pl-c">#</span>Variable for #the_wacky_club&#39;s ID</span></td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.suppann <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">506534514219024384</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for #supporter_announcements&#39; ID</span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.discordbans <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">377116857812910080</span>)								<span class="pl-c"><span class="pl-c">#</span>Unused variable currently</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.botlog <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">370677704174993417</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for #bot_log&#39;s ID</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.waitr <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">406520047134048256</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for &#39;Waiting Room for WJ Stream&#39; voice channel</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.streamr <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">373851080011939850</span>)									<span class="pl-c"><span class="pl-c">#</span>Variable for &#39;WJ Stream&#39; voice channel</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.rm <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_role(<span class="pl-c1">421679811577118720</span>)											<span class="pl-c"><span class="pl-c">#</span>Variable for &#39;Roster Manager&#39; role</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bans <span class="pl-k">=</span> []																			<span class="pl-c"><span class="pl-c">#</span>Array for bans</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.champs <span class="pl-k">=</span> []																		<span class="pl-c"><span class="pl-c">#</span>Array for Champions</span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.path <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>/root/.local/share/Red-DiscordBot/cogs/CogManager/cogs/roster/<span class="pl-pds">&quot;</span></span>			<span class="pl-c"><span class="pl-c">#</span>Path for main cog, used to keep all external data links in one folder</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.discordBans <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bansLog <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.passmsg <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.blacklist <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&quot;</span>168309055578701824<span class="pl-pds">&quot;</span></span>]													<span class="pl-c"><span class="pl-c">#</span>Blacklisted IDs of users that will NEVER be picked for customs</span></td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">		subr.load(<span class="pl-c1">self</span>)																			<span class="pl-c"><span class="pl-c">#</span>Run the load() function</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">openRoster</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">pw</span>):</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>await ctx.send(self.svr) #Do we have the server saved?</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">		subr.load(<span class="pl-c1">self</span>) <span class="pl-c"><span class="pl-c">#</span>Load preferences</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">		curd <span class="pl-k">=</span> <span class="pl-c1">str</span>(datetime.now().strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span>:%m<span class="pl-pds">&quot;</span></span>)) <span class="pl-c"><span class="pl-c">#</span>Current Date</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(curd <span class="pl-k">!=</span> <span class="pl-c1">self</span>.pwdate) <span class="pl-k">and</span> (pw<span class="pl-k">==</span><span class="pl-c1">1</span>): <span class="pl-c"><span class="pl-c">#</span>if it&#39;s a new day and pw=1 THEN Set a new password</span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">			<span class="pl-c"><span class="pl-c">#</span>SETTING A NEW PASSWORD#</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">self</span>.pwdate <span class="pl-k">=</span> curd <span class="pl-c"><span class="pl-c">#</span>Not a new day anymore</span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">			subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">			tempp <span class="pl-k">=</span> <span class="pl-c1">str</span>(random.randint(<span class="pl-c1">0</span>,<span class="pl-c1">1000</span>)) <span class="pl-c"><span class="pl-c">#</span>Random 3 digit number for password</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">self</span>.passw <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wj<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tempp.rjust(<span class="pl-c1">3</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>0<span class="pl-pds">&quot;</span></span>) <span class="pl-c"><span class="pl-c">#</span>Concatenate wjxxx</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> <span class="pl-c1">self</span>.wacky.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Password for customs has been set to - <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">self</span>.passw)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">self</span>.passmsg <span class="pl-k">=</span> <span class="pl-k">await</span> <span class="pl-c1">self</span>.suppann.send(<span class="pl-s"><span class="pl-pds">&quot;</span>The supporter password for customs is **&#39;<span class="pl-c1">%s</span>&#39;** - Please remember do **NOT** share this password with anyone and enjoy the customs!<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">self</span>.passw)</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.waitr <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">406520047134048256</span>) <span class="pl-c"><span class="pl-c">#</span>Waiting Room ID</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">		subr.load(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.rSwitch <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>Customs Roster Channel Permissions</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> a <span class="pl-k">in</span> <span class="pl-c1">self</span>.svr.roles:</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.sRoles) <span class="pl-k">or</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.pRoles):</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.channel.set_permissions(a, <span class="pl-v">send_messages</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">					<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>Event Category Permissions</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">self</span>.svr.channels:</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> <span class="pl-c1">str</span>(x) <span class="pl-k">in</span> <span class="pl-c1">self</span>.events:</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> x.set_permissions(<span class="pl-c1">self</span>.svr.default_role, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>Waiting Room Permissions</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">await</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">406520047134048256</span>).set_permissions(<span class="pl-c1">self</span>.svr.default_role, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>, <span class="pl-v">connect</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">closeRoster</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">msg</span>: discord.Message):</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.rSwitch <span class="pl-k">=</span> <span class="pl-c1">0</span>														<span class="pl-c"><span class="pl-c">#</span>Turns the Roster off</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bloc <span class="pl-k">=</span> <span class="pl-c1">0</span>															<span class="pl-c"><span class="pl-c">#</span>Allows the @here message upon opening</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> a <span class="pl-k">in</span> <span class="pl-c1">self</span>.svr.roles:												<span class="pl-c"><span class="pl-c">#</span>----- Denies users read/send messages permissions</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.sRoles) <span class="pl-k">or</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.pRoles):				<span class="pl-c"><span class="pl-c">#</span>---/</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> msg.channel.set_permissions(a, <span class="pl-v">send_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">banCheck</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">passive</span><span class="pl-k">=</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> <span class="pl-c1">str</span>(datetime.now().strftime(<span class="pl-s"><span class="pl-pds">&quot;</span>%H<span class="pl-pds">&quot;</span></span>)) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>00<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">			curdate <span class="pl-k">=</span> <span class="pl-c1">str</span>(datetime.now().strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span>-%m-%Y<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">			count <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">for</span> m <span class="pl-k">in</span> <span class="pl-c1">self</span>.bans:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">				count <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> m[<span class="pl-c1">2</span>] <span class="pl-k">==</span> curdate:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">					role <span class="pl-k">=</span> discord.utils.get(<span class="pl-c1">self</span>.svr.roles, <span class="pl-v">id</span><span class="pl-k">=</span><span class="pl-c1">475261440953942029</span>)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">					tu <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_member(<span class="pl-c1">int</span>(m[<span class="pl-c1">0</span>]))</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> tu.remove_roles(role)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">try</span>: <span class="pl-k">await</span> tu.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You are no longer timed out, please adhere to the rules in future<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">except</span>: <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">					pprint(<span class="pl-c1">self</span>.bansLog)</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">					<span class="pl-c1">self</span>.bansLog.append(m[<span class="pl-c1">0</span>])</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">					pprint(<span class="pl-c1">self</span>.bansLog)</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">del</span> <span class="pl-c1">self</span>.bans[count]</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">					subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3600</span>)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">			subr.banCheck(<span class="pl-c1">self</span>, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3600</span>)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">			subr.banCheck(<span class="pl-c1">self</span>, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-en">save</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>roster.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.customs, outfile)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>chosen.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.chosen, outfile)</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">dict</span> <span class="pl-k">=</span> {<span class="pl-s"><span class="pl-pds">&quot;</span>pwdate<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">self</span>.pwdate, <span class="pl-s"><span class="pl-pds">&quot;</span>champs<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">self</span>.champs}</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>misc.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">dict</span>, outfile)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>dBans.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.discordBans, outfile)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>fBans.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.faceitBans, outfile)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bansLog.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.bansLog, outfile)</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bans.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">			json.dump(<span class="pl-c1">self</span>.bans, outfile)</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">			</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-en">load</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.customs <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>roster.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.chosen <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>chosen.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">dict</span> <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>misc.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bans <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bans.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.discordBans <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>dBans.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.faceitBans <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>fBans.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.bansLog <span class="pl-k">=</span> json.load(<span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bansLog.json<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(<span class="pl-c1">self</span>.pwdate<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>18:04<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">			subr.banCheck(<span class="pl-c1">self</span>, <span class="pl-v">passive</span><span class="pl-k">=</span><span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.pwdate <span class="pl-k">=</span> dict[<span class="pl-s"><span class="pl-pds">&quot;</span>pwdate<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.champs <span class="pl-k">=</span> dict[<span class="pl-s"><span class="pl-pds">&quot;</span>champs<span class="pl-pds">&quot;</span></span>]</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-en">roleCheck</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">user</span>):</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">		uRoles <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">for</span> u <span class="pl-k">in</span> user.roles:</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">			uRoles.append(<span class="pl-c1">str</span>(u))</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">return</span> (<span class="pl-c1">set</span>(uRoles).intersection(<span class="pl-c1">self</span>.mRoles))</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-en">channelTest</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(ctx.message.guild <span class="pl-k">is</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">return</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">return</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">def</span> <span class="pl-en">checkBlacklist</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">		uid <span class="pl-k">=</span> <span class="pl-c1">str</span>(ctx.author.id)</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">return</span> (uid <span class="pl-k">in</span> <span class="pl-c1">self</span>.blacklist)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">on_message</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">message</span>):</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(message.guild <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">and</span> message.author.id <span class="pl-k">!=</span> <span class="pl-c1">424179093094006785</span>):</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> message.channel.send(<span class="pl-s"><span class="pl-pds">&quot;</span>DMs are not allowed<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(<span class="pl-c1">str</span>(message.channel) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wacky_roster<span class="pl-pds">&quot;</span></span>) <span class="pl-k">and</span> (<span class="pl-c1">self</span>.rSwitch <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, message.author)):</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span>(message.author.id <span class="pl-k">==</span> <span class="pl-c1">424179093094006785</span>):</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span>(message.content <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>!addme<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> message.delete()</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">						</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(<span class="pl-c1">str</span>(message.channel.name) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>access<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span>(message.content <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>!acceptrules<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> message.delete()</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">					</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(<span class="pl-c1">str</span>(message.channel.name) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>general_chat<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&quot;</span>http<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> message.content <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&quot;</span>www<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> message.content:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, message.author)):</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">						message.delete()</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">						m <span class="pl-k">=</span> <span class="pl-k">await</span> message.channel.send(message.author.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> please read the #rules. No links allowed in #general_chat. Thank you!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">5</span>)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> m.delete()</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">on_member_join</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">member</span>):																				<span class="pl-c"><span class="pl-c">#</span>Server will still need a landing-page. Some users may have disabled receiving private messages from server users which cancels this</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> member.send(<span class="pl-s"><span class="pl-pds">&quot;</span>**Welcome to the WackyJacky101 community!**<span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line"><span class="pl-s">If you are looking for the **supporter password** for custom games, please read this important information:<span class="pl-cce">\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line"><span class="pl-s">1. Link Discord to your Twitch/Patreon accounts (if you haven&#39;t done it yet) under Settings -&gt; Connections.<span class="pl-cce">\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line"><span class="pl-s">2. Wait for up to an hour for the automatic sync to get your Twitch subscriber role<span class="pl-cce">\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line"><span class="pl-s">3. After you have your role, you will find the password pinned in #the_wacky_club (how to see pinned messages: &lt;https://tinyurl.com/yd662tfg&gt;) <span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line"><span class="pl-s">If you weren&#39;t in need of this information we apologize for the ping - thank you for joining us! :heart: <span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Best regards from WackyJacky101 and the moderator team<span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line"><span class="pl-s">PS. You will not be able to chat for the first 10 minutes. While you wait, please familiarize yourself with the **#rules**. Thanks!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">acceptrules</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(<span class="pl-c1">str</span>(ctx.channel.name)<span class="pl-k">==</span><span class="pl-s"><span class="pl-pds">&quot;</span>access<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">				r <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_role(<span class="pl-c1">501014583511613460</span>)</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.add_roles(r)</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">addme</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.checkBlacklist(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You have been blacklisted and cannot join Wacky&#39;s roster. If you don&#39;t know why, please PM a moderator on Discord.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">elif</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">			user <span class="pl-k">=</span> ctx.author</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">			</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(ctx.author.id <span class="pl-k">==</span> <span class="pl-c1">290455355316764682</span>):</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>@here <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> ctx.author.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> has just attempted to add himself to the Roster. Wacky wants to play himself? :sma:<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">			</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> user.id <span class="pl-k">in</span> <span class="pl-c1">self</span>.customs:												<span class="pl-c"><span class="pl-c">#</span>Check user is already opted in</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You&#39;re already added to the Roster<span class="pl-pds">&quot;</span></span>)				<span class="pl-c"><span class="pl-c">#</span>Reply that user is already opted in</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(user.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - You&#39;re already added to the Roster, cannot DM this user.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">elif</span> user.id <span class="pl-k">in</span> <span class="pl-c1">self</span>.chosen:</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You have already been picked and cannot play again<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(user.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - You have already been picked. Cannot DM this user.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">elif</span> <span class="pl-c1">self</span>.rSwitch <span class="pl-k">==</span> <span class="pl-c1">1</span>:																<span class="pl-c"><span class="pl-c">#</span>Otherwise, make sure Roster is on</span></td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.customs.append(user.id)												<span class="pl-c"><span class="pl-c">#</span>Add user to list</span></td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">				subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.send(user.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> added to the Roster!<span class="pl-pds">&quot;</span></span>)							<span class="pl-c"><span class="pl-c">#</span>Message chat to say user is added</span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Roster is closed<span class="pl-pds">&quot;</span></span>)									<span class="pl-c"><span class="pl-c">#</span>Otherwise, Roster is closed</span></td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(user.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - Roster is closed, cannot DM this user.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">createteam</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">		</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">addteam</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">a</span>: discord.Member<span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">b</span>: discord.Member<span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">c</span>: discord.Member<span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span> a <span class="pl-k">==</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You need at least 2 members to form a team<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">			</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>Give Unique ID used to join a team</span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>Checks and Adding</span></td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">removeme</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):																<span class="pl-c"><span class="pl-c">#</span>Command to remove yourself from the roster</span></td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">			a <span class="pl-k">=</span> ctx.message.author</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> a.id <span class="pl-k">in</span> <span class="pl-c1">self</span>.chosen:</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You have already been picked, you can&#39;t be be picked again.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">					<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">elif</span>(a.id <span class="pl-k">in</span> <span class="pl-c1">self</span>.customs):</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.customs.remove(a.id)</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"><span class="pl-c">#</span>self.chosen.append(str(a.id)) #-Blocks re-adding</span></td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">				subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">def</span> <span class="pl-en">is_mentioned</span>(<span class="pl-smi">m</span>):</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">return</span> ctx.author <span class="pl-k">in</span> m.mentions</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.channel.purge(<span class="pl-v">limit</span><span class="pl-k">=</span><span class="pl-c1">100</span>, <span class="pl-v">check</span><span class="pl-k">=</span>is_mentioned)</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You have been removed from the Roster<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">					rt <span class="pl-k">=</span> <span class="pl-k">await</span> ctx.send(user.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - You have been removed from the Roster, cannot DM this user.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> rt.delete()</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You are not on the Roster<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">					rt <span class="pl-k">=</span> <span class="pl-k">await</span> ctx.send(ctx.author.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - You are not on the roster, cannot DM this user.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> rt.delete()</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">unpick</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">usr</span>: discord.Member):</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">				uid <span class="pl-k">=</span> usr.id</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> uid <span class="pl-k">in</span> <span class="pl-c1">self</span>.chosen:</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">					<span class="pl-c1">self</span>.customs.append(uid)</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">					<span class="pl-c1">self</span>.chosen.remove(uid)</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(usr.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> is back on the Roster!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(usr.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> is not on the chosen list and cannot be unpicked<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">pick</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">limit</span><span class="pl-k">=</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> (subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span>(limit <span class="pl-k">&gt;</span> <span class="pl-c1">3</span>): limit <span class="pl-k">=</span> <span class="pl-c1">3</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">				pickedUsers <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">				totalPicked <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">				rounds <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span>(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)<span class="pl-k">&gt;</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">while</span>(totalPicked <span class="pl-k">&lt;</span> limit):</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">						tagged <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">						pickedUsers <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">						pickedNames <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">						rounds<span class="pl-k">+=</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">						tm <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">while</span>(tagged <span class="pl-k">&lt;</span> (limit<span class="pl-k">-</span>totalPicked)):						<span class="pl-c"><span class="pl-c">#</span>While Tagged count is less than &#39;limit&#39; minus total players moved</span></td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">							mem <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">if</span>(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)) <span class="pl-k">==</span> <span class="pl-c1">0</span>:								<span class="pl-c"><span class="pl-c">#</span>If there are no more players on the roster, break</span></td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Roster is empty<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">							ran <span class="pl-k">=</span> random.randint(<span class="pl-c1">0</span>, (<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)<span class="pl-k">-</span><span class="pl-c1">1</span>))			<span class="pl-c"><span class="pl-c">#</span>Pick a random index between 0 and the length of the self.customs array</span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">							</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">await</span> <span class="pl-c1">self</span>.thunder.send(<span class="pl-s"><span class="pl-pds">&quot;</span>ran = <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(ran) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> | cuid = <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">self</span>.customs[ran]) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> | total = <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)))</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">							</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">							mem <span class="pl-k">=</span> <span class="pl-c1">self</span>.svr.get_member(<span class="pl-c1">self</span>.customs[ran])		<span class="pl-c"><span class="pl-c">#</span>Retry obtaining members info</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">							</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">							<span class="pl-c1">self</span>.chosen.append(<span class="pl-c1">self</span>.customs[ran])					<span class="pl-c"><span class="pl-c">#</span> Remove player&#39;s ability to rejoin the roster or get picked again</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">del</span> <span class="pl-c1">self</span>.customs[ran]									<span class="pl-c"><span class="pl-c">#</span>/</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">							subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">							</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">try</span>:														<span class="pl-c"><span class="pl-c">#</span>\</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">								pickedUsers.append(mem.id)								<span class="pl-c"><span class="pl-c">#</span> - Stores player&#39;s info in new arrays for ease of access</span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">								pickedNames.append(mem.mention)							<span class="pl-c"><span class="pl-c">#</span>/</span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">def</span> <span class="pl-en">is_mentioned</span>(<span class="pl-smi">m</span>):									<span class="pl-c"><span class="pl-c">#</span>\</span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">									<span class="pl-k">return</span> mem <span class="pl-k">in</span> m.mentions							<span class="pl-c"><span class="pl-c">#</span> - Removes all mentions in the last 100 messages of the chosen member</span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">await</span> ctx.channel.purge(<span class="pl-v">limit</span><span class="pl-k">=</span><span class="pl-c1">100</span>, <span class="pl-v">check</span><span class="pl-k">=</span>is_mentioned)	<span class="pl-c"><span class="pl-c">#</span>/</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">									<span class="pl-k">await</span> <span class="pl-c1">self</span>.thunder.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Error - <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> mem.id <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> | <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> mem.discriminator) <span class="pl-c"><span class="pl-c">#</span>If the above fails, message Thunder with some debug information</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">									<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">										<span class="pl-k">await</span> <span class="pl-c1">self</span>.thunder.send(<span class="pl-c1">self</span>.customs[ran] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> has produced an error<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">									<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">										<span class="pl-k">await</span> <span class="pl-c1">self</span>.thunder.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Something broke<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">										</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">							</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">								</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">await</span> mem.send(<span class="pl-s"><span class="pl-pds">&quot;</span>You have been picked for WackyJacky101&#39;s Custom Match Team! Please join the Waiting Room voice chat! &lt;https://discord.gg/aYdYxBn&gt;<span class="pl-pds">&quot;</span></span>)							<span class="pl-c"><span class="pl-c">#</span>Attempt to DM the user with a link to quickly join the voice chat channel.</span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">								tm.append(mem.mention)							<span class="pl-c"><span class="pl-c">#</span>Adds user mention to variable so they can be mentioned as NOT having DMs enabled.</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">							tagged <span class="pl-k">=</span> tagged <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(pickedNames) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>: Please join the Waiting Room voice chat<span class="pl-pds">&quot;</span></span>)	<span class="pl-c"><span class="pl-c">#</span>Tag all users in one message about joining the voice channel</span></td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">await</span> <span class="pl-c1">self</span>.thunder.send(<span class="pl-c1">str</span>(pickedNames))		<span class="pl-c"><span class="pl-c">#</span>If above fails, try to send Thunder a list of the names</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">								<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">						<span class="pl-c"><span class="pl-c">#</span>Can&#39;t DM</span></td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span>(<span class="pl-c1">len</span>(tm)<span class="pl-k">&gt;</span><span class="pl-c1">0</span>):</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">							tempmess <span class="pl-k">=</span> <span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(tm) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>: Cannot receive DMs from WJBot.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">10</span>)</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">await</span> tempmess.delete()</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">							tm <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">						<span class="pl-c"><span class="pl-c">#</span>Auto Move#</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">90</span>)									<span class="pl-c"><span class="pl-c">#</span>Gives 90 seconds to join voice channel</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">self</span>.waitr.members:							<span class="pl-c"><span class="pl-c">#</span>Cycle through the users in the waiting room</span></td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">for</span> j <span class="pl-k">in</span> pickedUsers:								<span class="pl-c"><span class="pl-c">#</span>Check all users that have been picked in the roster</span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">								<span class="pl-k">if</span> <span class="pl-c1">str</span>(i.id) <span class="pl-k">==</span> <span class="pl-c1">str</span>(j):							<span class="pl-c"><span class="pl-c">#</span>If user is in the voice chat AND been picked in the roster</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">									totalPicked <span class="pl-k">=</span> totalPicked <span class="pl-k">+</span> <span class="pl-c1">1</span>				<span class="pl-c"><span class="pl-c">#</span>Increment totalPicked by 1 so we don&#39;t pick more than necessary</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">									<span class="pl-k">await</span> i.edit(<span class="pl-v">voice_channel</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.streamr)	<span class="pl-c"><span class="pl-c">#</span>Move user to Stream Room voice chat with Wacky</span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">									</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">if</span>(<span class="pl-c1">str</span>(totalPicked) <span class="pl-k">==</span> <span class="pl-c1">str</span>(limit)):</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">							<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">							<span class="pl-c"><span class="pl-c">#</span>await self.thunder.send(&quot;Your team of &quot; + str(totalPicked) + &quot; is ready and waiting for the next round in voice chat&quot;)</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">elif</span>(rounds <span class="pl-k">==</span> <span class="pl-c1">3</span>):</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">await</span> ctx.send(<span class="pl-c1">self</span>.rm.mention <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> - Picking complete - <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(limit<span class="pl-k">-</span>totalPicked) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> remaining.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">							<span class="pl-c"><span class="pl-c">#</span>Mentions Roster Manager as roster has run through 3 times and still not got a full team</span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">							<span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">timeout</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">usr</span>: discord.Member, <span class="pl-smi">days</span>, <span class="pl-smi">reason</span>):</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">			ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.channel.name)) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>club_distruptions_log<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">				role <span class="pl-k">=</span> discord.utils.get(<span class="pl-c1">self</span>.svr.roles, <span class="pl-v">id</span><span class="pl-k">=</span><span class="pl-c1">475261440953942029</span>)</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> usr.add_roles(role)</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">				curdate <span class="pl-k">=</span> <span class="pl-c1">str</span>(datetime.now().strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%d</span>:%m:%y<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">				bandate <span class="pl-k">=</span> <span class="pl-c1">str</span>(datetime.now() <span class="pl-k">+</span> timedelta(<span class="pl-v">days</span><span class="pl-k">=</span>(<span class="pl-c1">int</span>((days)))<span class="pl-k">+</span><span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">				bandate <span class="pl-k">=</span> bandate[<span class="pl-c1">8</span>:<span class="pl-c1">10</span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> bandate[<span class="pl-c1">5</span>:<span class="pl-c1">7</span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> bandate[<span class="pl-c1">0</span>:<span class="pl-c1">4</span>]</td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">list</span> <span class="pl-k">=</span> [usr.id, <span class="pl-c1">str</span>(usr.name), bandate, reason, <span class="pl-c1">str</span>(ctx.author.name), curdate]</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.bans.append(<span class="pl-c1">list</span>)</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">with</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bans.json<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> outfile:</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">					json.dump(<span class="pl-c1">self</span>.bans, outfile)</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">				subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">				bc <span class="pl-k">=</span> <span class="pl-c1">self</span>.bansLog.count(<span class="pl-c1">str</span>(usr.id))</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.send(usr.name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> has been timed out by <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(ctx.author.name) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> for <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> days <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> days for the reason of: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> reason)</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(usr.name <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>&#39;s total timeouts now stands at: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(bc <span class="pl-k">+</span> <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span> <span class="pl-k">=</span> <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">banChecks</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> subr.banCheck(<span class="pl-c1">self</span>, <span class="pl-v">passive</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> ctx.invoked_subcommand <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Invalid argument, please type !rhelp for help with commands you can use<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">						<span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>close<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_close</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> subr.closeRoster(<span class="pl-c1">self</span>, ctx.message)</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>@here The Roster is now closed! Please DM the bot using !removeme if you wish to be removed from the Roster<span class="pl-pds">&quot;</span></span>, <span class="pl-v">filter</span><span class="pl-k">=</span><span class="pl-c1">None</span>)	<span class="pl-c"><span class="pl-c">#</span>Display message mentioning all the Roster is now closed</span></td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>list<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_list</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>, <span class="pl-smi">spt</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)):</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">				count <span class="pl-k">=</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)																<span class="pl-c"><span class="pl-c">#</span>Count for the remaining player not self.chosen</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">				noms <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> spt <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>names<span class="pl-pds">&quot;</span></span>:																		<span class="pl-c"><span class="pl-c">#</span>-\</span></td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">for</span> nom <span class="pl-k">in</span> <span class="pl-c1">self</span>.customs:</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">						noms.append(<span class="pl-c1">self</span>.svr.get_member(nom).mention)</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">					noms <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Customs Roster Total: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(count) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(noms)				<span class="pl-c"><span class="pl-c">#</span>--Begins the start of the send_message but stores to avoid pinging up to 21 times!</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">					</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> ctx.author.send(noms)													<span class="pl-c"><span class="pl-c">#</span>Finally sends the store as a DM/send_message to the user that called the command</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Customs Roster total: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(count) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span>(<span class="pl-s"><span class="pl-pds">&quot;</span> participant<span class="pl-pds">&quot;</span></span> <span class="pl-k">if</span> count <span class="pl-k">==</span> <span class="pl-c1">1</span> <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&quot;</span> participants<span class="pl-pds">&quot;</span></span>))				<span class="pl-c"><span class="pl-c">#</span>Shows total players left in chat</span></td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>reset<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_reset</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">self</span>.customs <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line">			<span class="pl-c1">self</span>.chosen <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">			subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Roster has been reset<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>history<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_history</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line">				his <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Roster Players Already Selected:<span class="pl-cce">\n\n</span><span class="pl-pds">&quot;</span></span>										<span class="pl-c"><span class="pl-c">#</span>Begins the string so all is sent as one message</span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(his <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(<span class="pl-c1">self</span>.chosen))	<span class="pl-c"><span class="pl-c">#</span>Finally DMs moderator with all players in the roster who have already played</span></td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">					cl <span class="pl-k">=</span> <span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Cannot DM user<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">					cl.delete()</td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>end<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_end</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.rSwitch <span class="pl-k">=</span> <span class="pl-c1">0</span>																<span class="pl-c"><span class="pl-c">#</span>Turns the Roster off</span></td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">del</span> <span class="pl-c1">self</span>.customs[:]																<span class="pl-c"><span class="pl-c">#</span>\</span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">del</span> <span class="pl-c1">self</span>.chosen[:]																<span class="pl-c"><span class="pl-c">#</span>-- Resets self.customs and self.chosen lists</span></td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">				subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> a <span class="pl-k">in</span> <span class="pl-c1">self</span>.svr.roles:														<span class="pl-c"><span class="pl-c">#</span>----- Denies users read/send messages permissions</span></td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.sRoles) <span class="pl-k">or</span> (<span class="pl-c1">str</span>(a) <span class="pl-k">in</span> <span class="pl-c1">self</span>.pRoles):						<span class="pl-c"><span class="pl-c">#</span>---/</span></td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">						role <span class="pl-k">=</span> a																<span class="pl-c"><span class="pl-c">#</span>--/</span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> ctx.channel.set_permissions(a, <span class="pl-v">send_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">for</span> x <span class="pl-k">in</span> <span class="pl-c1">self</span>.svr.channels:</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> <span class="pl-c1">str</span>(x) <span class="pl-k">in</span> <span class="pl-c1">self</span>.events:</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> x.set_permissions(<span class="pl-c1">self</span>.svr.default_role, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> <span class="pl-c1">str</span>(x) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>event-chat<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">await</span> x.set_permissions(<span class="pl-c1">self</span>.svr.default_role, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> <span class="pl-c1">self</span>.svr.get_channel(<span class="pl-c1">406520047134048256</span>).set_permissions(<span class="pl-c1">self</span>.svr.default_role, <span class="pl-v">read_messages</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>, <span class="pl-v">connect</span> <span class="pl-k">=</span> <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>open<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_open</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> subr.openRoster(<span class="pl-c1">self</span>, ctx, <span class="pl-c1">1</span>)											</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>@here Roster for playing with Wacky is now open until further notice. Please type !addme to join, and remember to do !removeme if you can&#39;t attend after all. For more information about the queue system please read the pinned message<span class="pl-pds">&quot;</span></span>, <span class="pl-v">filter</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>silent<span class="pl-pds">&quot;</span></span>) <span class="pl-c"><span class="pl-c">#</span>Silently open/close the Roster</span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_silent</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-c1">self</span>.rSwitch <span class="pl-k">==</span> <span class="pl-c1">0</span>:					<span class="pl-c"><span class="pl-c">#</span>Open</span></td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> subr.openRoster(<span class="pl-c1">self</span>, ctx, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>The Roster is now open! Please type !addme to join. For more information about the queue system please read the pinned message.<span class="pl-pds">&quot;</span></span>, <span class="pl-v">filter</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:									<span class="pl-c"><span class="pl-c">#</span>Close</span></td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> subr.closeRoster(<span class="pl-c1">self</span>, ctx)</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>The Roster is now closed! Please DM the bot using !removeme if you wish to be removed from the Roster<span class="pl-pds">&quot;</span></span>, <span class="pl-v">filter</span><span class="pl-k">=</span><span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>load<span class="pl-pds">&quot;</span></span>) <span class="pl-c"><span class="pl-c">#</span>Load the current Roster, this is used in case the Bot restarts - Automatically called when opening the roster or using silent</span></td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_load</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">				subr.load(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Roster loaded successfully<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">no_pm</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>clear<span class="pl-pds">&quot;</span></span>)			<span class="pl-c"><span class="pl-c">#</span>Clear the channel of all messages (except pinned) only if the channel is in self.channels</span></td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_clear</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>((subr.roleCheck(<span class="pl-c1">self</span>, ctx.message.author)) <span class="pl-k">and</span> (<span class="pl-c1">str</span>(ctx.message.channel.name) <span class="pl-k">in</span> <span class="pl-c1">self</span>.channels)):</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">def</span> <span class="pl-en">is_pinned</span>(<span class="pl-smi">m</span>):</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> m.pinned <span class="pl-k">==</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.channel.purge(<span class="pl-v">limit</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">check</span><span class="pl-k">=</span>is_pinned)</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">				cl <span class="pl-k">=</span> <span class="pl-k">await</span> ctx.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Messages Cleared<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> asyncio.sleep(<span class="pl-c1">3</span>)</td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> cl.delete()</td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>status<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_status</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">await</span> ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span>(subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">				whis <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>Roster Status:<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">if</span> <span class="pl-c1">self</span>.rSwitch <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">					whis <span class="pl-k">=</span> whis <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Closed | <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">					whis <span class="pl-k">=</span> whis <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Open | <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">				</td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">				whis <span class="pl-k">=</span> whis <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> Participants <span class="pl-pds">&quot;</span></span> <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs) <span class="pl-k">!=</span> <span class="pl-c1">1</span> <span class="pl-k">else</span> whis <span class="pl-k">+</span> <span class="pl-c1">str</span>(<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.customs)) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> Participant <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">				</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(whis)</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>vo<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_vo</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">		<span class="pl-c1">self</span>.customs.append(ctx.author.id)</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">		subr.save(<span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">		<span class="pl-c"><span class="pl-c">#</span>await ctx.send(discord.utils.find(lambda s: s.name == &quot;Roster Manager&quot;, self.svr.roles).id)</span></td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@roster.group</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">name</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>pass<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">roster_pass</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">if</span>(subr.channelTest(<span class="pl-c1">self</span>, ctx) <span class="pl-k">==</span> <span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">			ctx.message.delete()</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> (subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">def</span> <span class="pl-en">bot_post</span>(<span class="pl-smi">m</span>):</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">if</span> m.author.id <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&quot;</span>424179093094006785<span class="pl-pds">&quot;</span></span>:</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">						<span class="pl-k">return</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.channel.purge(<span class="pl-v">limit</span><span class="pl-k">=</span><span class="pl-c1">5</span>, <span class="pl-v">check</span><span class="pl-k">=</span>bot_post)			</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">				tempp <span class="pl-k">=</span> <span class="pl-c1">str</span>(random.randint(<span class="pl-c1">0</span>,<span class="pl-c1">1000</span>)) <span class="pl-c"><span class="pl-c">#</span>Random 3 digit number for password</span></td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.passw <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>wj<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> tempp.rjust(<span class="pl-c1">3</span>,<span class="pl-s"><span class="pl-pds">&quot;</span>0<span class="pl-pds">&quot;</span></span>) <span class="pl-c"><span class="pl-c">#</span>Concatenate wjxxx</span></td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> <span class="pl-c1">self</span>.wacky.send(<span class="pl-s"><span class="pl-pds">&quot;</span>Password for customs has been set to - <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">self</span>.passw)</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">				<span class="pl-c1">self</span>.passmsg <span class="pl-k">=</span> <span class="pl-k">await</span> <span class="pl-c1">self</span>.suppann.send(<span class="pl-s"><span class="pl-pds">&quot;</span>@here The supporter password for customs is **&#39;<span class="pl-c1">%s</span>&#39;** - Please remember do **NOT** share this password with anyone and enjoy the customs!<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">self</span>.passw)</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">	</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">	<span class="pl-en">@commands.command</span>(<span class="pl-v">pass_context</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">	<span class="pl-k">async</span> <span class="pl-k">def</span> <span class="pl-en">rhelp</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">ctx</span>):																							<span class="pl-c"><span class="pl-c">#</span>Whispers users/mod the commands they can use</span></td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">if</span> (subr.roleCheck(<span class="pl-c1">self</span>, ctx.author)):</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"><span class="pl-c">#</span>Moderators</span></td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>**WackyJacky101 Customs Roster Commands:**<span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	`If you are in any doubt as to how to control the roster, please contact Thunder or Alli<span class="pl-cce">\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line"><span class="pl-s">			`<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">				<span class="pl-c"><span class="pl-c">#</span>Users</span></td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">await</span> ctx.author.send(<span class="pl-s"><span class="pl-pds">&quot;</span>**WackyJacky101 Customs Roster Commands:**<span class="pl-cce">\n\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line"><span class="pl-s">	`!addme    - Put your name into the Roster to play on Wacky&#39;s team. Good Luck! Roster must open.<span class="pl-cce">\n</span><span class="pl-c1">\</span></span></td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line"><span class="pl-s">!removeme - Remove your name from the Roster.`<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">					<span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">		<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">await</span> ctx.author.send(subr.roleCheck(<span class="pl-c1">self</span>, ctx.author))</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">			<span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">				<span class="pl-k">return</span></td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zm5 0a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3zM13 7.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/ThunderSn1per/WJBot/blame/f25f5ea694b2f904c36cf0328a89be4b6e05890e/roster.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/ThunderSn1per/WJBot/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>



  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>
  

  </div>

        
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2019 <span title="0.28837s from unicorn-58f9df96d-ndqf6">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon mr-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-N6BPdqxnrYL4kxWa5gDIlmhui/SEMiHoobwzTpVOWheR111Zxv5GOnCtGpt5qhE5rIpi9RHMeyngI5w6WhGfnw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-0339542411b5666802ea364ae561d67e.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-D/8iR8ROD3vVOmwLSVsS1j1knDeAOuW9NLNRFb3Pyd68G/gC1b3xRH/krz0K2nuECEZRjVsUAU5caoJKAwoLwA==" type="application/javascript" src="https://github.githubassets.com/assets/github-27e2e2875f3fc6cfce6518e479adf7b8.js"></script>
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 0 0 0 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 0 0 .01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark" open>
    <summary aria-haspopup="dialog" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"/></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>

  <div aria-live="polite" class="js-global-screen-reader-notice sr-only"></div>

  </body>
</html>

