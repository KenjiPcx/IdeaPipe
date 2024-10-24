### This script is used to extract the groups from gummysearch.com and the subreddits within each group.

import json
from bs4 import BeautifulSoup

html = """
<html lang="en"><head><meta charset="utf-8"><link rel="shortcut icon" href="/images/branding-logo-body-square.png"><meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit=no"><link rel="apple-touch-icon" sizes="180x180" href="/images/branding-logo-body-outline.png"><link rel="apple-touch-icon" sizes="120x120" href="/images/branding-logo-body-outline.png"><link rel="apple-touch-icon" sizes="167x167" href="/images/branding-logo-body-outline.png"><link rel="apple-touch-icon" sizes="152x152" href="/images/branding-logo-body-outline.png"><link rel="apple-touch-icon" sizes="144x144" href="/images/branding-logo-body-outline.png"><meta name="theme-color" content="#000000"><link rel="manifest" href="/manifest.json"><title>Audiences | Curated</title><meta property="robots" content="noindex, follow"><meta property="og:url" content="https://go.gummysearch.com"><meta property="og:type" content="website"><meta property="og:title" content="GummySearch - Reddit Audience Research"><meta property="og:image" content="https://go.gummysearch.com/images/social-share-image.png"><meta property="description" content="Quickly discover your customer's pain points, what solutions they need, and what they are eager to pay for"><meta property="og:description" content="Quickly discover your customer's pain points, what solutions they need, and what they are eager to pay for"><meta property="twitter:card" content="summary_large_image"><meta property="twitter:creator" content="@gummy_search"><meta property="twitter:title" content="GummySearch - Reddit Audience Research"><meta property="twitter:description" content="Quickly discover your customer's pain points, what solutions they need, and what they are eager to pay for"><script src="https://js-agent.newrelic.com/nr-spa-1210.min.js"></script><script async="" crossorigin="anonymous" src="https://edge.fullstory.com/s/fs.js"></script><script src="https://assets.churnkey.co/js/app.js?appId=wq8d877hj" async=""></script><script type="text/javascript" async="" src="https://app.posthog.com/static/array.js"></script><script async="" src="https://www.googletagmanager.com/gtag/js?id=G-LEPHGWM3SM"></script><script>{function gtag(){dataLayer.push(arguments)}window.dataLayer=window.dataLayer||[],gtag("js",new Date),gtag("config","G-LEPHGWM3SM")}</script><script type="text/javascript" src="/newrelic.js"></script><script>NREUM.loader_config={accountID:"3145432",trustKey:"3145432",agentID:"485240809",licenseKey:"NRJS-b4a46d9c8473c8a09f2",applicationID:"485230763"},NREUM.info={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",licenseKey:"NRJS-b4a46d9c8473c8a09f2",applicationID:"485230763",sa:1}</script><script defer="defer" data-domain="go.gummysearch.com,roll-up.gummysearch.com" src="https://plausible.io/js/plausible.js"></script><script>!function(n,u){n._rwq=u,n[u]=n[u]||function(){(n[u].q=n[u].q||[]).push(arguments)}}(window,"rewardful")</script><script async="" src="https://r.wdfl.co/rw.js" data-rewardful="ef0d4a"></script><script>!function(t,e){var o,r,n,s;e.__SV||(window.posthog=e,e._i=[],e.init=function(a,p,i){function c(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(n=t.createElement("script")).type="text/javascript",n.async=!0,n.src=p.api_host+"/static/array.js",(s=t.getElementsByTagName("script")[0]).parentNode.insertBefore(n,s);var g=e;for(void 0!==i?g=e[i]=[]:i="posthog",g.people=g.people||[],g.toString=function(t){var e="posthog";return"posthog"!==i&&(e+="."+i),t||(e+=" (stub)"),e},g.people.toString=function(){return g.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),r=0;r<o.length;r++)c(g,o[r]);e._i.push([a,p,i])},e.__SV=1)}(document,window.posthog||[]),posthog.init("phc_18klnizkxU7egM2kVcRzEgHC26I2A6TLjCjC0eLMOtf",{api_host:"https://app.posthog.com"})</script><script>!function(){if(!window.churnkey||!window.churnkey.created){window.churnkey={created:!0};const e=document.createElement("script");e.src="https://assets.churnkey.co/js/app.js?appId=wq8d877hj",e.async=!0;const n=document.getElementsByTagName("script")[0];n.parentNode.insertBefore(e,n)}}()</script><link href="/static/css/2.aacdaee8.chunk.css" rel="stylesheet"><link href="/static/css/main.6ea19709.chunk.css" rel="stylesheet"><link type="text/css" rel="stylesheet" href="https://assets.churnkey.co/css/app.css"><style data-react-tooltip="true">.__react_component_tooltip {
  border-radius: 3px;
  display: inline-block;
  font-size: 13px;
  left: -999em;
  opacity: 0;
  padding: 8px 21px;
  position: fixed;
  pointer-events: none;
  transition: opacity 0.3s ease-out;
  top: -999em;
  visibility: hidden;
  z-index: 999;
}
.__react_component_tooltip.allow_hover, .__react_component_tooltip.allow_click {
  pointer-events: auto;
}
.__react_component_tooltip::before, .__react_component_tooltip::after {
  content: "";
  width: 0;
  height: 0;
  position: absolute;
}
.__react_component_tooltip.show {
  opacity: 0.9;
  margin-top: 0;
  margin-left: 0;
  visibility: visible;
}
.__react_component_tooltip.place-top::before {
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  bottom: -8px;
  left: 50%;
  margin-left: -10px;
}
.__react_component_tooltip.place-bottom::before {
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  top: -8px;
  left: 50%;
  margin-left: -10px;
}
.__react_component_tooltip.place-left::before {
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  right: -8px;
  top: 50%;
  margin-top: -5px;
}
.__react_component_tooltip.place-right::before {
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  left: -8px;
  top: 50%;
  margin-top: -5px;
}
.__react_component_tooltip .multi-line {
  display: block;
  padding: 2px 0;
  text-align: center;
}</style></head><body style="background:#111827"><noscript>You need to enable JavaScript to run this app.</noscript><div id="root"><div class="Toastify"></div><div class="h-screen overflow-hidden bg-gray-900 flex darkStyle"><nav aria-label="Sidebar" class="hidden md:flex flex-col md:flex-shrink-0 md:bg-gray-800"><div class="__react_component_tooltip te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787 place-top type-dark" id="sidebar" data-id="tooltip"><style>
  	.te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-top {
        margin-top: -10px;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-top::before {
        border-top: 8px solid transparent;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-bottom {
        margin-top: 10px;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-left {
        margin-left: -10px;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-left::before {
        border-left: 8px solid transparent;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-right {
        margin-left: 10px;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-right::before {
        border-right: 8px solid transparent;
    }
    .te62f8aa5-d4a4-4db5-b1ab-31ca7c9a7787.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="absolute inset-y-0 left-0 md:static md:flex-shrink-0"><a class="flex items-center justify-center h-20 w-20 bg-cyan-500 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-cyan-600 md:w-20" href="/search/"><img class="h-10 w-auto" src="/images/branding-logo-head-gray.png" alt="GummySearch logo"></a></div><div class="relative w-20 flex flex-col p-3 py-4 space-y-3 flex-grow"><a data-for="sidebar" data-tip="Audiences" class="flex-shrink-0 inline-flex items-center justify-center h-14 w-14 rounded-lg bg-gray-900 text-white" href="/audiences/" currentitem="false"><span class="sr-only">Audiences</span><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path></svg></a><a data-for="sidebar" data-tip="Advanced Search" class="flex-shrink-0 inline-flex items-center justify-center h-14 w-14 rounded-lg text-gray-400 hover:bg-gray-700" href="/search/" currentitem="false"><span class="sr-only">Search</span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"></path></svg></a><a data-for="sidebar" data-tip="Conversations" class="flex-shrink-0 inline-flex relative items-center justify-center h-14 w-14 rounded-lg text-gray-400 hover:bg-gray-700" href="/conversations/" currentitem="false"><span class="sr-only">Conversatons</span><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"></path></svg></a></div><div class="relative w-20 flex flex-col p-3 space-y-3"><div class="relative"><div class="__react_component_tooltip t517c9bf0-64c4-4d2b-94f1-c9650096ab01 place-top type-dark" id="launch-guide" data-id="tooltip"><style>
  	.t517c9bf0-64c4-4d2b-94f1-c9650096ab01 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-top {
        margin-top: -10px;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-top::before {
        border-top: 8px solid transparent;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-bottom {
        margin-top: 10px;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-left {
        margin-left: -10px;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-left::before {
        border-left: 8px solid transparent;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-right {
        margin-left: 10px;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-right::before {
        border-right: 8px solid transparent;
    }
    .t517c9bf0-64c4-4d2b-94f1-c9650096ab01.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><button data-for="launch-guide" data-tip="Launch Guide" class="relative flex-shrink-0 inline-flex items-center justify-center h-14 w-14 focus:outline-none focus:ring-transparent focus:border-none rounded-lg text-gray-400 hover:bg-gray-700" id="headlessui-popover-button-4" type="button" aria-expanded="false" currentitem="false"><span class="sr-only">Launch Guide</span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-6 w-6"><path stroke-linecap="round" stroke-linejoin="round" d="M15.59 14.37a6 6 0 0 1-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 0 0 6.16-12.12A14.98 14.98 0 0 0 9.631 8.41m5.96 5.96a14.926 14.926 0 0 1-5.841 2.58m-.119-8.54a6 6 0 0 0-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 0 0-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 0 1-2.448-2.448 14.9 14.9 0 0 1 .06-.312m-2.24 2.39a4.493 4.493 0 0 0-1.757 4.306 4.493 4.493 0 0 0 4.306-1.758M16.5 9a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"></path></svg><div class="absolute"><svg height="40" width="40" style="opacity: 1;"><circle stroke="rgb(52, 211, 153)" fill="transparent" stroke-dasharray="113.09733552923255 113.09733552923255" stroke-width="2" r="18" cx="20" cy="20" style="stroke-dashoffset: 97.2637;"></circle></svg></div></button></div><a data-for="sidebar" data-tip="Help" class="flex-shrink-0 inline-flex items-center justify-center h-14 w-14 rounded-lg text-gray-400 hover:bg-gray-700" href="/help/" currentitem="false"><span class="sr-only">Help</span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-6 w-6" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></a><a data-for="sidebar" data-tip="Account" class="flex-shrink-0 inline-flex items-center justify-center h-14 w-14 rounded-lg text-gray-400 hover:bg-gray-700" href="/account/" currentitem="false"><span class="sr-only">Account</span><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A13.937 13.937 0 0112 16c2.5 0 4.847.655 6.879 1.804M15 10a3 3 0 11-6 0 3 3 0 016 0zm6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg></a><div class="relative"><button class="flex-shrink-0 inline-flex items-center justify-center h-14 w-14 focus:outline-none focus:ring-transparent focus:border-none rounded-lg text-gray-400 hover:bg-gray-700" id="headlessui-popover-button-2" type="button" aria-expanded="false"><span class="sr-only">More</span><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h.01M12 12h.01M19 12h.01M6 12a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0zm7 0a1 1 0 11-2 0 1 1 0 012 0z"></path></svg></button></div></div></nav><main id="main" class="min-w-0 min-h-0 flex-1 flex flex-col overflow-auto text-white h-screen"><div class="flex-grow relative flex flex-col p-4 sm:p-8"><div><div class="flex items-center sm:-mt-3 pb-2"><div class="flex-1 min-w-0"><h2 class="text-2xl font-bold leading-7 text-white sm:text-3xl sm:truncate">Audiences</h2></div><div class="ml-auto flex lg:mt-0"><a type="button" class="appearance-none inline-flex items-center px-4 py-2 border border-solid border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gray-700 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-cyan-500" href="/audiences/info/"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="-ml-1 mr-2 h-5 w-5" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>Info</a><a type="button" class="appearance-none ml-3 inline-flex items-center px-4 py-2 border border-solid border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-cyan-500 hover:bg-cyan-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-cyan-500" href="/audiences/new/"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="-ml-1 mr-2 h-5 w-5" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>New</a></div></div><div class="border-b border-solid border-gray-800"><nav class="-mb-px flex space-x-2 sm:space-x-4 max-w-full overflow-x-auto no-scrollbar" x-descriptions="Tab component"><a class="whitespace-nowrap py-2 pb-4 px-2 flex items-center border-solid border-b-2 font-medium focus:outline-none focus:ring-none text-sm border-transparent text-gray-400 hover:text-gray-300 hover:border-gray-300 " href="/audiences/"><span>Saved</span></a><a class="whitespace-nowrap py-2 pb-4 px-2 flex items-center border-solid border-b-2 font-medium focus:outline-none focus:ring-none text-sm border-white text-white " href="/audiences/curated/"><span>Curated</span></a><a class="whitespace-nowrap py-2 pb-4 px-2 flex items-center border-solid border-b-2 font-medium focus:outline-none focus:ring-none text-sm border-transparent text-gray-400 hover:text-gray-300 hover:border-gray-300 " href="/audiences/trending/"><span>Trending</span></a></nav></div><div class="pt-8"><div><div class="mb-2 flex-wrap"><h2 class="text-lg font-medium flex items-center flex-wrap"><span>Curated Audiences</span></h2></div><div class=""><div class="grid grid-cols-1 md:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-6 sm:grid-cols-3 opacity-100 translate-y-0"><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Pet Lovers</h2><div class="__react_component_tooltip t1d7397bb-1604-4fa3-b5f6-61b69a034144 place-top type-dark" id="audience-card-4c0463bfad" data-id="tooltip"><style>
  	.t1d7397bb-1604-4fa3-b5f6-61b69a034144 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-top {
        margin-top: -10px;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-top::before {
        border-top: 8px solid transparent;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-bottom {
        margin-top: 10px;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-left {
        margin-left: -10px;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-left::before {
        border-left: 8px solid transparent;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-right {
        margin-left: 10px;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-right::before {
        border-right: 8px solid transparent;
    }
    .t1d7397bb-1604-4fa3-b5f6-61b69a034144.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><span class="font-normal" data-for="audience-card-4c0463bfad" data-tip="You have already saved this curated audience" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-4c0463bfad" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>31 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>20.5M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.75% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t24bc3fa9-1ce3-4536-ba1a-f19e45105e24 show place-top type-custom w-60 text-center" id="collection-4c0463bfad-icon" data-id="tooltip" style="left: 56px; top: 185px;"><style>
  	.t24bc3fa9-1ce3-4536-ba1a-f19e45105e24 {
	    color: black;
	    background: white;
	    border: 1px solid transparent;
  	}

  	.t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-top {
        margin-top: -10px;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-top::before {
        border-top: 8px solid transparent;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: white;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-bottom {
        margin-top: 10px;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: white;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-left {
        margin-left: -10px;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-left::before {
        border-left: 8px solid transparent;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: white;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-right {
        margin-left: 10px;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-right::before {
        border-right: 8px solid transparent;
    }
    .t24bc3fa9-1ce3-4536-ba1a-f19e45105e24.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: white;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style>r/herpetology</div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-4c0463bfad-icon" data-tip="r/dogbreed, r/DogBreeds101, r/Dogowners, r/DogTrainingTips, r/doggrooming, r/lookatmydog, r/reptiles, r/germanshepherds, r/Pets, r/CatAdvice, r/cat, r/Ornithology, r/puppy101, r/DOG, r/birding, r/BeardedDragons, r/RATS, r/dogswithjobs, r/dogpictures, r/parrots, r/Aquariums, r/Dogtraining, r/dogs, r/cats" currentitem="false">+24</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/PetAdvice" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tjao/styles/communityIcon_0hdy74lcndjd1.png?width=256&amp;s=b11a01d637062e17c94f668e16b079699108d844" alt="PetAdvice"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/cockatiel" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2uqu9/styles/communityIcon_9p15b1k9zw551.jpg?width=256&amp;s=c24dd0811a88a00eb2a515526ebcac227e9d4aa5" alt="cockatiel"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/turtle" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2svlx/styles/communityIcon_1ff99du8zq891.png?width=256&amp;s=3992da7a00704895165f6a3798d86d18a8748fdd" alt="turtle"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/leopardgeckos" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2slot/styles/communityIcon_yuep9bjj34ya1.png?width=256&amp;s=935edbdc38c78feb506fde4cd73945eef49f3b27" alt="leopardgeckos"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/ballpython" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2srho/styles/communityIcon_iprkwgdy985b1.jpg?width=256&amp;s=4901f54733b3e3f140b828bdc31c122ed8e0ad9e" alt="ballpython"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/herpetology" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2re9t/styles/communityIcon_hxt82sxbl8cc1.png?width=256&amp;s=a90b29d5f3484d261e82f8bd9a71f5ec48431ec4" alt="herpetology"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4c0463bfad-icon" data-tip="r/DogAdvice" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_367ex/styles/communityIcon_hzmr0tbew45a1.jpg?width=256&amp;s=130d2c817ee3447319d2de44061e61f13bd832e1" alt="DogAdvice"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Software Developers</h2><div class="__react_component_tooltip t47925bb6-3fd5-43ee-bc0d-5bffe40ee105 place-top type-dark" id="audience-card-dbf5157d8f" data-id="tooltip"><style>
  	.t47925bb6-3fd5-43ee-bc0d-5bffe40ee105 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-top {
        margin-top: -10px;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-top::before {
        border-top: 8px solid transparent;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-bottom {
        margin-top: 10px;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-left {
        margin-left: -10px;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-left::before {
        border-left: 8px solid transparent;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-right {
        margin-left: 10px;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-right::before {
        border-right: 8px solid transparent;
    }
    .t47925bb6-3fd5-43ee-bc0d-5bffe40ee105.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-dbf5157d8f" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>26 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>27.1M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.91% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t03835d09-9b00-4845-9eda-a3b48689c849 place-top type-custom w-60 text-center" id="collection-dbf5157d8f-icon" data-id="tooltip" style="left: 511px; top: 185px;"><style>
  	.t03835d09-9b00-4845-9eda-a3b48689c849 {
	    color: black;
	    background: white;
	    border: 1px solid transparent;
  	}

  	.t03835d09-9b00-4845-9eda-a3b48689c849.place-top {
        margin-top: -10px;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-top::before {
        border-top: 8px solid transparent;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: white;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t03835d09-9b00-4845-9eda-a3b48689c849.place-bottom {
        margin-top: 10px;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: white;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t03835d09-9b00-4845-9eda-a3b48689c849.place-left {
        margin-left: -10px;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-left::before {
        border-left: 8px solid transparent;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: white;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t03835d09-9b00-4845-9eda-a3b48689c849.place-right {
        margin-left: 10px;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-right::before {
        border-right: 8px solid transparent;
    }
    .t03835d09-9b00-4845-9eda-a3b48689c849.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: white;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style>r/iOSProgramming</div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-dbf5157d8f-icon" data-tip="r/Development, r/coolgithubprojects, r/softwaredevelopment, r/SoftwareEngineering, r/csharp, r/rust, r/devops, r/computerscience, r/reactjs, r/coding, r/learnpython, r/Python, r/linux, r/cscareerquestions, r/AskEngineers, r/javascript, r/webdev, r/learnprogramming, r/programming" currentitem="false">+19</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/elixir" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vhb3/styles/communityIcon_5ycr3zsnriea1.jpg?width=256&amp;s=e4b87f31c6f456cd514d7200338251c63a6e41db" alt="elixir"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/AskComputerScience" currentitem="false"><img class="h-full w-full rounded-sm" src="https://b.thumbs.redditmedia.com/m0_B7gzednCG7Uwqwub_mYYMsZNgxbUbHzWb9JTE1dM.png" alt="AskComputerScience"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/reactnative" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_37k5y/styles/communityIcon_e9xvw609p7r21.png?width=256&amp;s=c99f815fefd71859bc0149534586c32366a7ab36" alt="reactnative"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/iOSProgramming" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2s61a/styles/communityIcon_qu38ws3ubg9d1.png?width=256&amp;s=7bcdddade8412e3b2b1d280422fd068b0692d1de" alt="iOSProgramming"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/ExperiencedDevs" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_e0gez/styles/communityIcon_vnwju3cb5ei41.jpg?width=256&amp;s=2e361c65409bd546957c0e2c25f93be537e5b617" alt="ExperiencedDevs"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/software" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qh19/styles/communityIcon_2tdndgpyiiw51.jpg?width=256&amp;s=c51f7330da492f93787ee4129e5f42347f186260" alt="software"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-dbf5157d8f-icon" data-tip="r/learnjavascript" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tugi/styles/communityIcon_7yzrvmem0wi31.png?width=256&amp;s=d0110712c83415e5309f985c6d7dc19086f7d79d" alt="learnjavascript"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">DevOps</h2><div class="__react_component_tooltip t71d3b9d3-7297-4813-861a-a960afbe6983 place-top type-dark" id="audience-card-25f2512068" data-id="tooltip"><style>
  	.t71d3b9d3-7297-4813-861a-a960afbe6983 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t71d3b9d3-7297-4813-861a-a960afbe6983.place-top {
        margin-top: -10px;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-top::before {
        border-top: 8px solid transparent;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-bottom {
        margin-top: 10px;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-left {
        margin-left: -10px;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-left::before {
        border-left: 8px solid transparent;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-right {
        margin-left: 10px;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-right::before {
        border-right: 8px solid transparent;
    }
    .t71d3b9d3-7297-4813-861a-a960afbe6983.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-25f2512068" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>21 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>1.3M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.28% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t367cda27-ccca-43d2-8ea5-e7a64e735344 place-top type-dark" id="collection-25f2512068-icon" data-id="tooltip"><style>
  	.t367cda27-ccca-43d2-8ea5-e7a64e735344 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t367cda27-ccca-43d2-8ea5-e7a64e735344.place-top {
        margin-top: -10px;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-top::before {
        border-top: 8px solid transparent;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-bottom {
        margin-top: 10px;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-left {
        margin-left: -10px;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-left::before {
        border-left: 8px solid transparent;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-right {
        margin-left: 10px;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-right::before {
        border-right: 8px solid transparent;
    }
    .t367cda27-ccca-43d2-8ea5-e7a64e735344.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-25f2512068-icon" data-tip="r/DevOpsSec, r/ExperiencedDevOps, r/AWS_cloud, r/devopsjobs, r/Cloud, r/cloudcomputing, r/sre, r/computing, r/Terraform, r/googlecloud, r/AZURE, r/ExperiencedDevs, r/aws, r/devops" currentitem="false">+14</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/PlatformEngineers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_433re1/styles/communityIcon_xk1npgiq2dob1.png?width=256&amp;s=1958d15bb4607d04bd645df28972b757ceecdc37" alt="PlatformEngineers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/aws_cdk" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_28vuhu/styles/communityIcon_clokr4nws8041.png?width=256&amp;s=4af855b7ca9b66626274324d84d72e0723b43dd2" alt="aws_cdk"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/platformengineering" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_5x8v97/styles/communityIcon_y68mslqctvba1.png?width=256&amp;s=47849e509922363cd6b4ac9f98465a103937fed4" alt="platformengineering"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/DevOpsLinks" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3f9jf/styles/communityIcon_wuqiedz3326a1.png?width=256&amp;s=e39bd9803e4a159d74428cb9ea240f5da1917be2" alt="DevOpsLinks"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/Docker_DevOps" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_364pbd/styles/communityIcon_i6968q3kpcp51.PNG?width=256&amp;s=c377d55837d6b4cbd6ecd84df3bae3cd0c323dfe" alt="Docker_DevOps"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/AWS_Certified_Experts" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3ilga/styles/communityIcon_rk97ua0wvsw21.png?width=256&amp;s=f3ac99e6e2a69fab64a9e589828a80ae2af4d567" alt="AWS_Certified_Experts"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-25f2512068-icon" data-tip="r/azuredevops" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_oe4la/styles/communityIcon_lc1sg4wc73t21.jpg?width=256&amp;s=dd83df136006b5e8d0fbdedb00696291f4b71e9a" alt="azuredevops"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Crypto</h2><div class="__react_component_tooltip t6cc87f07-7a46-44c3-9f3a-edebdd8c379e place-top type-dark" id="audience-card-49d2261f12" data-id="tooltip"><style>
  	.t6cc87f07-7a46-44c3-9f3a-edebdd8c379e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-top {
        margin-top: -10px;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-bottom {
        margin-top: 10px;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-left {
        margin-left: -10px;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-right {
        margin-left: 10px;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6cc87f07-7a46-44c3-9f3a-edebdd8c379e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-49d2261f12" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>19 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>17.3M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.07% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435 place-top type-dark" id="collection-49d2261f12-icon" data-id="tooltip"><style>
  	.t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-top {
        margin-top: -10px;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-top::before {
        border-top: 8px solid transparent;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-bottom {
        margin-top: 10px;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-left {
        margin-left: -10px;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-left::before {
        border-left: 8px solid transparent;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-right {
        margin-left: 10px;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-right::before {
        border-right: 8px solid transparent;
    }
    .t39d1bfda-a2d2-489a-ab30-7e3d9dcb1435.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-49d2261f12-icon" data-tip="r/ethfinance, r/ethdev, r/defi, r/CryptoCurrencyTrading, r/solana, r/Crypto_Currency_News, r/CryptoCurrencies, r/BitcoinBeginners, r/CryptoMarkets, r/ethtrader, r/ethereum, r/Bitcoin" currentitem="false">+12</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/defi_" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_46rd1t/styles/communityIcon_jb36y9tywfq61.png?width=256&amp;s=92db6b99116ff11dd38d3cc7269cf5618af0bd28" alt="defi_"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/CryptoNews" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_30nfb/styles/communityIcon_r85474la4wr91.png?width=256&amp;s=3a8a1c637a4c5b80d495241f324d169159104595" alt="CryptoNews"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/defiblockchain" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2p8jo9/styles/communityIcon_y3nspl9gbik51.png?width=256&amp;s=46ebbc934d00e59205cb6759da0b98beee0cef6e" alt="defiblockchain"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/web3" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qy9b/styles/communityIcon_lwhzovecgv1c1.png?width=256&amp;s=225808b10f9095af2b3b700e93f399ac04a26220" alt="web3"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/ethstaker" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3b6pl/styles/communityIcon_chp7v5j1jt1b1.jpg?width=256&amp;s=69e14f68cd4bf98e486f5ab2f41610d884eb49b6" alt="ethstaker"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/0xPolygon" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qgijx/styles/communityIcon_0gpn7je434za1.jpg?width=256&amp;s=9517816fdf8721c66f416943ff9a422d5c856257" alt="0xPolygon"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-49d2261f12-icon" data-tip="r/Crypto_General" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2xgpi/styles/communityIcon_ezf2xqvasm6d1.png?width=256&amp;s=82fd108604783fffc11ec5908a91fb7b579c8a24" alt="Crypto_General"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Marketers</h2><div class="__react_component_tooltip t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87 place-top type-dark" id="audience-card-e8e85097b3" data-id="tooltip"><style>
  	.t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-top {
        margin-top: -10px;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-top::before {
        border-top: 8px solid transparent;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-bottom {
        margin-top: 10px;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-left {
        margin-left: -10px;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-left::before {
        border-left: 8px solid transparent;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-right {
        margin-left: 10px;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-right::before {
        border-right: 8px solid transparent;
    }
    .t965fc16c-2d4c-47f2-a9f1-ad0ee891ab87.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-e8e85097b3" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>18 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>5.0M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>5.39% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t73c756cd-940a-4362-ba6f-30ca72dbe2bf place-top type-dark" id="collection-e8e85097b3-icon" data-id="tooltip"><style>
  	.t73c756cd-940a-4362-ba6f-30ca72dbe2bf {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-top {
        margin-top: -10px;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-top::before {
        border-top: 8px solid transparent;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-bottom {
        margin-top: 10px;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-left {
        margin-left: -10px;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-left::before {
        border-left: 8px solid transparent;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-right {
        margin-left: 10px;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-right::before {
        border-right: 8px solid transparent;
    }
    .t73c756cd-940a-4362-ba6f-30ca72dbe2bf.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-e8e85097b3-icon" data-tip="r/affiliate_marketing, r/content_marketing, r/InstagramMarketing, r/PPC, r/advertising, r/DigitalMarketing, r/Affiliatemarketing, r/digital_marketing, r/SEO, r/marketing, r/socialmedia" currentitem="false">+11</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/OnlineMarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qstp/styles/communityIcon_5fnvt3ilpbwb1.png?width=256&amp;s=c470c86ffddb31eb22c2c5b2fcb6773083c09e32" alt="OnlineMarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/MarketingResearch" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2xlmf/styles/communityIcon_aqplgabnfep31.jpg?width=256&amp;s=e812b50f44d38494e357b6e3d9d57bc4a950f158" alt="MarketingResearch"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/googleads" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rge2/styles/communityIcon_fz8ine75s1691.jpg?width=256&amp;s=fae821351de3e4f2e8b50c3dc95c9b0ffb07a133" alt="googleads"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/Emailmarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r1yx/styles/communityIcon_k1li29utju8a1.png?width=256&amp;s=492b3bde8bd185ea9a377390a01e81d6de9d1f25" alt="Emailmarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/AskMarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vqfw/styles/communityIcon_v31urp88x5pd1.png?width=256&amp;s=018ada57acca0f77195e0cb0d06ca06629dd98dc" alt="AskMarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/FacebookAds" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2yoxx/styles/communityIcon_2svbmovwqke71.png?width=256&amp;s=85abf0687654cb000d5ed8b9cd3738748aa2a691" alt="FacebookAds"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e8e85097b3-icon" data-tip="r/bigseo" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wjav/styles/communityIcon_a0kac7rnkdi71.png?width=256&amp;s=a2a0bf7d35aaebbb0a86ccad04352e03b1f553c4" alt="bigseo"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Startup Founders</h2><div class="__react_component_tooltip t7c418ef0-1479-406a-ba52-c8180f0199e6 place-top type-dark" id="audience-card-9c93affcdc" data-id="tooltip"><style>
  	.t7c418ef0-1479-406a-ba52-c8180f0199e6 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t7c418ef0-1479-406a-ba52-c8180f0199e6.place-top {
        margin-top: -10px;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-top::before {
        border-top: 8px solid transparent;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-bottom {
        margin-top: 10px;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-left {
        margin-left: -10px;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-left::before {
        border-left: 8px solid transparent;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-right {
        margin-left: 10px;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-right::before {
        border-right: 8px solid transparent;
    }
    .t7c418ef0-1479-406a-ba52-c8180f0199e6.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-9c93affcdc" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>16 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>11.4M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.17% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t6c78adea-bb70-4220-b683-c403d4478b39 place-top type-custom w-60 text-center" id="collection-9c93affcdc-icon" data-id="tooltip" style="left: 427px; top: 329px;"><style>
  	.t6c78adea-bb70-4220-b683-c403d4478b39 {
	    color: black;
	    background: white;
	    border: 1px solid transparent;
  	}

  	.t6c78adea-bb70-4220-b683-c403d4478b39.place-top {
        margin-top: -10px;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: white;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6c78adea-bb70-4220-b683-c403d4478b39.place-bottom {
        margin-top: 10px;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: white;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6c78adea-bb70-4220-b683-c403d4478b39.place-left {
        margin-left: -10px;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: white;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6c78adea-bb70-4220-b683-c403d4478b39.place-right {
        margin-left: 10px;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6c78adea-bb70-4220-b683-c403d4478b39.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: white;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style>r/EntrepreneurRideAlong</div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-9c93affcdc-icon" data-tip="r/startup_resources, r/indiebiz, r/Entrepreneurs, r/advancedentrepreneur, r/SideProject, r/startups, r/smallbusiness, r/business, r/Entrepreneur" currentitem="false">+9</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/indiehackers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3gjm0/styles/communityIcon_l6l5fyl07eud1.png?width=256&amp;s=c48aa5ae40d197651d74c22ca9e8da20a995f52a" alt="indiehackers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/growmybusiness" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ykna/styles/communityIcon_3dfg1sh7xs061.png?width=256&amp;s=4321f69bcf061fcca37e0371c4af750074222c40" alt="growmybusiness"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/ycombinator" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sfff/styles/communityIcon_a5yupf4kf9ba1.png?width=256&amp;s=93459d0172790e59b0ddcbe78541464d0d6dfac5" alt="ycombinator"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/Entrepreneurship" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhww/styles/communityIcon_62isd4lv0cx41.png?width=256&amp;s=eecb4c37d0ce013184e74a3cc1000e6e4b5972ea" alt="Entrepreneurship"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/startup" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhyd/styles/communityIcon_1rgkkxz718ac1.png?width=256&amp;s=6c06cd831a6d135075201a41e474b12e02cd5185" alt="startup"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/SaaS" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qkq6/styles/communityIcon_u7ddkuay2xn21.jpg?width=256&amp;s=9054f6d63f23825552de4bd6f31328716775e412" alt="SaaS"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-9c93affcdc-icon" data-tip="r/EntrepreneurRideAlong" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2twzl/styles/communityIcon_t2a0ic3xi6md1.png?width=256&amp;s=eb3b817447f5bff6b036d43aa6a2aa1fd51575da" alt="EntrepreneurRideAlong"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Stock Investors</h2><div class="__react_component_tooltip t2fd8d60f-8621-4911-a663-f04435bc1f7e place-top type-dark" id="audience-card-19669fb480" data-id="tooltip"><style>
  	.t2fd8d60f-8621-4911-a663-f04435bc1f7e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-top {
        margin-top: -10px;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-top::before {
        border-top: 8px solid transparent;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-bottom {
        margin-top: 10px;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-left {
        margin-left: -10px;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-left::before {
        border-left: 8px solid transparent;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-right {
        margin-left: 10px;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-right::before {
        border-right: 8px solid transparent;
    }
    .t2fd8d60f-8621-4911-a663-f04435bc1f7e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-19669fb480" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>15 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>24.1M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.21% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t062e6866-006f-4fb8-9868-070272cabc43 place-top type-dark" id="collection-19669fb480-icon" data-id="tooltip"><style>
  	.t062e6866-006f-4fb8-9868-070272cabc43 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t062e6866-006f-4fb8-9868-070272cabc43.place-top {
        margin-top: -10px;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-top::before {
        border-top: 8px solid transparent;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t062e6866-006f-4fb8-9868-070272cabc43.place-bottom {
        margin-top: 10px;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t062e6866-006f-4fb8-9868-070272cabc43.place-left {
        margin-left: -10px;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-left::before {
        border-left: 8px solid transparent;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t062e6866-006f-4fb8-9868-070272cabc43.place-right {
        margin-left: 10px;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-right::before {
        border-right: 8px solid transparent;
    }
    .t062e6866-006f-4fb8-9868-070272cabc43.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-19669fb480-icon" data-tip="r/SecurityAnalysis, r/options, r/FinancialCareers, r/finance, r/investing, r/StockMarket, r/Daytrading, r/stocks" currentitem="false">+8</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/technicalanalysis" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2shyk/styles/communityIcon_hh9mqmgljv871.png?width=256&amp;s=ca4b5d90a4c528f8efe39a2ec6dab11c94e1d93b" alt="technicalanalysis"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/swingtrading" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_35vb2/styles/communityIcon_p38z4b87z19c1.jpg?width=256&amp;s=f326ae989f97c205ff2532ec4a624c9075d61152" alt="swingtrading"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/StocksAndTrading" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wwow/styles/communityIcon_zucr5ozavon81.png?width=256&amp;s=ca3eda5cb526823bfdc179536bf6f31f88487d3c" alt="StocksAndTrading"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/Trading" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qldr/styles/communityIcon_iaphdyh2zei61.png?width=256&amp;s=11f14b250ca0a06238eff68e959c1ecc1fed3d4d" alt="Trading"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/ValueInvesting" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rndg/styles/communityIcon_tti8k7ixulj81.jpeg?width=256&amp;s=b72bb206b0e6206f1157f652d431c87eccf68fcb" alt="ValueInvesting"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/Forex" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhmq/styles/communityIcon_8bmoph38dvwb1.png?width=256&amp;s=96ddc035714fc41f0b4f4ac615829c34538aa25c" alt="Forex"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-19669fb480-icon" data-tip="r/dividends" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qsbv/styles/communityIcon_h9shb863y8061.png?width=256&amp;s=48ba31b9b705a31bfdcb2e543128fd1741ac74ef" alt="dividends"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Video Editors</h2><div class="__react_component_tooltip t60c7abb1-0a4d-4041-948a-9ea3ad165bd3 place-top type-dark" id="audience-card-3550affaca" data-id="tooltip"><style>
  	.t60c7abb1-0a4d-4041-948a-9ea3ad165bd3 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-top {
        margin-top: -10px;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-top::before {
        border-top: 8px solid transparent;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-bottom {
        margin-top: 10px;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-left {
        margin-left: -10px;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-left::before {
        border-left: 8px solid transparent;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-right {
        margin-left: 10px;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-right::before {
        border-right: 8px solid transparent;
    }
    .t60c7abb1-0a4d-4041-948a-9ea3ad165bd3.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-3550affaca" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>15 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>1.9M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.67% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t4c2708ca-ad28-42a7-b96c-f716deb5ed4b place-top type-dark" id="collection-3550affaca-icon" data-id="tooltip"><style>
  	.t4c2708ca-ad28-42a7-b96c-f716deb5ed4b {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-top {
        margin-top: -10px;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-top::before {
        border-top: 8px solid transparent;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-bottom {
        margin-top: 10px;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-left {
        margin-left: -10px;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-left::before {
        border-left: 8px solid transparent;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-right {
        margin-left: 10px;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-right::before {
        border-right: 8px solid transparent;
    }
    .t4c2708ca-ad28-42a7-b96c-f716deb5ed4b.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-3550affaca-icon" data-tip="r/videomaker, r/Youtubevideo, r/buildapcvideoediting, r/iMovie, r/editing, r/finalcutpro, r/youtubers, r/NewTubers" currentitem="false">+8</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/postproduction" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rp6w/styles/communityIcon_qfs4k5su9f3c1.png?width=256&amp;s=c713b842b2ae5bbd798e72ae29bf153358b127e1" alt="postproduction"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/VideoEditors" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_38zd8/styles/communityIcon_xqh9cnx7a8b51.png?width=256&amp;s=30ca864effbbdb15a075a27f727e2480d8af908f" alt="VideoEditors"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/editors" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qpkc/styles/communityIcon_ezpiwt2512m11.png?width=256&amp;s=ce8328aaa24057b6858dc3ffbab88d7cd3f79179" alt="editors"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/premiere" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vddz/styles/communityIcon_rf8rndnq6h851.png?width=256&amp;s=0b5677be868700e3899e7e7784e167a7753e6883" alt="premiere"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/gopro" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rvat/styles/communityIcon_eczx5tmdbio11.png?width=256&amp;s=987e5c055b12f8cda5d26b779006cdcfbc7fcb1a" alt="gopro"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/videography" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qwgz/styles/communityIcon_ai25di8tmqd21.png?width=256&amp;s=a6b86f890a7c1888edcb73848826ddff8c975bd6" alt="videography"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3550affaca-icon" data-tip="r/VideoEditing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ri0h/styles/communityIcon_fqy1rqv5p2m11.png?width=256&amp;s=9aa920417b383586bb971b15a5be348292086a5a" alt="VideoEditing"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Generative AI</h2><div class="__react_component_tooltip tdf751c44-65fc-4c63-92c0-5d8645a06d18 place-top type-dark" id="audience-card-617a323a6d" data-id="tooltip"><style>
  	.tdf751c44-65fc-4c63-92c0-5d8645a06d18 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-top {
        margin-top: -10px;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-top::before {
        border-top: 8px solid transparent;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-bottom {
        margin-top: 10px;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-left {
        margin-left: -10px;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-left::before {
        border-left: 8px solid transparent;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-right {
        margin-left: 10px;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-right::before {
        border-right: 8px solid transparent;
    }
    .tdf751c44-65fc-4c63-92c0-5d8645a06d18.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-617a323a6d" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>15 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>14.2M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>6.12% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip te6b8967a-14a1-4517-bd49-d318420acca9 place-top type-dark" id="collection-617a323a6d-icon" data-id="tooltip"><style>
  	.te6b8967a-14a1-4517-bd49-d318420acca9 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.te6b8967a-14a1-4517-bd49-d318420acca9.place-top {
        margin-top: -10px;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-top::before {
        border-top: 8px solid transparent;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .te6b8967a-14a1-4517-bd49-d318420acca9.place-bottom {
        margin-top: 10px;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .te6b8967a-14a1-4517-bd49-d318420acca9.place-left {
        margin-left: -10px;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-left::before {
        border-left: 8px solid transparent;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .te6b8967a-14a1-4517-bd49-d318420acca9.place-right {
        margin-left: 10px;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-right::before {
        border-right: 8px solid transparent;
    }
    .te6b8967a-14a1-4517-bd49-d318420acca9.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-617a323a6d-icon" data-tip="r/PromptEngineering, r/LanguageTechnology, r/StableDiffusion, r/weirddalle, r/GPT3, r/midjourney, r/OpenAI, r/ChatGPT" currentitem="false">+8</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/DreamBooth" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_6xvul5/styles/communityIcon_hn09p1pxj2q91.png?width=256&amp;s=9e93b4051f798f91b92d4a5d03dab64d6541cebd" alt="DreamBooth"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/starryai" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_55d4g3/styles/communityIcon_gvlonzfkhqjb1.png?width=256&amp;s=b9965635d4a7f16ceb80df8838a38e5d64d2bd9d" alt="starryai"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/nightcafe" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_54v4b3/styles/communityIcon_8hf16js5bor71.png?width=256&amp;s=42098b586674db7e0f4d29510e7c06af9e4ff7e4" alt="nightcafe"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/sdforall" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_76l9xa/styles/communityIcon_t9spijgkbot91.png?width=256&amp;s=c10ad716316da9e3981b0de1b66e06b89e4e4726" alt="sdforall"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/deepdream" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_38wmv/styles/communityIcon_bbdfh656tyy31.jpg?width=256&amp;s=c249cf80a3817276a3c3e4cd766831412694215d" alt="deepdream"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/dalle2" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_66jnlu/styles/communityIcon_9atutqbch0z81.png?width=256&amp;s=9e04005acb8e2ff54911658846a8fc135baf9402" alt="dalle2"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-617a323a6d-icon" data-tip="r/aiArt" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3j874/styles/communityIcon_eu4kh15k5ald1.png?width=256&amp;s=fbb99de0afc5c4b73a3376d968f9582f730772a6" alt="aiArt"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Designers</h2><div class="__react_component_tooltip t15980248-8500-4707-bb00-1d4771e69086 place-top type-dark" id="audience-card-c6ffc48830" data-id="tooltip"><style>
  	.t15980248-8500-4707-bb00-1d4771e69086 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t15980248-8500-4707-bb00-1d4771e69086.place-top {
        margin-top: -10px;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-top::before {
        border-top: 8px solid transparent;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t15980248-8500-4707-bb00-1d4771e69086.place-bottom {
        margin-top: 10px;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t15980248-8500-4707-bb00-1d4771e69086.place-left {
        margin-left: -10px;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-left::before {
        border-left: 8px solid transparent;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t15980248-8500-4707-bb00-1d4771e69086.place-right {
        margin-left: 10px;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-right::before {
        border-right: 8px solid transparent;
    }
    .t15980248-8500-4707-bb00-1d4771e69086.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-c6ffc48830" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>13 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>8.5M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.83% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t76a0d3d8-7b7d-4926-9b84-c58a2f31e027 place-top type-dark" id="collection-c6ffc48830-icon" data-id="tooltip"><style>
  	.t76a0d3d8-7b7d-4926-9b84-c58a2f31e027 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-top {
        margin-top: -10px;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-top::before {
        border-top: 8px solid transparent;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-bottom {
        margin-top: 10px;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-left {
        margin-left: -10px;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-left::before {
        border-left: 8px solid transparent;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-right {
        margin-left: 10px;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-right::before {
        border-right: 8px solid transparent;
    }
    .t76a0d3d8-7b7d-4926-9b84-c58a2f31e027.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-c6ffc48830-icon" data-tip="r/uidesign, r/product_design, r/UXResearch, r/web_design, r/graphic_design, r/Design" currentitem="false">+6</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/UX_Design" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2shhn/styles/communityIcon_ldny560phjaa1.png?width=256&amp;s=0de026ffe6ae564090ceba9337a6b1fcd97bffb6" alt="UX_Design"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/learndesign" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2yo7l/styles/communityIcon_quzu9rqeaim61.png?width=256&amp;s=ee8799608f5361791f93821c4e3436f6fa5b351b" alt="learndesign"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/userexperience" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qj2z/styles/communityIcon_hbh12wyi2cj21.png?width=256&amp;s=5ad5f61bacf92a1027b7aaa508fcaa3a08a7a745" alt="userexperience"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/UXDesign" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2u66g/styles/communityIcon_gjdxwtiuqt691.jpeg?width=256&amp;s=3130f695575513929aa12a6ff7831d517a075faa" alt="UXDesign"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/UI_Design" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vqtk/styles/communityIcon_scg1gbyqkkn81.png?width=256&amp;s=9fc9ffe8bf05daf2c220cd97f57a04ecdc8094db" alt="UI_Design"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/logodesign" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2s4v6/styles/communityIcon_5bm7k02yw1ma1.jpg?width=256&amp;s=ec872b56f17e16fdb96f484d1bbf6c3fd636bda9" alt="logodesign"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-c6ffc48830-icon" data-tip="r/typography" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhx0/styles/communityIcon_ltnrbv1nlgh91.png?width=256&amp;s=1eecfa3d9dd05c2cd9e425403a383c46cb531c97" alt="typography"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Data Scientists</h2><div class="__react_component_tooltip tce1affd6-d7c5-4d9c-8067-6ba03e1b5890 place-top type-dark" id="audience-card-8253681caf" data-id="tooltip"><style>
  	.tce1affd6-d7c5-4d9c-8067-6ba03e1b5890 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-top {
        margin-top: -10px;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-top::before {
        border-top: 8px solid transparent;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-bottom {
        margin-top: 10px;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-left {
        margin-left: -10px;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-left::before {
        border-left: 8px solid transparent;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-right {
        margin-left: 10px;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-right::before {
        border-right: 8px solid transparent;
    }
    .tce1affd6-d7c5-4d9c-8067-6ba03e1b5890.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-8253681caf" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>13 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>6.7M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.40% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t71323d06-4250-45ed-9954-748f5d0b3dc4 place-top type-dark" id="collection-8253681caf-icon" data-id="tooltip"><style>
  	.t71323d06-4250-45ed-9954-748f5d0b3dc4 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t71323d06-4250-45ed-9954-748f5d0b3dc4.place-top {
        margin-top: -10px;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-top::before {
        border-top: 8px solid transparent;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-bottom {
        margin-top: 10px;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-left {
        margin-left: -10px;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-left::before {
        border-left: 8px solid transparent;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-right {
        margin-left: 10px;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-right::before {
        border-right: 8px solid transparent;
    }
    .t71323d06-4250-45ed-9954-748f5d0b3dc4.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-8253681caf-icon" data-tip="r/datascientists, r/bigdata_analytics, r/dataanalytics, r/bigdata, r/dataanalysis, r/BusinessIntelligence" currentitem="false">+6</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/data" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qoxz/styles/communityIcon_mrtxv12eutk61.png?width=256&amp;s=d2179b3d905984bee5332a08e6d33692b90fae15" alt="data"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/analytics" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rhz9/styles/communityIcon_gyisrr8vpei31.png?width=256&amp;s=421b4a63cfb7177d75995968607256509dc9496e" alt="analytics"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/datasets" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r97t/styles/communityIcon_ri05w19k4zh01.png?width=256&amp;s=020d7a2621a938f0da80fd7e6d5b4d1ac820408a" alt="datasets"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/dataengineering" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_36en4/styles/communityIcon_t74nv7kttaz61.png?width=256&amp;s=c7f7095449533edfce5ab2e2cde34f5343e75d63" alt="dataengineering"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/statistics" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhfi/styles/communityIcon_yce0j6me7s931.png?width=256&amp;s=aa54117e1283119c19b69e17a77035db63366a2f" alt="statistics"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/datascience" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sptq/styles/communityIcon_fdj8zurrifa71.png?width=256&amp;s=a9a418840926af79a511991bce743bc67e704730" alt="datascience"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8253681caf-icon" data-tip="r/MachineLearning" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r3gv/styles/communityIcon_kilpomt3l5c51.png?width=256&amp;s=671205393c49c1a601b16e1ba19c2a25fb0f0d22" alt="MachineLearning"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Fitness Enthusiasts</h2><div class="__react_component_tooltip td7bac5a9-3b51-4acb-9d7a-8afcebd88834 place-top type-dark" id="audience-card-a97ab91eb8" data-id="tooltip"><style>
  	.td7bac5a9-3b51-4acb-9d7a-8afcebd88834 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-top {
        margin-top: -10px;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-top::before {
        border-top: 8px solid transparent;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-bottom {
        margin-top: 10px;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-left {
        margin-left: -10px;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-left::before {
        border-left: 8px solid transparent;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-right {
        margin-left: 10px;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-right::before {
        border-right: 8px solid transparent;
    }
    .td7bac5a9-3b51-4acb-9d7a-8afcebd88834.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-a97ab91eb8" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>12 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>28.4M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.66% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip td31516e7-00fb-480c-a5b0-22780f9433b1 place-top type-dark" id="collection-a97ab91eb8-icon" data-id="tooltip"><style>
  	.td31516e7-00fb-480c-a5b0-22780f9433b1 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.td31516e7-00fb-480c-a5b0-22780f9433b1.place-top {
        margin-top: -10px;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-top::before {
        border-top: 8px solid transparent;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-bottom {
        margin-top: 10px;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-left {
        margin-left: -10px;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-left::before {
        border-left: 8px solid transparent;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-right {
        margin-left: 10px;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-right::before {
        border-right: 8px solid transparent;
    }
    .td31516e7-00fb-480c-a5b0-22780f9433b1.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-a97ab91eb8-icon" data-tip="r/workout, r/yoga, r/loseit, r/strength_training, r/Fitness" currentitem="false">+5</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/personaltraining" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2u17x/styles/communityIcon_upqk0cddlfwb1.png?width=256&amp;s=3922f1905584e88cdb775b11474f102e9795de95" alt="personaltraining"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/physicaltherapy" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tj75/styles/communityIcon_bvdjns7ytqub1.png?width=256&amp;s=48e3a1a2bf6555c0238de1af87cbaf7ce3082d89" alt="physicaltherapy"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/fitness30plus" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2zswl/styles/communityIcon_suox8tsh917b1.png?width=256&amp;s=bd06b959870616dae43bc47a3d67208d66edd2b3" alt="fitness30plus"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/weightroom" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ssmu/styles/communityIcon_h2ponceq8hw01.png?width=256&amp;s=5d2edcfa3fabbd809fcab16b16a1012b3fa2e75e" alt="weightroom"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/GymMotivation" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wvep/styles/communityIcon_64030pe319gc1.png?width=256&amp;s=16ff21ded46033b55add78fd28602f2af38f9de7" alt="GymMotivation"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/GYM" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qizo/styles/communityIcon_k6ps1zdvy93a1.jpg?width=256&amp;s=962d835f639e08f92bd39c0d64251ffa4ce76961" alt="GYM"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a97ab91eb8-icon" data-tip="r/Health" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qh9z/styles/communityIcon_rke0til8qkw61.png?width=256&amp;s=4e85c3ba012c2bc88ef3faab33a900507b669c47" alt="Health"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Gaming</h2><div class="__react_component_tooltip tc09c2d5e-ea82-4f79-b6db-473abb4752f6 place-top type-dark" id="audience-card-0680322027" data-id="tooltip"><style>
  	.tc09c2d5e-ea82-4f79-b6db-473abb4752f6 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-top {
        margin-top: -10px;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-top::before {
        border-top: 8px solid transparent;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-bottom {
        margin-top: 10px;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-left {
        margin-left: -10px;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-left::before {
        border-left: 8px solid transparent;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-right {
        margin-left: 10px;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-right::before {
        border-right: 8px solid transparent;
    }
    .tc09c2d5e-ea82-4f79-b6db-473abb4752f6.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-0680322027" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>11 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>49.1M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.20% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t599fdc16-8b10-4596-97b2-d59b855bab0e place-top type-dark" id="collection-0680322027-icon" data-id="tooltip"><style>
  	.t599fdc16-8b10-4596-97b2-d59b855bab0e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t599fdc16-8b10-4596-97b2-d59b855bab0e.place-top {
        margin-top: -10px;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-top::before {
        border-top: 8px solid transparent;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-bottom {
        margin-top: 10px;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-left {
        margin-left: -10px;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-left::before {
        border-left: 8px solid transparent;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-right {
        margin-left: 10px;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-right::before {
        border-right: 8px solid transparent;
    }
    .t599fdc16-8b10-4596-97b2-d59b855bab0e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-0680322027-icon" data-tip="r/IndieGaming, r/GamingLeaksAndRumours, r/pcgaming, r/gaming" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/XboxGamers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tsys/styles/communityIcon_ik24dl6n4lb51.png?width=256&amp;s=9ed654512824dd7fbb63eb825a775a9d0b681a15" alt="XboxGamers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/TwitchStreaming" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_33958/styles/communityIcon_5ywiz3oug7251.png?width=256&amp;s=b497a54de3256c31495c53702e8a9581ce32bbf4" alt="TwitchStreaming"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/gamers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ql62/styles/communityIcon_leqfxm89l5h01.png?width=256&amp;s=463f03e9fae8ce99947533a3fde00d0985152f78" alt="gamers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/GamerPals" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wfh2/styles/communityIcon_h9a2y7z61xn51.jpg?width=256&amp;s=1b2d2818a795b28de173d94a79ad7175895de4b5" alt="GamerPals"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/macgaming" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rk3e/styles/communityIcon_w3iywk5ym8l31.png?width=256&amp;s=d821dd21ffadbac47961f467de6282f2f03f101a" alt="macgaming"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/CozyGamers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_487hv0/styles/communityIcon_o75oa325fp1c1.png?width=256&amp;s=a3b92e2d49ab7da83cabb0b5efac355350ee602c" alt="CozyGamers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-0680322027-icon" data-tip="r/linux_gaming" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r2u0/styles/communityIcon_nrhnuu07r3k21.png?width=256&amp;s=657ae6bda8da52d6638b8292646ef4db8f5319ed" alt="linux_gaming"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Gardeners</h2><div class="__react_component_tooltip tdafa51ba-120f-4a4e-b30b-6b7f27878ec8 place-top type-dark" id="audience-card-4ea5627ec3" data-id="tooltip"><style>
  	.tdafa51ba-120f-4a4e-b30b-6b7f27878ec8 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-top {
        margin-top: -10px;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-top::before {
        border-top: 8px solid transparent;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-bottom {
        margin-top: 10px;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-left {
        margin-left: -10px;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-left::before {
        border-left: 8px solid transparent;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-right {
        margin-left: 10px;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-right::before {
        border-right: 8px solid transparent;
    }
    .tdafa51ba-120f-4a4e-b30b-6b7f27878ec8.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-4ea5627ec3" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>11 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>11.3M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.45% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t039b4cf2-bc65-47d2-922f-e5957ab709af place-top type-dark" id="collection-4ea5627ec3-icon" data-id="tooltip"><style>
  	.t039b4cf2-bc65-47d2-922f-e5957ab709af {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t039b4cf2-bc65-47d2-922f-e5957ab709af.place-top {
        margin-top: -10px;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-top::before {
        border-top: 8px solid transparent;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-bottom {
        margin-top: 10px;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-left {
        margin-left: -10px;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-left::before {
        border-left: 8px solid transparent;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-right {
        margin-left: 10px;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-right::before {
        border-right: 8px solid transparent;
    }
    .t039b4cf2-bc65-47d2-922f-e5957ab709af.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-4ea5627ec3-icon" data-tip="r/flowers, r/Permaculture, r/whatsthisplant, r/gardening" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/GardenersWorld" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ct1mu/styles/communityIcon_ym8xjmdd9pa41.jpg?width=256&amp;s=d60218da86fd8088da767040304bf552f6cd5d2e" alt="GardenersWorld"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/UrbanGardening" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vunn/styles/communityIcon_30dpxntsdxgb1.jpg?width=256&amp;s=2883c8bcc0e24bf648dd16fc4d75d101a22ab131" alt="UrbanGardening"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/GardeningUK" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_31s8w/styles/communityIcon_7o71r5h5rova1.png?width=256&amp;s=bd40a97e23260abdffeac9275c6d3d5c9c7f3c6e" alt="GardeningUK"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/SavageGarden" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qwxx/styles/communityIcon_uwq1feks5ep61.png?width=256&amp;s=644011160e193bfcc216c599ae25e09827a432bb" alt="SavageGarden"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/vegetablegardening" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_30g5j/styles/communityIcon_8syvm2ahcpz91.png?width=256&amp;s=d8643f0e91a9aa204d2649141eb4dfc6bcefb74b" alt="vegetablegardening"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/succulents" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2smnv/styles/communityIcon_cnzkp15lmkn41.png?width=256&amp;s=c46fc970b04ea7b31807517112924679a021a33f" alt="succulents"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-4ea5627ec3-icon" data-tip="r/mycology" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qu6q/styles/communityIcon_aezomltxrgfd1.png?width=256&amp;s=ec3e08b557ef4c2858c46b7e7f1d99b4a850e1ba" alt="mycology"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Photographers</h2><div class="__react_component_tooltip tdfae742d-ac5f-49a3-9ae7-33f77fcc0929 place-top type-dark" id="audience-card-cb0165ae74" data-id="tooltip"><style>
  	.tdfae742d-ac5f-49a3-9ae7-33f77fcc0929 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-top {
        margin-top: -10px;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-top::before {
        border-top: 8px solid transparent;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-bottom {
        margin-top: 10px;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-left {
        margin-left: -10px;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-left::before {
        border-left: 8px solid transparent;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-right {
        margin-left: 10px;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-right::before {
        border-right: 8px solid transparent;
    }
    .tdfae742d-ac5f-49a3-9ae7-33f77fcc0929.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-cb0165ae74" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>11 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>10.0M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>0.91% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t24da4fbe-6cce-4f68-838c-c1395081cd73 place-top type-dark" id="collection-cb0165ae74-icon" data-id="tooltip"><style>
  	.t24da4fbe-6cce-4f68-838c-c1395081cd73 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t24da4fbe-6cce-4f68-838c-c1395081cd73.place-top {
        margin-top: -10px;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-top::before {
        border-top: 8px solid transparent;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-bottom {
        margin-top: 10px;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-left {
        margin-left: -10px;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-left::before {
        border-left: 8px solid transparent;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-right {
        margin-left: 10px;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-right::before {
        border-right: 8px solid transparent;
    }
    .t24da4fbe-6cce-4f68-838c-c1395081cd73.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-cb0165ae74-icon" data-tip="r/Beginning_Photography, r/postprocessing, r/AskPhotography, r/photography" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/WeddingPhotography" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rdee/styles/communityIcon_8mezc6glqgba1.jpg?width=256&amp;s=85304563fccdbf1e4096ee18e5525e4e0599ed5a" alt="WeddingPhotography"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/Nikon" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qr6k/styles/communityIcon_gyniux4hanf41.png?width=256&amp;s=99b48183aa40e7f314494c2a5ad3c4dc0bb87bf4" alt="Nikon"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/canon" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qi07/styles/communityIcon_0wqoi0s9yzia1.png?width=256&amp;s=993d104ce5b1ea3858ea20163f54cd242c62daaf" alt="canon"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/AnalogCommunity" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3k1ng/styles/communityIcon_b3ldr25exyo91.png?width=256&amp;s=bf84e331d4be15aeb5eef02308e0c010268f6d08" alt="AnalogCommunity"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/SonyAlpha" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2si08/styles/communityIcon_ur987suktsk11.png?width=256&amp;s=44e6eb62b24ab804bc0bb0f5e859769af1072adf" alt="SonyAlpha"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/streetphotography" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rpuv/styles/communityIcon_apxxymqe7hzb1.png?width=256&amp;s=3cdf0dcff8feabba7676d817055ac72a01abace0" alt="streetphotography"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-cb0165ae74-icon" data-tip="r/analog" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r344/styles/communityIcon_arrf56nbq1t81.png?width=256&amp;s=27aea613bb02fb3d46808153646e2bb8ad16626e" alt="analog"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">NFT Collectors</h2><div class="__react_component_tooltip t30067393-13cb-4928-933d-c68f169e8288 place-top type-dark" id="audience-card-3a5039198a" data-id="tooltip"><style>
  	.t30067393-13cb-4928-933d-c68f169e8288 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t30067393-13cb-4928-933d-c68f169e8288.place-top {
        margin-top: -10px;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-top::before {
        border-top: 8px solid transparent;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t30067393-13cb-4928-933d-c68f169e8288.place-bottom {
        margin-top: 10px;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t30067393-13cb-4928-933d-c68f169e8288.place-left {
        margin-left: -10px;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-left::before {
        border-left: 8px solid transparent;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t30067393-13cb-4928-933d-c68f169e8288.place-right {
        margin-left: 10px;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-right::before {
        border-right: 8px solid transparent;
    }
    .t30067393-13cb-4928-933d-c68f169e8288.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-3a5039198a" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>10 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>3.1M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.19% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t67221027-20db-4ae3-b0bc-d4ff8f1a7f09 place-top type-dark" id="collection-3a5039198a-icon" data-id="tooltip"><style>
  	.t67221027-20db-4ae3-b0bc-d4ff8f1a7f09 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-top {
        margin-top: -10px;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-top::before {
        border-top: 8px solid transparent;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-bottom {
        margin-top: 10px;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-left {
        margin-left: -10px;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-left::before {
        border-left: 8px solid transparent;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-right {
        margin-left: 10px;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-right::before {
        border-right: 8px solid transparent;
    }
    .t67221027-20db-4ae3-b0bc-d4ff8f1a7f09.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-3a5039198a-icon" data-tip="r/opensea, r/NFTsMarketplace, r/NFT" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/DigitalItems" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_47q1o0/styles/communityIcon_3jnu5p724ir61.PNG?width=256&amp;s=248272c7253a15a4a164099d59d1d247fb93a418" alt="DigitalItems"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/OpenseaMarket" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_4507cc/styles/communityIcon_xqcicuoqtfo61.jpg?width=256&amp;s=55c52165b3547313938539d4881de504175eff98" alt="OpenseaMarket"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/CryptoArt" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2zxz9/styles/communityIcon_gboap2hue5d91.png?width=256&amp;s=0f6fb1f7ffc1b33b7fd26106e89af911682d52f8" alt="CryptoArt"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/OpenSeaNFT" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_46w8j5/styles/communityIcon_vwwsjwh70mq61.png?width=256&amp;s=95f1f68daa456556b062f607af0efaf349a42228" alt="OpenSeaNFT"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/NFTMarketplace" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3vnlab/styles/communityIcon_r42ga4wzcxe61.png?width=256&amp;s=3cbb935665f01fc329654d5958ec5d8480495a5b" alt="NFTMarketplace"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/NFTmarket" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_36bg0l/styles/communityIcon_7zkqtcmm4ow71.png?width=256&amp;s=c9ab4b5146b387704623cf01a38122cf8a985c49" alt="NFTmarket"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3a5039198a-icon" data-tip="r/NFTExchange" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3yli2s/styles/communityIcon_188iuhm44ow71.png?width=256&amp;s=fe2f99d7eb6ad8751a09811aac0dcaed668eb92c" alt="NFTExchange"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Ecommerce</h2><div class="__react_component_tooltip t6f80e64c-f418-4520-ab68-8707ea06b796 place-top type-dark" id="audience-card-d8e8e20b89" data-id="tooltip"><style>
  	.t6f80e64c-f418-4520-ab68-8707ea06b796 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t6f80e64c-f418-4520-ab68-8707ea06b796.place-top {
        margin-top: -10px;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-bottom {
        margin-top: 10px;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-left {
        margin-left: -10px;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-right {
        margin-left: 10px;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6f80e64c-f418-4520-ab68-8707ea06b796.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><span class="font-normal" data-for="audience-card-d8e8e20b89" data-tip="You have already saved this curated audience" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-d8e8e20b89" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>10 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>1.6M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.91% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip te62f001b-29af-481e-b75e-84b2919ab13f place-top type-dark" id="collection-d8e8e20b89-icon" data-id="tooltip"><style>
  	.te62f001b-29af-481e-b75e-84b2919ab13f {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.te62f001b-29af-481e-b75e-84b2919ab13f.place-top {
        margin-top: -10px;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-top::before {
        border-top: 8px solid transparent;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .te62f001b-29af-481e-b75e-84b2919ab13f.place-bottom {
        margin-top: 10px;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .te62f001b-29af-481e-b75e-84b2919ab13f.place-left {
        margin-left: -10px;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-left::before {
        border-left: 8px solid transparent;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .te62f001b-29af-481e-b75e-84b2919ab13f.place-right {
        margin-left: 10px;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-right::before {
        border-right: 8px solid transparent;
    }
    .te62f001b-29af-481e-b75e-84b2919ab13f.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-d8e8e20b89-icon" data-tip="r/ecommerce_growth, r/Random_Acts_of_Etsy, r/AmazonSeller" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/ecommercemarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3mb2t/styles/communityIcon_9ffch907ihcb1.png?width=256&amp;s=56b2f93cb3e019f7592ab76bda3fade1fbe95543" alt="ecommercemarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/reviewmyshopify" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3g5ir/styles/communityIcon_3s1r6rtsy9ta1.png?width=256&amp;s=8e6d50b60ba181b4aadb89c2952990fb06553ba3" alt="reviewmyshopify"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/EtsySellers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wthr/styles/communityIcon_w17e9nq8qy2b1.jpg?width=256&amp;s=96c049d9d804ed2494b15316f5e478c46b06f7a9" alt="EtsySellers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/Etsy" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qq24/styles/communityIcon_p91o79y2obo41.png?width=256&amp;s=6df3da05f6522b7e2b28fd01e9ce5d854887ab51" alt="Etsy"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/shopify" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sn78/styles/communityIcon_kagwtg8m01511.png?width=256&amp;s=856f0b7a52b9866f3d204b8ca227e9a67eb4f6d0" alt="shopify"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/dropship" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2txzl/styles/communityIcon_l2qgw0kqtqx41.png?width=256&amp;s=ae01a160ee8e832b0e6250fcc2ea22fc9eb0f5ac" alt="dropship"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d8e8e20b89-icon" data-tip="r/ecommerce" currentitem="false"><img class="h-full w-full rounded-sm" src="https://b.thumbs.redditmedia.com/2F1Wf8BfsceuKHJWcphsNd_DMF8HFxjZU0U4EkJQcys.png" alt="ecommerce"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">SEOs</h2><div class="__react_component_tooltip t2bdb784e-8c6a-49f2-b069-8cff076c2e47 place-top type-dark" id="audience-card-a29fd67a19" data-id="tooltip"><style>
  	.t2bdb784e-8c6a-49f2-b069-8cff076c2e47 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-top {
        margin-top: -10px;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-top::before {
        border-top: 8px solid transparent;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-bottom {
        margin-top: 10px;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-left {
        margin-left: -10px;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-left::before {
        border-left: 8px solid transparent;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-right {
        margin-left: 10px;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-right::before {
        border-right: 8px solid transparent;
    }
    .t2bdb784e-8c6a-49f2-b069-8cff076c2e47.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-a29fd67a19" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>10 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>535k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.48% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7 place-top type-dark" id="collection-a29fd67a19-icon" data-id="tooltip"><style>
  	.t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-top {
        margin-top: -10px;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-top::before {
        border-top: 8px solid transparent;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-bottom {
        margin-top: 10px;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-left {
        margin-left: -10px;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-left::before {
        border-left: 8px solid transparent;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-right {
        margin-left: 10px;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-right::before {
        border-right: 8px solid transparent;
    }
    .t1fb5b26d-6e40-40e2-a4d1-4a334040a3d7.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-a29fd67a19-icon" data-tip="r/SEO_Talk, r/bigseo, r/SEO" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/The_SEO" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3kpkl/styles/communityIcon_xrsmcwzkk5rd1.PNG?width=256&amp;s=15e750de224b6d327f95197a3011ac38fb738cef" alt="The_SEO"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/GoogleSearchConsole" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_1bgb2k/styles/communityIcon_goyn7sxf77j51.png?width=256&amp;s=2f849cb53b6a57acbaa1963bee232c703d3dc5c0" alt="GoogleSearchConsole"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/Local_SEO" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_33b02/styles/communityIcon_aylek8n6c3j81.jpg?width=256&amp;s=837c6380444a73268fcc0106164018c93d74b957" alt="Local_SEO"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/SEO_cases" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_779iet/styles/communityIcon_9xzxttk2eut91.png?width=256&amp;s=5391ec60099e14b56e7f879259efb4f0c991556c" alt="SEO_cases"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/seogrowth" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_4t7j8c/styles/communityIcon_gkpdve958xd71.png?width=256&amp;s=4fa7109771fae6804dfd2fd7e68f54726e89a3d6" alt="seogrowth"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/TechSEO" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3eciw/styles/communityIcon_54khj01nn4921.jpg?width=256&amp;s=51569861d75a98b465bee405603b16a05426bc17" alt="TechSEO"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-a29fd67a19-icon" data-tip="r/SEO_Digital_Marketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3j43f/styles/communityIcon_tmxl7sjsju6d1.png?width=256&amp;s=94a9106f670dda620e9462a4515fa76116bc78d8" alt="SEO_Digital_Marketing"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Self-Promoters</h2><div class="__react_component_tooltip tb7edff8f-55b3-4eb2-9849-1db6b5baabb3 place-top type-dark" id="audience-card-8009cfa6d6" data-id="tooltip"><style>
  	.tb7edff8f-55b3-4eb2-9849-1db6b5baabb3 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-top {
        margin-top: -10px;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-top::before {
        border-top: 8px solid transparent;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-bottom {
        margin-top: 10px;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-left {
        margin-left: -10px;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-left::before {
        border-left: 8px solid transparent;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-right {
        margin-left: 10px;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-right::before {
        border-right: 8px solid transparent;
    }
    .tb7edff8f-55b3-4eb2-9849-1db6b5baabb3.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-8009cfa6d6" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>9 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>371k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>4.95% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t5329a5e5-2567-4f2c-8388-98ea44332578 place-top type-dark" id="collection-8009cfa6d6-icon" data-id="tooltip"><style>
  	.t5329a5e5-2567-4f2c-8388-98ea44332578 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t5329a5e5-2567-4f2c-8388-98ea44332578.place-top {
        margin-top: -10px;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-top::before {
        border-top: 8px solid transparent;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-bottom {
        margin-top: 10px;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-left {
        margin-left: -10px;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-left::before {
        border-left: 8px solid transparent;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-right {
        margin-left: 10px;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-right::before {
        border-right: 8px solid transparent;
    }
    .t5329a5e5-2567-4f2c-8388-98ea44332578.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-8009cfa6d6-icon" data-tip="r/IMadeThis, r/AppIdeas, r/SideProject" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/TestMyApp" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_37hmj/styles/communityIcon_22j5hexmopx31.png?width=256&amp;s=12393554cdd6ed8585b05734a52b52bcdbfc62a0" alt="TestMyApp"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/betatests" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vu3w/styles/communityIcon_96rnde8haxi41.png?width=256&amp;s=d9dfdd6ef779a28e1f8e2bc16f1d24425a82b8eb" alt="betatests"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/ProductHunters" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3ego4/styles/communityIcon_i2s2g09gitv61.jpg?width=256&amp;s=093ecb5ee6efcdc48d4575451d23fd389f77632a" alt="ProductHunters"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/alphaandbetausers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2znn4/styles/communityIcon_b55xn3gqq2m61.png?width=256&amp;s=d389d2c73f5f6ec0d29627706757c885ae116a1c" alt="alphaandbetausers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/selfpromotion" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sc3r/styles/communityIcon_nnj8j2kqh5ma1.png?width=256&amp;s=c43032fdc3438c9ee73eae3f07da41311bfee48e" alt="selfpromotion"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-8009cfa6d6-icon" data-tip="r/youtubepromotion" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2yg9m/styles/communityIcon_wb7ximv0mdg51.png?width=256&amp;s=2a61ca67887c15d923fa3199d53eca10d004c6c4" alt="youtubepromotion"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Parents</h2><div class="__react_component_tooltip t586a9fd8-d5da-44a2-af79-f5de4d45b81b place-top type-dark" id="audience-card-ea3c13a592" data-id="tooltip"><style>
  	.t586a9fd8-d5da-44a2-af79-f5de4d45b81b {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-top {
        margin-top: -10px;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-top::before {
        border-top: 8px solid transparent;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-bottom {
        margin-top: 10px;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-left {
        margin-left: -10px;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-left::before {
        border-left: 8px solid transparent;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-right {
        margin-left: 10px;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-right::before {
        border-right: 8px solid transparent;
    }
    .t586a9fd8-d5da-44a2-af79-f5de4d45b81b.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-ea3c13a592" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>9 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>11.8M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.64% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t97e9702b-0761-472c-b829-5d3134967cb8 place-top type-dark" id="collection-ea3c13a592-icon" data-id="tooltip"><style>
  	.t97e9702b-0761-472c-b829-5d3134967cb8 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t97e9702b-0761-472c-b829-5d3134967cb8.place-top {
        margin-top: -10px;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-top::before {
        border-top: 8px solid transparent;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t97e9702b-0761-472c-b829-5d3134967cb8.place-bottom {
        margin-top: 10px;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t97e9702b-0761-472c-b829-5d3134967cb8.place-left {
        margin-left: -10px;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-left::before {
        border-left: 8px solid transparent;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t97e9702b-0761-472c-b829-5d3134967cb8.place-right {
        margin-left: 10px;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-right::before {
        border-right: 8px solid transparent;
    }
    .t97e9702b-0761-472c-b829-5d3134967cb8.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-ea3c13a592-icon" data-tip="r/raisingkids, r/Parenting" currentitem="false">+2</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/Parents" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qyuj/styles/communityIcon_c2k6ijob4f831.png?width=256&amp;s=20faf7145a6d2eda5a061d204066e8f201893aca" alt="Parents"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/parentsofmultiples" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2s8g3/styles/communityIcon_kv3fjbacwxl41.PNG?width=256&amp;s=4f70461dca4d695de6b0c8e546f7b8c4fd8b660a" alt="parentsofmultiples"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/NewParents" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2snqi/styles/communityIcon_dw6sw21ze42a1.png?width=256&amp;s=bac90d7ea6232605dbcf426a4c51e19ee03c51d8" alt="NewParents"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/toddlers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ta5v/styles/communityIcon_y928piiihx7b1.png?width=256&amp;s=0f6d8251017a8e3a41f878c107ecdb9d89510d46" alt="toddlers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/beyondthebump" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2u06v/styles/communityIcon_kq34nlfze8l61.jpg?width=256&amp;s=b2148cb1767828cc507a3feea83294e81a7f3ca4" alt="beyondthebump"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/SingleParents" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r6jl/styles/communityIcon_v523xlf2r37a1.png?width=256&amp;s=2d4b14853be9412b4d7d92917d7704ba623a339f" alt="SingleParents"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ea3c13a592-icon" data-tip="r/daddit" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rxue/styles/communityIcon_ssii86uo15p81.png?width=256&amp;s=39acd01ddb2023e2fcaf3293bfa7a0788f330fad" alt="daddit"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">No-code</h2><div class="__react_component_tooltip t6c2de45f-9144-4d13-b1db-767fd52d80ea place-top type-dark" id="audience-card-d587425504" data-id="tooltip"><style>
  	.t6c2de45f-9144-4d13-b1db-767fd52d80ea {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-top {
        margin-top: -10px;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-bottom {
        margin-top: 10px;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-left {
        margin-left: -10px;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-right {
        margin-left: 10px;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6c2de45f-9144-4d13-b1db-767fd52d80ea.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-d587425504" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>9 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>94k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>5.28% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t0f1f85c6-928c-4a5a-98ff-220a06a6df15 place-top type-dark" id="collection-d587425504-icon" data-id="tooltip"><style>
  	.t0f1f85c6-928c-4a5a-98ff-220a06a6df15 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-top {
        margin-top: -10px;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-top::before {
        border-top: 8px solid transparent;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-bottom {
        margin-top: 10px;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-left {
        margin-left: -10px;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-left::before {
        border-left: 8px solid transparent;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-right {
        margin-left: 10px;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-right::before {
        border-right: 8px solid transparent;
    }
    .t0f1f85c6-928c-4a5a-98ff-220a06a6df15.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-d587425504-icon" data-tip="r/nocodedevelopers, r/lowcode, r/NoCodeSaaS, r/nocode" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d587425504-icon" data-tip="r/Adalo" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2u3q46/styles/communityIcon_69n8m668zvg91.jpeg?width=256&amp;s=46d6e1352bf78bf6239ce307a305503e991043ce" alt="Adalo"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d587425504-icon" data-tip="r/NoCodeMovement" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ta3fr/styles/communityIcon_c9krbboo23851.jpg?width=256&amp;s=2526d13d3ad2bacd9c5dfc7b8962e87283a7d188" alt="NoCodeMovement"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d587425504-icon" data-tip="r/nocodelowcode" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3fxtff/styles/communityIcon_fhwk5sawaf061.png?width=256&amp;s=7e10e097e0aac7893394865a6d220cd1dc6f0866" alt="nocodelowcode"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d587425504-icon" data-tip="r/Airtable" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_36dkt/styles/communityIcon_ewauhccjm2c51.jpg?width=256&amp;s=c7ea2e4550e192c2aa3d1f8a2db52c3f2f69eb5f" alt="Airtable"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-d587425504-icon" data-tip="r/webflow" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_30h5p/styles/communityIcon_ddtmvgjhudsb1.png?width=256&amp;s=46c38bd21f2bd5d743b368361e588cf74b8e2b25" alt="webflow"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Cold Email</h2><div class="__react_component_tooltip tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1 place-top type-dark" id="audience-card-3e4a0a1751" data-id="tooltip"><style>
  	.tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-top {
        margin-top: -10px;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-top::before {
        border-top: 8px solid transparent;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-bottom {
        margin-top: 10px;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-left {
        margin-left: -10px;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-left::before {
        border-left: 8px solid transparent;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-right {
        margin-left: 10px;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-right::before {
        border-right: 8px solid transparent;
    }
    .tfd124bf3-d5f6-4b8b-8e12-33ca8dbb7ed1.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-3e4a0a1751" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>9 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>667k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.30% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip td4d449a0-616e-40c4-86f2-30faf0bc6e38 place-top type-dark" id="collection-3e4a0a1751-icon" data-id="tooltip"><style>
  	.td4d449a0-616e-40c4-86f2-30faf0bc6e38 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-top {
        margin-top: -10px;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-top::before {
        border-top: 8px solid transparent;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-bottom {
        margin-top: 10px;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-left {
        margin-left: -10px;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-left::before {
        border-left: 8px solid transparent;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-right {
        margin-left: 10px;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-right::before {
        border-right: 8px solid transparent;
    }
    .td4d449a0-616e-40c4-86f2-30faf0bc6e38.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-3e4a0a1751-icon" data-tip="r/OutreachHacks, r/B2BSaaS, r/copywriting" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/EmailOutreach" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_5bnoii/styles/communityIcon_q3yed09458i81.png?width=256&amp;s=d70d0bb8c1dae893b3a5f3af7e7ddbd65ede232b" alt="EmailOutreach"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/coldemail" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3bmai/styles/communityIcon_n88yyqapn9v41.png?width=256&amp;s=8faa2985d15310efa15df7b7ae8188fb9eb1bd68" alt="coldemail"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/b2b_sales" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3bphg/styles/communityIcon_jr9s7ybv5xd91.jpg?width=256&amp;s=966aa7a81db0684066c4bf04653fd6c593dc2c1a" alt="b2b_sales"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/LeadGeneration" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rh2i/styles/communityIcon_k6i0s99bz5p61.png?width=256&amp;s=40522b35a0af1dbfffb7c140568e2fcd8c32d804" alt="LeadGeneration"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/Emailmarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r1yx/styles/communityIcon_k1li29utju8a1.png?width=256&amp;s=492b3bde8bd185ea9a377390a01e81d6de9d1f25" alt="Emailmarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3e4a0a1751-icon" data-tip="r/sales" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qib3/styles/communityIcon_9zu1p9ie3ljc1.png?width=256&amp;s=d4f801c12556ffce512a7bc154a0f8089402db4b" alt="sales"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Financial Independence</h2><div class="__react_component_tooltip t06b157a0-eecd-4817-a682-acb14f6f0b6d place-top type-dark" id="audience-card-41511f40f8" data-id="tooltip"><style>
  	.t06b157a0-eecd-4817-a682-acb14f6f0b6d {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-top {
        margin-top: -10px;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-top::before {
        border-top: 8px solid transparent;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-bottom {
        margin-top: 10px;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-left {
        margin-left: -10px;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-left::before {
        border-left: 8px solid transparent;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-right {
        margin-left: 10px;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-right::before {
        border-right: 8px solid transparent;
    }
    .t06b157a0-eecd-4817-a682-acb14f6f0b6d.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-41511f40f8" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>31.4M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.25% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tab014f61-8b95-47e4-af2f-c91b4c7c2967 place-top type-dark" id="collection-41511f40f8-icon" data-id="tooltip"><style>
  	.tab014f61-8b95-47e4-af2f-c91b4c7c2967 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-top {
        margin-top: -10px;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-top::before {
        border-top: 8px solid transparent;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-bottom {
        margin-top: 10px;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-left {
        margin-left: -10px;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-left::before {
        border-left: 8px solid transparent;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-right {
        margin-left: 10px;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-right::before {
        border-right: 8px solid transparent;
    }
    .tab014f61-8b95-47e4-af2f-c91b4c7c2967.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-41511f40f8-icon" data-tip="r/FIREUK, r/financialindependence, r/Frugal, r/personalfinance" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-41511f40f8-icon" data-tip="r/fatFIRE" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3hqta/styles/communityIcon_c46gar6cisc61.png?width=256&amp;s=6b34b810627b2b3c49d4d753c681ce851e1c8e7e" alt="fatFIRE"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-41511f40f8-icon" data-tip="r/Fire" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qx4j/styles/communityIcon_8wnnp7ykwr6b1.jpg?width=256&amp;s=2f679bb36bae3d70fb9631eb32190d6ce1702249" alt="Fire"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-41511f40f8-icon" data-tip="r/FinancialPlanning" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qwze/styles/communityIcon_3p9rv5hoxq631.png?width=256&amp;s=884b6213279ae2a7d3d63f433ae4f0d14f10a4c4" alt="FinancialPlanning"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-41511f40f8-icon" data-tip="r/UKPersonalFinance" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2wkka/styles/communityIcon_pm84nm3tm5011.png?width=256&amp;s=eea07cc4a88179bcb3e6375e266346354e814805" alt="UKPersonalFinance"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">3D Printers</h2><div class="__react_component_tooltip ta95b2da3-fd0f-45be-9a44-59d1104c81f1 place-top type-dark" id="audience-card-04ea4ec375" data-id="tooltip"><style>
  	.ta95b2da3-fd0f-45be-9a44-59d1104c81f1 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-top {
        margin-top: -10px;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-top::before {
        border-top: 8px solid transparent;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-bottom {
        margin-top: 10px;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-left {
        margin-left: -10px;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-left::before {
        border-left: 8px solid transparent;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-right {
        margin-left: 10px;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-right::before {
        border-right: 8px solid transparent;
    }
    .ta95b2da3-fd0f-45be-9a44-59d1104c81f1.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-04ea4ec375" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>5.9M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.93% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t64b8bcd2-0999-45da-8b7d-7d6a58626e43 place-top type-dark" id="collection-04ea4ec375-icon" data-id="tooltip"><style>
  	.t64b8bcd2-0999-45da-8b7d-7d6a58626e43 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-top {
        margin-top: -10px;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-top::before {
        border-top: 8px solid transparent;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-bottom {
        margin-top: 10px;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-left {
        margin-left: -10px;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-left::before {
        border-left: 8px solid transparent;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-right {
        margin-left: 10px;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-right::before {
        border-right: 8px solid transparent;
    }
    .t64b8bcd2-0999-45da-8b7d-7d6a58626e43.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-04ea4ec375-icon" data-tip="r/3dprinter, r/3Dprintmything, r/functionalprint" currentitem="false">+3</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-04ea4ec375-icon" data-tip="r/FixMyPrint" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_30mvb/styles/communityIcon_116xkp62mt961.jpg?width=256&amp;s=2a134a516a00a657ef595166beb6e2d68fbc4a0f" alt="FixMyPrint"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-04ea4ec375-icon" data-tip="r/ender3" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_i3pca/styles/communityIcon_v7mktobtenp21.png?width=256&amp;s=7f6b7e55a70e126bfcf30add6e374dd68c49c1a3" alt="ender3"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-04ea4ec375-icon" data-tip="r/3Dmodeling" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sawg/styles/communityIcon_cuqo4ipiolr31.png?width=256&amp;s=7efabed1f07815a2f61d9be7b512fde7539501a0" alt="3Dmodeling"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-04ea4ec375-icon" data-tip="r/blender" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qim4/styles/communityIcon_t1mvkn6ma6g71.png?width=256&amp;s=6d7b358f7f5a335dec23b9299d46a7690462b813" alt="blender"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-04ea4ec375-icon" data-tip="r/3Dprinting" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rk5q/styles/communityIcon_s8h0mrftpnn31.png?width=256&amp;s=0a0f6c26a21fb74a6dc31b02cbff6b4a1ec5e12d" alt="3Dprinting"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Freelancers</h2><div class="__react_component_tooltip taf050454-613d-4a7d-aefd-b9809002ca9a place-top type-dark" id="audience-card-43f455a4e7" data-id="tooltip"><style>
  	.taf050454-613d-4a7d-aefd-b9809002ca9a {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.taf050454-613d-4a7d-aefd-b9809002ca9a.place-top {
        margin-top: -10px;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-top::before {
        border-top: 8px solid transparent;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-bottom {
        margin-top: 10px;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-left {
        margin-left: -10px;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-left::before {
        border-left: 8px solid transparent;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-right {
        margin-left: 10px;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-right::before {
        border-right: 8px solid transparent;
    }
    .taf050454-613d-4a7d-aefd-b9809002ca9a.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-43f455a4e7" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>1.9M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.48% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tc29e220f-5ce5-433d-b350-663db8f2b768 place-top type-dark" id="collection-43f455a4e7-icon" data-id="tooltip"><style>
  	.tc29e220f-5ce5-433d-b350-663db8f2b768 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tc29e220f-5ce5-433d-b350-663db8f2b768.place-top {
        margin-top: -10px;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-top::before {
        border-top: 8px solid transparent;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-bottom {
        margin-top: 10px;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-left {
        margin-left: -10px;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-left::before {
        border-left: 8px solid transparent;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-right {
        margin-left: 10px;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-right::before {
        border-right: 8px solid transparent;
    }
    .tc29e220f-5ce5-433d-b350-663db8f2b768.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-43f455a4e7-icon" data-tip="r/Upwork, r/freelanceWriters, r/freelance, r/WorkOnline" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-43f455a4e7-icon" data-tip="r/Freelancers" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r96d/styles/communityIcon_q8kn2n2trcl61.png?width=256&amp;s=735bdbe46bfb67dbb48d3f215808398454ca452b" alt="Freelancers"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-43f455a4e7-icon" data-tip="r/freelance_forhire" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_38rv2/styles/communityIcon_wfaedgzx5pi11.png?width=256&amp;s=4ed8e58b6b8c9d7cde8fdc36c52e1d44a6d42729" alt="freelance_forhire"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-43f455a4e7-icon" data-tip="r/Fiverr" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tvqo/styles/communityIcon_nhj0q53q3fk91.png?width=256&amp;s=a247bd8ced80d0cab3cfbc7e8a3aa8621fff7618" alt="Fiverr"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-43f455a4e7-icon" data-tip="r/forhire" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qzbh/styles/communityIcon_cltq8kacnop01.png?width=256&amp;s=d80228795427671602623af636c2437839d1e57b" alt="forhire"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Copywriters</h2><div class="__react_component_tooltip tdf327831-92b1-4883-ae5e-c186d5cdfa57 place-top type-dark" id="audience-card-35c522d8d9" data-id="tooltip"><style>
  	.tdf327831-92b1-4883-ae5e-c186d5cdfa57 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-top {
        margin-top: -10px;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-top::before {
        border-top: 8px solid transparent;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-bottom {
        margin-top: 10px;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-left {
        margin-left: -10px;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-left::before {
        border-left: 8px solid transparent;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-right {
        margin-left: 10px;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-right::before {
        border-right: 8px solid transparent;
    }
    .tdf327831-92b1-4883-ae5e-c186d5cdfa57.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-35c522d8d9" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>1.3M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.83% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip te7c20af0-84b4-4189-a3b5-8dfd1610a612 place-top type-dark" id="collection-35c522d8d9-icon" data-id="tooltip"><style>
  	.te7c20af0-84b4-4189-a3b5-8dfd1610a612 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-top {
        margin-top: -10px;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-top::before {
        border-top: 8px solid transparent;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-bottom {
        margin-top: 10px;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-left {
        margin-left: -10px;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-left::before {
        border-left: 8px solid transparent;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-right {
        margin-left: 10px;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-right::before {
        border-right: 8px solid transparent;
    }
    .te7c20af0-84b4-4189-a3b5-8dfd1610a612.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-35c522d8d9-icon" data-tip="r/ContentHacks, r/Write2Publish, r/freelanceWriters, r/copywriting, r/writers" currentitem="false">+5</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-35c522d8d9-icon" data-tip="r/content_marketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2zbx8/styles/communityIcon_ssxyrz51k47d1.png?width=256&amp;s=5374b6b2fcc7f86ce4c07f195d05f1b425437ee2" alt="content_marketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-35c522d8d9-icon" data-tip="r/KeepWriting" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tl2y/styles/communityIcon_rskt0zlgxgd31.jpg?width=256&amp;s=64e18bc63b4678f7d5656984565b4b78384c94ec" alt="KeepWriting"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-35c522d8d9-icon" data-tip="r/SEO" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhbx/styles/communityIcon_191l6xkqju6d1.png?width=256&amp;s=4a29285ca7e84a08e16e3dfdc3ebad5937e55f24" alt="SEO"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Notion Users</h2><div class="__react_component_tooltip t9fa0bce2-4d54-4171-8c94-331f8dfb128f place-top type-dark" id="audience-card-60e8175e2b" data-id="tooltip"><style>
  	.t9fa0bce2-4d54-4171-8c94-331f8dfb128f {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-top {
        margin-top: -10px;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-top::before {
        border-top: 8px solid transparent;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-bottom {
        margin-top: 10px;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-left {
        margin-left: -10px;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-left::before {
        border-left: 8px solid transparent;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-right {
        margin-left: 10px;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-right::before {
        border-right: 8px solid transparent;
    }
    .t9fa0bce2-4d54-4171-8c94-331f8dfb128f.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><span class="font-normal" data-for="audience-card-60e8175e2b" data-tip="You have already saved this curated audience" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-60e8175e2b" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>391k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.35% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tea84e429-27c4-4544-b5c6-2f4a73bca788 place-top type-dark" id="collection-60e8175e2b-icon" data-id="tooltip"><style>
  	.tea84e429-27c4-4544-b5c6-2f4a73bca788 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tea84e429-27c4-4544-b5c6-2f4a73bca788.place-top {
        margin-top: -10px;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-top::before {
        border-top: 8px solid transparent;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-bottom {
        margin-top: 10px;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-left {
        margin-left: -10px;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-left::before {
        border-left: 8px solid transparent;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-right {
        margin-left: 10px;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-right::before {
        border-right: 8px solid transparent;
    }
    .tea84e429-27c4-4544-b5c6-2f4a73bca788.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-60e8175e2b-icon" data-tip="r/Notion" currentitem="false">+1</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/NotionPromote" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_4xlh24/styles/communityIcon_lh0cc7wmlsi71.png?width=256&amp;s=332f70e25556aee0d1977675f394d3cfe3ed5297" alt="NotionPromote"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/BestNotionTemplates" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_9inlb6/styles/communityIcon_88qxyhhok7sb1.jpg?width=256&amp;s=327cd469632c5a5e4067789f9c43ecc7b5d16ad8" alt="BestNotionTemplates"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/AskNotion" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_8lduma/styles/communityIcon_3zxs203svp5b1.jpg?width=256&amp;s=3016d58efebe542cfc8d49eb73b46260c1e7ef48" alt="AskNotion"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/NotionGeeks" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_8ldth9/styles/communityIcon_zj4utjx8vp5b1.png?width=256&amp;s=571eb3460a723fb98182dcd9eb280d223918e383" alt="NotionGeeks"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/FreeNotionTemplates" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_87sg5q/styles/communityIcon_sciam3p6430b1.png?width=256&amp;s=7e050a598bd11f363d87de4bdd00f9f2fe06f2b2" alt="FreeNotionTemplates"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/notioncreations" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_6sssdf/styles/communityIcon_2m1bepvyrr2a1.png?width=256&amp;s=93d24abb0730fe917dbb87033bccb2d378d54794" alt="notioncreations"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-60e8175e2b-icon" data-tip="r/Notiontemplates" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3jj1vr/styles/communityIcon_h2c48cgoif461.png?width=256&amp;s=93f32b49db011d7667907f9c3a014459787e7fae" alt="Notiontemplates"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">English Learners</h2><div class="__react_component_tooltip t6a4292db-8378-4c9f-b8e7-1c766bd469d9 place-top type-dark" id="audience-card-f0c8c37989" data-id="tooltip"><style>
  	.t6a4292db-8378-4c9f-b8e7-1c766bd469d9 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-top {
        margin-top: -10px;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-bottom {
        margin-top: 10px;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-left {
        margin-left: -10px;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-right {
        margin-left: 10px;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6a4292db-8378-4c9f-b8e7-1c766bd469d9.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-f0c8c37989" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>8 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>3.0M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>5.77% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t5737b56d-bece-4dd8-9d6a-3246004cbd60 place-top type-dark" id="collection-f0c8c37989-icon" data-id="tooltip"><style>
  	.t5737b56d-bece-4dd8-9d6a-3246004cbd60 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-top {
        margin-top: -10px;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-top::before {
        border-top: 8px solid transparent;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-bottom {
        margin-top: 10px;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-left {
        margin-left: -10px;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-left::before {
        border-left: 8px solid transparent;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-right {
        margin-left: 10px;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-right::before {
        border-right: 8px solid transparent;
    }
    .t5737b56d-bece-4dd8-9d6a-3246004cbd60.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-f0c8c37989-icon" data-tip="r/EnglishStudy, r/LearnEnglishFree, r/Learn_English, r/learnEnglishOnline" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f0c8c37989-icon" data-tip="r/LearnEnglishOnReddit" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2ywxdk/styles/communityIcon_673uesq1c0g51.png?width=256&amp;s=1a34411475b8571d7d5bdb3fae314f6cf9f2e8de" alt="LearnEnglishOnReddit"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f0c8c37989-icon" data-tip="r/language_exchange" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2tdbm/styles/communityIcon_yfjvakd1flhc1.png?width=256&amp;s=1194d9c593f1cc2709fa18f568cfd27078a50910" alt="language_exchange"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f0c8c37989-icon" data-tip="r/EnglishLearning" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2u8ap/styles/communityIcon_sferz26yxuk81.png?width=256&amp;s=44ba5ccf0b11135d4339ef1994cc7056676f479b" alt="EnglishLearning"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f0c8c37989-icon" data-tip="r/languagelearning" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rjsc/styles/communityIcon_8w18xo3lyjv01.png?width=256&amp;s=4cc883a03f7ec2663da92cd03f01f7b1c2e5966c" alt="languagelearning"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Influencers</h2><div class="__react_component_tooltip t82784f18-c752-4dfe-97f8-0448fd92a132 place-top type-dark" id="audience-card-f6308134a8" data-id="tooltip"><style>
  	.t82784f18-c752-4dfe-97f8-0448fd92a132 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t82784f18-c752-4dfe-97f8-0448fd92a132.place-top {
        margin-top: -10px;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-top::before {
        border-top: 8px solid transparent;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-bottom {
        margin-top: 10px;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-left {
        margin-left: -10px;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-left::before {
        border-left: 8px solid transparent;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-right {
        margin-left: 10px;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-right::before {
        border-right: 8px solid transparent;
    }
    .t82784f18-c752-4dfe-97f8-0448fd92a132.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><span class="font-normal" data-for="audience-card-f6308134a8" data-tip="You have already saved this curated audience" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-f6308134a8" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>7 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>5.4M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>4.98% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t7f5dc8c2-409e-4b3c-a074-42511759e4a7 place-top type-dark" id="collection-f6308134a8-icon" data-id="tooltip"><style>
  	.t7f5dc8c2-409e-4b3c-a074-42511759e4a7 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-top {
        margin-top: -10px;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-top::before {
        border-top: 8px solid transparent;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-bottom {
        margin-top: 10px;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-left {
        margin-left: -10px;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-left::before {
        border-left: 8px solid transparent;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-right {
        margin-left: 10px;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-right::before {
        border-right: 8px solid transparent;
    }
    .t7f5dc8c2-409e-4b3c-a074-42511759e4a7.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-f6308134a8-icon" data-tip="r/SocialMediaMarketing" currentitem="false">+1</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/InstagramGrowthTips" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_27exdd/styles/communityIcon_obe6nugk3cv31.png?width=256&amp;s=e21086238482ddaebf285e4bb3477d0f6b8d4bdd" alt="InstagramGrowthTips"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/influencermarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3a10b/styles/communityIcon_hmnifniekxs91.png?width=256&amp;s=7126fcce550ffc0f5901d12432733e36a0e10943" alt="influencermarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/InstagramMarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://a.thumbs.redditmedia.com/JDkvH4BSYJQOZ93RZGUIVUjtEqi1T5WnhTyqeCtgUJ0.png" alt="InstagramMarketing"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/Instagram" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2seh9/styles/communityIcon_hybmyae0zqx31.png?width=256&amp;s=bab7f168561e04eb437858b9f6a8f9cfa5e5e9f8" alt="Instagram"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/socialmedia" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qi2m/styles/communityIcon_235yy63bdp7d1.jpeg?width=256&amp;s=20a4a42f1cf65d09ff25fae6311b5221cdf2f82f" alt="socialmedia"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-f6308134a8-icon" data-tip="r/BeautyGuruChatter" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3jayp/styles/communityIcon_38zcdzsbhrw51.png?width=256&amp;s=7222abe955d2fce961b15d935a122cad092e03b0" alt="BeautyGuruChatter"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">AirBnB Hosts</h2><div class="__react_component_tooltip t5d994455-cb35-40d0-9fb4-63850e382f3e place-top type-dark" id="audience-card-3f870dbedd" data-id="tooltip"><style>
  	.t5d994455-cb35-40d0-9fb4-63850e382f3e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t5d994455-cb35-40d0-9fb4-63850e382f3e.place-top {
        margin-top: -10px;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-top::before {
        border-top: 8px solid transparent;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-bottom {
        margin-top: 10px;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-left {
        margin-left: -10px;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-left::before {
        border-left: 8px solid transparent;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-right {
        margin-left: 10px;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-right::before {
        border-right: 8px solid transparent;
    }
    .t5d994455-cb35-40d0-9fb4-63850e382f3e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-3f870dbedd" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>99k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>4.08% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tea88ca70-e233-45dc-8ae0-c4368df47453 place-top type-dark" id="collection-3f870dbedd-icon" data-id="tooltip"><style>
  	.tea88ca70-e233-45dc-8ae0-c4368df47453 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tea88ca70-e233-45dc-8ae0-c4368df47453.place-top {
        margin-top: -10px;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-top::before {
        border-top: 8px solid transparent;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-bottom {
        margin-top: 10px;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-left {
        margin-left: -10px;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-left::before {
        border-left: 8px solid transparent;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-right {
        margin-left: 10px;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-right::before {
        border-right: 8px solid transparent;
    }
    .tea88ca70-e233-45dc-8ae0-c4368df47453.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-3f870dbedd-icon" data-tip="r/learnairbnb, r/ShortTermRentals" currentitem="false">+2</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3f870dbedd-icon" data-tip="r/AirBnBInvesting" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_4esos9/styles/communityIcon_37lfeku0bzy61.png?width=256&amp;s=af136b43fc1794567c297e6b209236d033f80b10" alt="AirBnBInvesting"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3f870dbedd-icon" data-tip="r/rentalproperties" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_266eel/styles/communityIcon_ac6uu0jxc6r31.png?width=256&amp;s=3ccd0a854a61258ae37ce99429eb1082afbb4893" alt="rentalproperties"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3f870dbedd-icon" data-tip="r/AirBnBHosts" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3gr14/styles/communityIcon_r40khuhdk8q41.png?width=256&amp;s=37c92df674ced47a3ed24e4c6f55e700ca1dc700" alt="AirBnBHosts"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-3f870dbedd-icon" data-tip="r/airbnb_hosts" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3ji5s/styles/communityIcon_ijwvhdlikzv41.png?width=256&amp;s=5602621652b8b7453be8bf2ca21593389056d649" alt="airbnb_hosts"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Advertisers</h2><div class="__react_component_tooltip tcb73187b-ee45-4290-97cb-afaa10c80c10 place-top type-dark" id="audience-card-44f804faa8" data-id="tooltip"><style>
  	.tcb73187b-ee45-4290-97cb-afaa10c80c10 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tcb73187b-ee45-4290-97cb-afaa10c80c10.place-top {
        margin-top: -10px;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-top::before {
        border-top: 8px solid transparent;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-bottom {
        margin-top: 10px;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-left {
        margin-left: -10px;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-left::before {
        border-left: 8px solid transparent;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-right {
        margin-left: 10px;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-right::before {
        border-right: 8px solid transparent;
    }
    .tcb73187b-ee45-4290-97cb-afaa10c80c10.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-44f804faa8" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>2.3M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>4.85% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t833b8b0c-fc91-4e96-a35d-01eaed6e4e39 place-top type-dark" id="collection-44f804faa8-icon" data-id="tooltip"><style>
  	.t833b8b0c-fc91-4e96-a35d-01eaed6e4e39 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-top {
        margin-top: -10px;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-top::before {
        border-top: 8px solid transparent;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-bottom {
        margin-top: 10px;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-left {
        margin-left: -10px;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-left::before {
        border-left: 8px solid transparent;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-right {
        margin-left: 10px;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-right::before {
        border-right: 8px solid transparent;
    }
    .t833b8b0c-fc91-4e96-a35d-01eaed6e4e39.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/googleads" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2rge2/styles/communityIcon_fz8ine75s1691.jpg?width=256&amp;s=fae821351de3e4f2e8b50c3dc95c9b0ffb07a133" alt="googleads"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/FacebookAds" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2yoxx/styles/communityIcon_2svbmovwqke71.png?width=256&amp;s=85abf0687654cb000d5ed8b9cd3738748aa2a691" alt="FacebookAds"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/PPC" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qvdk/styles/communityIcon_8f7jzfcbn5g21.png?width=256&amp;s=0b7fc84e606a639ff6a0f0982d850da2a286e899" alt="PPC"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/advertising" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhvy/styles/communityIcon_yoy1daa2pb7d1.jpg?width=256&amp;s=7f842276e2cd1d42222b51051440af3a52afa7da" alt="advertising"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/SEO" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhbx/styles/communityIcon_191l6xkqju6d1.png?width=256&amp;s=4a29285ca7e84a08e16e3dfdc3ebad5937e55f24" alt="SEO"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-44f804faa8-icon" data-tip="r/marketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qhmg/styles/communityIcon_amdb6rj8w5p31.png?width=256&amp;s=61b2f220cfc6548e3e29f3611c79b3770d35d9c2" alt="marketing"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Remote Workers</h2><div class="__react_component_tooltip t75a570bd-52b6-4d21-852f-5446442febad place-top type-dark" id="audience-card-581c0e8e3e" data-id="tooltip"><style>
  	.t75a570bd-52b6-4d21-852f-5446442febad {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t75a570bd-52b6-4d21-852f-5446442febad.place-top {
        margin-top: -10px;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-top::before {
        border-top: 8px solid transparent;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t75a570bd-52b6-4d21-852f-5446442febad.place-bottom {
        margin-top: 10px;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t75a570bd-52b6-4d21-852f-5446442febad.place-left {
        margin-left: -10px;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-left::before {
        border-left: 8px solid transparent;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t75a570bd-52b6-4d21-852f-5446442febad.place-right {
        margin-left: 10px;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-right::before {
        border-right: 8px solid transparent;
    }
    .t75a570bd-52b6-4d21-852f-5446442febad.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-581c0e8e3e" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>3.4M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.39% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t4f988514-a567-4347-8faa-eca076f3c27c place-top type-dark" id="collection-581c0e8e3e-icon" data-id="tooltip"><style>
  	.t4f988514-a567-4347-8faa-eca076f3c27c {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t4f988514-a567-4347-8faa-eca076f3c27c.place-top {
        margin-top: -10px;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-top::before {
        border-top: 8px solid transparent;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t4f988514-a567-4347-8faa-eca076f3c27c.place-bottom {
        margin-top: 10px;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t4f988514-a567-4347-8faa-eca076f3c27c.place-left {
        margin-left: -10px;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-left::before {
        border-left: 8px solid transparent;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t4f988514-a567-4347-8faa-eca076f3c27c.place-right {
        margin-left: 10px;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-right::before {
        border-right: 8px solid transparent;
    }
    .t4f988514-a567-4347-8faa-eca076f3c27c.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-581c0e8e3e-icon" data-tip="r/workfromhome, r/work, r/remotework, r/WorkOnline, r/digitalnomad" currentitem="false">+5</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-581c0e8e3e-icon" data-tip="r/RemoteJobs" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2vs4i/styles/communityIcon_1o7vv6nka5ra1.jpg?width=256&amp;s=3ea771dbecbb7567df62a47daa03a00996c96bf3" alt="RemoteJobs"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Productivity</h2><div class="__react_component_tooltip t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe place-top type-dark" id="audience-card-523ca5f33d" data-id="tooltip"><style>
  	.t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-top {
        margin-top: -10px;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-top::before {
        border-top: 8px solid transparent;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-bottom {
        margin-top: 10px;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-left {
        margin-left: -10px;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-left::before {
        border-left: 8px solid transparent;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-right {
        margin-left: 10px;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-right::before {
        border-right: 8px solid transparent;
    }
    .t6d28ee52-35c2-4e43-bbeb-f5e9c5ea79fe.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><span class="font-normal" data-for="audience-card-523ca5f33d" data-tip="You have already saved this curated audience" currentitem="false"><svg xmlns="http://www.w3.org/2000/svg" class="ml-2 h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-523ca5f33d" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>41.6M Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>0.96% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t164d6403-a1aa-4be0-abb6-a701e8bf4ae8 place-top type-dark" id="collection-523ca5f33d-icon" data-id="tooltip"><style>
  	.t164d6403-a1aa-4be0-abb6-a701e8bf4ae8 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-top {
        margin-top: -10px;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-top::before {
        border-top: 8px solid transparent;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-bottom {
        margin-top: 10px;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-left {
        margin-left: -10px;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-left::before {
        border-left: 8px solid transparent;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-right {
        margin-left: 10px;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-right::before {
        border-right: 8px solid transparent;
    }
    .t164d6403-a1aa-4be0-abb6-a701e8bf4ae8.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-523ca5f33d-icon" data-tip="r/LifeHack_Pro, r/lifehack" currentitem="false">+2</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-523ca5f33d-icon" data-tip="r/getdisciplined" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2uzju/styles/communityIcon_488kxisiiao41.png?width=256&amp;s=494abe83422de27f9fe2c23070ee2a8c02342f1c" alt="getdisciplined"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-523ca5f33d-icon" data-tip="r/productivity" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qh1k/styles/communityIcon_fumtbs2jry381.png?width=256&amp;s=707805616ae19292886d7b23b456b5891d2ae181" alt="productivity"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-523ca5f33d-icon" data-tip="r/lifehacks" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qj5n/styles/communityIcon_japcsnjgfog91.png?width=256&amp;s=394d92a1f031ce92612990acefdf1ee40e20883d" alt="lifehacks"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-523ca5f33d-icon" data-tip="r/LifeProTips" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2s5oq/styles/communityIcon_vkdkb2aoisi91.jpg?width=256&amp;s=17b646ba8e259382e30db1ee87734700a40da250" alt="LifeProTips"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Product Managers</h2><div class="__react_component_tooltip td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf place-top type-dark" id="audience-card-b3369d6fa8" data-id="tooltip"><style>
  	.td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-top {
        margin-top: -10px;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-top::before {
        border-top: 8px solid transparent;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-bottom {
        margin-top: 10px;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-left {
        margin-left: -10px;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-left::before {
        border-left: 8px solid transparent;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-right {
        margin-left: 10px;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-right::before {
        border-right: 8px solid transparent;
    }
    .td12c673e-5aaa-43ac-badb-a8e9e7fbdeaf.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-b3369d6fa8" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>207k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.41% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tc6c7008d-1fe6-40b8-9a00-a990b137b885 place-top type-dark" id="collection-b3369d6fa8-icon" data-id="tooltip"><style>
  	.tc6c7008d-1fe6-40b8-9a00-a990b137b885 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-top {
        margin-top: -10px;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-top::before {
        border-top: 8px solid transparent;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-bottom {
        margin-top: 10px;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-left {
        margin-left: -10px;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-left::before {
        border-left: 8px solid transparent;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-right {
        margin-left: 10px;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-right::before {
        border-right: 8px solid transparent;
    }
    .tc6c7008d-1fe6-40b8-9a00-a990b137b885.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-b3369d6fa8-icon" data-tip="r/Product_Management, r/ProductManager, r/ProductOwner, r/prodmgmt" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-b3369d6fa8-icon" data-tip="r/ProductMgmt" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_25x3yu/styles/communityIcon_nnted5xx8wl51.jpg?width=256&amp;s=4c6a5fe258b41e6b872f018734e82f8c48af5396" alt="ProductMgmt"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-b3369d6fa8-icon" data-tip="r/ProductManagement" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r8ul/styles/communityIcon_ns0x5ubrfvc61.jpeg?width=256&amp;s=569b78c2829110fa08ae8ad7dfb65cdf64adab73" alt="ProductManagement"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">SaaS founders</h2><div class="__react_component_tooltip t024c78e9-9702-44b0-b762-d384954ebf7c place-top type-dark" id="audience-card-fd62e6dd1b" data-id="tooltip"><style>
  	.t024c78e9-9702-44b0-b762-d384954ebf7c {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t024c78e9-9702-44b0-b762-d384954ebf7c.place-top {
        margin-top: -10px;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-top::before {
        border-top: 8px solid transparent;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-bottom {
        margin-top: 10px;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-left {
        margin-left: -10px;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-left::before {
        border-left: 8px solid transparent;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-right {
        margin-left: 10px;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-right::before {
        border-right: 8px solid transparent;
    }
    .t024c78e9-9702-44b0-b762-d384954ebf7c.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-fd62e6dd1b" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>6 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>204k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>7.74% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t0036503e-84f8-4ad9-a260-76904e19e92b place-top type-dark" id="collection-fd62e6dd1b-icon" data-id="tooltip"><style>
  	.t0036503e-84f8-4ad9-a260-76904e19e92b {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t0036503e-84f8-4ad9-a260-76904e19e92b.place-top {
        margin-top: -10px;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-top::before {
        border-top: 8px solid transparent;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-bottom {
        margin-top: 10px;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-left {
        margin-left: -10px;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-left::before {
        border-left: 8px solid transparent;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-right {
        margin-left: 10px;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-right::before {
        border-right: 8px solid transparent;
    }
    .t0036503e-84f8-4ad9-a260-76904e19e92b.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-fd62e6dd1b-icon" data-tip="r/B2BSaaS, r/SaaS_Email_Marketing, r/NoCodeSaaS, r/SaaSSales" currentitem="false">+4</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-fd62e6dd1b-icon" data-tip="r/microsaas" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3n8ao/styles/communityIcon_jffqvvq8o2i91.png?width=256&amp;s=2d8f4fc5cf30383b025c22b077bf5d6c985dc952" alt="microsaas"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-fd62e6dd1b-icon" data-tip="r/SaaS" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qkq6/styles/communityIcon_u7ddkuay2xn21.jpg?width=256&amp;s=9054f6d63f23825552de4bd6f31328716775e412" alt="SaaS"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">B2B Sales</h2><div class="__react_component_tooltip tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e place-top type-dark" id="audience-card-ff1a70be65" data-id="tooltip"><style>
  	.tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-top {
        margin-top: -10px;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-top::before {
        border-top: 8px solid transparent;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-bottom {
        margin-top: 10px;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-left {
        margin-left: -10px;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-left::before {
        border-left: 8px solid transparent;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-right {
        margin-left: 10px;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-right::before {
        border-right: 8px solid transparent;
    }
    .tfc5f99f2-3ee4-44a2-8769-e5809e1e6a6e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-ff1a70be65" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>5 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>390k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>2.30% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip tca88f177-6505-4b9f-aae1-0225d558ad96 place-top type-dark" id="collection-ff1a70be65-icon" data-id="tooltip"><style>
  	.tca88f177-6505-4b9f-aae1-0225d558ad96 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tca88f177-6505-4b9f-aae1-0225d558ad96.place-top {
        margin-top: -10px;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-top::before {
        border-top: 8px solid transparent;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-bottom {
        margin-top: 10px;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-left {
        margin-left: -10px;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-left::before {
        border-left: 8px solid transparent;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-right {
        margin-left: 10px;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-right::before {
        border-right: 8px solid transparent;
    }
    .tca88f177-6505-4b9f-aae1-0225d558ad96.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ff1a70be65-icon" data-tip="r/B_2_B_Selling_Tips" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_4ccefr/styles/communityIcon_zor2zcfmapw61.png?width=256&amp;s=6054c66a68373e969130c2891b1835ee55b75362" alt="B_2_B_Selling_Tips"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ff1a70be65-icon" data-tip="r/B2BSales" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2sb35/styles/communityIcon_k171yid76ok21.png?width=256&amp;s=b24f007957c8b9ce4d013246e4d9458a6e4c274a" alt="B2BSales"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ff1a70be65-icon" data-tip="r/b2b_sales" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3bphg/styles/communityIcon_jr9s7ybv5xd91.jpg?width=256&amp;s=966aa7a81db0684066c4bf04653fd6c593dc2c1a" alt="b2b_sales"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ff1a70be65-icon" data-tip="r/salestechniques" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_37pu1/styles/communityIcon_lui1pwaucuid1.jpg?width=256&amp;s=0d37706488994eaa6996d71456d2465b20fb2bc5" alt="salestechniques"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-ff1a70be65-icon" data-tip="r/sales" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2qib3/styles/communityIcon_9zu1p9ie3ljc1.png?width=256&amp;s=d4f801c12556ffce512a7bc154a0f8089402db4b" alt="sales"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Restaurant Owners</h2><div class="__react_component_tooltip tf2a544a3-6858-45b2-a7c6-181f69d2db03 place-top type-dark" id="audience-card-043ed919e0" data-id="tooltip"><style>
  	.tf2a544a3-6858-45b2-a7c6-181f69d2db03 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-top {
        margin-top: -10px;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-top::before {
        border-top: 8px solid transparent;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-bottom {
        margin-top: 10px;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-left {
        margin-left: -10px;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-left::before {
        border-left: 8px solid transparent;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-right {
        margin-left: 10px;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-right::before {
        border-right: 8px solid transparent;
    }
    .tf2a544a3-6858-45b2-a7c6-181f69d2db03.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-043ed919e0" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>4 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>222k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>1.40% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t9e562f5f-5504-44ec-a5d3-5bd58f406b2e place-top type-dark" id="collection-043ed919e0-icon" data-id="tooltip"><style>
  	.t9e562f5f-5504-44ec-a5d3-5bd58f406b2e {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-top {
        margin-top: -10px;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-top::before {
        border-top: 8px solid transparent;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-bottom {
        margin-top: 10px;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-left {
        margin-left: -10px;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-left::before {
        border-left: 8px solid transparent;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-right {
        margin-left: 10px;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-right::before {
        border-right: 8px solid transparent;
    }
    .t9e562f5f-5504-44ec-a5d3-5bd58f406b2e.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-700 h-12 w-12 text-center py-3.5 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:bg-gray-600 group-hover:border-gray-700 relative text-xs text-gray-400 font-semibold" data-for="collection-043ed919e0-icon" data-tip="r/restaurateur, r/restaurant" currentitem="false">+2</div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-043ed919e0-icon" data-tip="r/BarOwners" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_9d2i5/styles/communityIcon_zqkv7xry4c5a1.png?width=256&amp;s=61cbd66e911c19a9a903e20f5c5771a651fa0312" alt="BarOwners"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-043ed919e0-icon" data-tip="r/restaurantowners" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_3240z/styles/communityIcon_tk86gcth8mc41.jpg?width=256&amp;s=83421c90074d7c0369b6e215f6a3625decedbb67" alt="restaurantowners"></div></div></dd></div></div><div class="group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col"><div class="flex items-center"><h2 class="text-xl font-semibold mr-auto">Newsletter Creators</h2><div class="__react_component_tooltip t4173517e-8328-4e52-88bc-f6142d3180d7 place-top type-dark" id="audience-card-e6d089365f" data-id="tooltip"><style>
  	.t4173517e-8328-4e52-88bc-f6142d3180d7 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t4173517e-8328-4e52-88bc-f6142d3180d7.place-top {
        margin-top: -10px;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-top::before {
        border-top: 8px solid transparent;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-bottom {
        margin-top: 10px;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-left {
        margin-left: -10px;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-left::before {
        border-left: 8px solid transparent;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-right {
        margin-left: 10px;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-right::before {
        border-right: 8px solid transparent;
    }
    .t4173517e-8328-4e52-88bc-f6142d3180d7.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="ml-2 h-6 w-6 flex-shrink-0 text-gray-500" data-for="audience-card-e6d089365f" data-tip="Curated by GummySearch" currentItem="false"><path stroke-linecap="round" stroke-linejoin="round" d="M4.098 19.902a3.75 3.75 0 005.304 0l6.401-6.402M6.75 21A3.75 3.75 0 013 17.25V4.125C3 3.504 3.504 3 4.125 3h5.25c.621 0 1.125.504 1.125 1.125v4.072M6.75 21a3.75 3.75 0 003.75-3.75V8.197M6.75 21h13.125c.621 0 1.125-.504 1.125-1.125v-5.25c0-.621-.504-1.125-1.125-1.125h-4.072M10.5 8.197l2.88-2.88c.438-.439 1.15-.439 1.59 0l3.712 3.713c.44.44.44 1.152 0 1.59l-2.879 2.88M6.75 17.25h.008v.008H6.75v-.008z"></path></svg></div><div class=""><div class="mt-2 flex sm:space-x-4 text-xs"><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" enable-background="new 0 0 24 24" height="512" fill="currentColor" viewBox="0 0 24 24" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m21.325 9.308c-.758 0-1.425.319-1.916.816-1.805-1.268-4.239-2.084-6.936-2.171l1.401-6.406 4.461 1.016c0 1.108.89 2.013 1.982 2.013 1.113 0 2.008-.929 2.008-2.038s-.889-2.038-2.007-2.038c-.779 0-1.451.477-1.786 1.129l-4.927-1.108c-.248-.067-.491.113-.557.365l-1.538 7.062c-2.676.113-5.084.928-6.895 2.197-.491-.518-1.184-.837-1.942-.837-2.812 0-3.733 3.829-1.158 5.138-.091.405-.132.837-.132 1.268 0 4.301 4.775 7.786 10.638 7.786 5.888 0 10.663-3.485 10.663-7.786 0-.431-.045-.883-.156-1.289 2.523-1.314 1.594-5.115-1.203-5.117zm-15.724 5.41c0-1.129.89-2.038 2.008-2.038 1.092 0 1.983.903 1.983 2.038 0 1.109-.89 2.013-1.983 2.013-1.113.005-2.008-.904-2.008-2.013zm10.839 4.798c-1.841 1.868-7.036 1.868-8.878 0-.203-.18-.203-.498 0-.703.177-.18.491-.18.668 0 1.406 1.463 6.07 1.488 7.537 0 .177-.18.491-.18.668 0 .207.206.207.524.005.703zm-.041-2.781c-1.092 0-1.982-.903-1.982-2.011 0-1.129.89-2.038 1.982-2.038 1.113 0 2.008.903 2.008 2.038-.005 1.103-.895 2.011-2.008 2.011z"></path></svg>3 Subs</div><div class="flex items-center text-gray-300"><svg class="h-4 w-4 mr-1 opacity-25" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>86k Users</div><div class="flex text-gray-400"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="h-4 w-4 mr-1"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path></svg><div>4.08% /mo</div></div></div><dd class="flex justify-between items-baseline md:block"><div class="__react_component_tooltip t26bbff0e-5655-4ffe-9511-a928a01189d1 place-top type-dark" id="collection-e6d089365f-icon" data-id="tooltip"><style>
  	.t26bbff0e-5655-4ffe-9511-a928a01189d1 {
	    color: #fff;
	    background: #222;
	    border: 1px solid transparent;
  	}

  	.t26bbff0e-5655-4ffe-9511-a928a01189d1.place-top {
        margin-top: -10px;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-top::before {
        border-top: 8px solid transparent;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-top::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        bottom: -6px;
        left: 50%;
        margin-left: -8px;
        border-top-color: #222;
        border-top-style: solid;
        border-top-width: 6px;
    }

    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-bottom {
        margin-top: 10px;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-bottom::before {
        border-bottom: 8px solid transparent;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-bottom::after {
        border-left: 8px solid transparent;
        border-right: 8px solid transparent;
        top: -6px;
        left: 50%;
        margin-left: -8px;
        border-bottom-color: #222;
        border-bottom-style: solid;
        border-bottom-width: 6px;
    }

    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-left {
        margin-left: -10px;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-left::before {
        border-left: 8px solid transparent;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-left::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        right: -6px;
        top: 50%;
        margin-top: -4px;
        border-left-color: #222;
        border-left-style: solid;
        border-left-width: 6px;
    }

    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-right {
        margin-left: 10px;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-right::before {
        border-right: 8px solid transparent;
    }
    .t26bbff0e-5655-4ffe-9511-a928a01189d1.place-right::after {
        border-top: 5px solid transparent;
        border-bottom: 5px solid transparent;
        left: -6px;
        top: 50%;
        margin-top: -4px;
        border-right-color: #222;
        border-right-style: solid;
        border-right-width: 6px;
    }
  </style></div><div class="flex flex-wrap mt-2 flex-row-reverse justify-end pr-4"><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e6d089365f-icon" data-tip="r/Newsletters" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_363kz/styles/communityIcon_pysnhcb5t6ka1.jpg?width=256&amp;s=0526cfe99a76e9f48eb412d1985e9e3ddaf9cd77" alt="Newsletters"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e6d089365f-icon" data-tip="r/Substack" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_13ecxt/styles/communityIcon_l59tckjbg7t61.png?width=256&amp;s=f88590220b588b030bc4784551e2fb81df7d4a13" alt="Substack"></div><div class="bg-gray-600 shadow-sm h-12 w-12 p-1 rounded-md -mr-4 border-2 border-solid border-gray-800 group-hover:border-gray-700 relative" data-for="collection-e6d089365f-icon" data-tip="r/Emailmarketing" currentitem="false"><img class="h-full w-full rounded-sm" src="https://styles.redditmedia.com/t5_2r1yx/styles/communityIcon_k1li29utju8a1.png?width=256&amp;s=492b3bde8bd185ea9a377390a01e81d6de9d1f25" alt="Emailmarketing"></div></div></dd></div></div></div></div></div></div></div><div></div></div></main></div></div><script>!function(e){function r(r){for(var n,l,a=r[0],f=r[1],i=r[2],p=0,s=[];p<a.length;p++)l=a[p],Object.prototype.hasOwnProperty.call(o,l)&&o[l]&&s.push(o[l][0]),o[l]=0;for(n in f)Object.prototype.hasOwnProperty.call(f,n)&&(e[n]=f[n]);for(c&&c(r);s.length;)s.shift()();return u.push.apply(u,i||[]),t()}function t(){for(var e,r=0;r<u.length;r++){for(var t=u[r],n=!0,a=1;a<t.length;a++){var f=t[a];0!==o[f]&&(n=!1)}n&&(u.splice(r--,1),e=l(l.s=t[0]))}return e}var n={},o={1:0},u=[];function l(r){if(n[r])return n[r].exports;var t=n[r]={i:r,l:!1,exports:{}};return e[r].call(t.exports,t,t.exports,l),t.l=!0,t.exports}l.m=e,l.c=n,l.d=function(e,r,t){l.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:t})},l.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},l.t=function(e,r){if(1&r&&(e=l(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var t=Object.create(null);if(l.r(t),Object.defineProperty(t,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var n in e)l.d(t,n,function(r){return e[r]}.bind(null,n));return t},l.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return l.d(r,"a",r),r},l.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},l.p="/";var a=this["webpackJsonpgummy-search"]=this["webpackJsonpgummy-search"]||[],f=a.push.bind(a);a.push=r,a=a.slice();for(var i=0;i<a.length;i++)r(a[i]);var c=f;t()}([])</script><script src="/static/js/2.30e0d8f0.chunk.js"></script><script src="/static/js/main.d9783d95.chunk.js"></script><ck-widget vce-ready=""><div class="ck-style"><!----><!----></div></ck-widget><ck-pause-wall vce-ready=""><!----></ck-pause-wall><ck-failed-payment-wall vce-ready=""><!----></ck-failed-payment-wall><ck-managed-flow vce-ready=""><!----></ck-managed-flow></body></html>
"""

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

group = soup.findAll('div', class_='group bg-gray-800 hover:bg-gray-700 rounded-md shadow-md cursor-pointer text-white flex p-4 flex-col')

results = []

for g in group:
    soup = BeautifulSoup(str(g), 'html.parser')
    # Extract the group name
    group_name = soup.find('h2', class_='text-xl').text

    # Extract all subreddit names
    subreddits = []
    tooltip_divs = soup.find_all('div', {'data-tip': True})

    for div in tooltip_divs:
        data_tip = div['data-tip']
        subreddits.extend([sub.strip() for sub in data_tip.split(',')])

    # Create the JSON result
    result = {
        'groupName': group_name,
        'subreddits': subreddits
    }

    results.append(result)

# Save the results to groupsAndSubreddits.json
with open('groupsAndSubreddits.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Results have been saved to groupsAndSubreddits.json")