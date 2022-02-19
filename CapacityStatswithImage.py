import os
import tweepy
import tkinter
import re
import time
import locale
import asyncio
from PIL import Image, ImageDraw, ImageFont
import time
import pyppeteer
from pyppeteer import launch
# need to put starting location same as the directory of the file
# if running with the Windows task scheduler

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

    # APY Percentages
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/account/supply')
    time.sleep(7)
    element = await page.querySelectorAll(".css-1bvmc47")
    geminiAPY = await page.evaluate('(element) => element.textContent', element[0])
    spednAPY = await page.evaluate('(element) => element.textContent', element[1])
    lightningAPY = await page.evaluate('(element) => element.textContent', element[2])
    
    geminiAPY = geminiAPY.replace("APY", "")
    spednAPY = spednAPY.replace("APY", "")
    lightningAPY =lightningAPY.replace("APY", "")



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

    
    # tweet1 = "                              Flexa Capacity Stats\n\n"
    # tweet2 = "Staked on Gemini: " + geminiStakedStr  + " ₳\n" + "APY on Gemini: "  + geminiAPY
    # tweet3 = "\n\nStaked on Spedn: " + spednStakedstr + " ₳\n" + "APY on Spedn: "  + spednAPY
    # tweet4 = "\n\nStaked on Lightning: " + lightningStakedStr + " ₳\n" + "APY on Lightning: "  + lightningAPY
    # tweet5 = "Tokens staked out of the circulating supply: \n" + totalTokensStakedFormatted + " ₳ / " + totalCircTokensFormatted + " ₳"
    # tweet6 = "\n\nTotal Staked Percentage: " + stakedPercentageStr + "%\n"+ "$AMP #flexa #amp"
    
    
    tweet1 = "                              Flexa Capacity Stats\n\n"
    tweet2 =   "    Pool                 APY                Amount of AMP Staked                       \n"
    tweet2_5 = " -----------         ----------          ----------------------------------                 \n"
    tweet2_75 = "   Spedn             " + spednAPY + "                 "  +spednStakedstr +  " ₳\n\n" 
    tweet3 = "  Gemini            " + geminiAPY + "                 "  +geminiStakedStr +  " ₳\n\n" 
    tweet4 = " Lightning         " + lightningAPY + "                  "  +lightningStakedStr +  " ₳\n\n" 
    tweet5 = "Tokens staked out of the circulating supply: \n" + totalTokensStakedFormatted + " ₳ / " + totalCircTokensFormatted + " ₳"
    tweet6 = "\n\nTotal Staked Percentage: " + stakedPercentageStr + "%\n"+ "$AMP #flexa #amp"

    tweet = (tweet1 + tweet2 + tweet2_5 + tweet2_75 + tweet3 + tweet4)
    tweetText = (tweet5 + tweet6)


    # https://python.plainenglish.io/generating-text-on-image-with-python-eefe4430fe77
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    width = 512
    height = 305
    img = Image.new('RGB', (width, height), color='black')
    fnt = ImageFont.truetype("NotoSans-Regular.ttf", 20)
    imgDraw = ImageDraw.Draw(img)

    imgDraw.text((10, 10), tweet,font=fnt, fill=(255, 255, 255))

    currentTime = time.time()
    currentTime = int(currentTime)
    currentTime = str(currentTime)

    img.save('{}.png'.format(currentTime))
    exit()
    time.sleep(3)

    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    api = tweepy.API(authenticator, wait_on_rate_limit=True)

    # upload image
    media = api.media_upload('{}.png'.format(currentTime))

    # post tweet with image
    api.update_status(status=tweetText,media_ids=[media.media_id])



    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
