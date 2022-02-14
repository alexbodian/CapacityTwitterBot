import os
import tweepy
import tkinter
import re
import time
import locale
import asyncio
import time
import pyppeteer
from pyppeteer import launch


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
async def main():
    browser = await launch()

    # Gemini Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/app/gemini')
    time.sleep(7)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    geminiStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    geminiStaked = geminiStaked.group(0)
    # print("Total Staked on Gemini: " + geminiStaked)
    geminiStakedStr = geminiStaked
    geminiStaked = geminiStaked.replace(",", "")
    geminiStaked = float(geminiStaked)
    
    # # Spedn Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/app/spedn')
    time.sleep(7)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    spednStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    spednStaked = spednStaked.group(0)
    spednStakedstr = spednStaked
    # print("Total Staked on Spedn: " + spednStaked)
    spednStaked = spednStaked.replace(",", "")
    spednStaked = float(spednStaked)


    # # Lightning Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/lightning')
    time.sleep(7)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    lightningStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    lightningStaked = lightningStaked.group(0)
    lightningStakedStr = lightningStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    lightningStaked = lightningStaked.replace(",", "")
    lightningStaked = float(lightningStaked)

    # Pulls the current circ supply from the website
    page = await browser.newPage()
    time.sleep(2)
    await page.goto('https://amptoken.org/metrics/circulating-supply/')
    element = await page.querySelector("pre")
    title = await page.evaluate('(element) => element.textContent', element)
    totalCircTokens = float(title)
    totalCircTokensFormatted = locale.format_string("%d", totalCircTokens, grouping=True)
    
    
    totalTokensStaked = geminiStaked+spednStaked+lightningStaked
    totalTokensStakedFormatted = locale.format_string("%d", totalTokensStaked, grouping=True)


    stakedPercentage = (((geminiStaked+spednStaked+lightningStaked)/totalCircTokens)*100)
    stakedPercentage = round(stakedPercentage,2)
    stakedPercentageStr = str(stakedPercentage)
    # print("Total number of tokens staked out of circulating supply: " + totalTokensStakedFormatted + " / " + totalCircTokensFormatted)
    # print("Total Staked Percentage: " + stakedPercentageStr + "%")

    
    tweet1 = "Flexa Capacity Stats\n"
    tweet2 = "Total Staked on Gemini: " + geminiStakedStr  
    tweet3 = "\nTotal Staked on Spedn: " + spednStakedstr 
    tweet4 = "\nTotal Staked on Lightning: " + lightningStakedStr
    tweet5 = "\nTotal number of tokens staked out of circulating supply: " + totalTokensStakedFormatted + " / " + totalCircTokensFormatted 
    tweet6 = "\nTotal Staked Percentage: " + stakedPercentageStr + "%"

    tweet = (tweet1 + tweet2 + tweet3 + tweet4 + tweet5 + tweet6)

    
    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    api = tweepy.API(authenticator, wait_on_rate_limit=True)

    api.update_status(tweet)



    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
