import os
import tweepy
import re
import time
import locale
import asyncio
import pandas as pd
import dataframe_image as dfi
import csv
from datetime import date
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import time
import pyppeteer
from pyppeteer import launch
# need to put starting location same as the directory of the file
# if running with the Windows task scheduler

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
async def main():
    browser = await launch()

    stakedList = []
    stakedStrList = []
    apyList = []

    poolList = [
    'Gemini',
    'Spedn',
    'Bitcoin',
    'Bitcoin Cash',
    'Cardano',
    'Celo',
    'Dogecoin',
    'Ethereum',
    'Lightning',
    'Litecoin',
    'Polygon',
    'Solana',
    'Tezos',
    'Zcash'
    ]

    urlList = [
    'app/gemini',
    'app/spedn',
    'transformer/bitcoin',
    'transformer/bitcoin-cash',
    'transformer/cardano',
    'transformer/celo',
    'transformer/dogecoin',
    'transformer/ethereum',
    'transformer/lightning',
    'transformer/litecoin',
    'transformer/polygon',
    'transformer/solana',
    'transformer/tezos',
    'transformer/zcash'
    ]
    

    # Amount staked per pool
    for url in urlList:
        page = await browser.newPage()
        siteURL = 'https://app.flexa.network/explore/' + url
        await page.goto(siteURL)
        time.sleep(11)
        element = await page.querySelector(".css-i3vmyo")
        title = await page.evaluate('(element) => element.textContent', element)
        Staked = re.search("(?s)(?<=currently ).*?(?= of)", title)
        Staked = Staked.group(0)
        # print("Total Staked on Gemini: " + geminiStaked)
        StakedStr = Staked
        Staked = Staked.replace(",", "")
        Staked = float(Staked)
        stakedList.append(Staked)
        stakedStrList.append(StakedStr)

    
    
    # APY Percentages
    time.sleep(17)
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/account/supply')
    element = await page.querySelectorAll(".css-1bvmc47")

    for x in range(14):
        tempAPY = await page.evaluate('(element) => element.textContent', element[x])
        tempAPY = tempAPY.replace("APY", "")

        apyList.append(tempAPY)


    # Pulls the current circ supply from the website
    page = await browser.newPage()
    time.sleep(11)
    await page.goto('https://amptoken.org/metrics/circulating-supply/')
    element = await page.querySelector("pre")
    title = await page.evaluate('(element) => element.textContent', element)
    totalCircTokens = float(title)
    totalCircTokensFormatted = locale.format_string("%d", totalCircTokens, grouping=True)
    
    # Calculating Staked Stats
    totalTokensStaked = sum(stakedList)
    totalTokensStakedFormatted = locale.format_string("%d", totalTokensStaked, grouping=True)


    stakedPercentage = (((totalTokensStaked)/totalCircTokens)*100)
    stakedPercentage = round(stakedPercentage,2)
    stakedPercentageStr = str(stakedPercentage)

    lastStakedValue = 1 # placeholder
    # read
    readFile = open("lastStaked.txt", 'r')
    for line in readFile:
        lastStakedValue = line

    # write
    myfile = open("lastStaked.txt", 'w')
    myfile.write(str(totalTokensStaked))

    current = totalTokensStaked
    difference = current  - int(float(lastStakedValue)) 
    



    # negative
    if difference < 0:
        difference = difference * -1 
        stakedChangeStr = locale.format_string("%d", difference, grouping=True)
        tweet12 = "\nChange in amount staked in the past hour: \nDecreased by " + stakedChangeStr + " ₳\n"
    # positive
    elif difference >= 0:
        stakedChangeStr = locale.format_string("%d", difference, grouping=True)
        tweet12 = "\nChange in amount staked in the past hour: \nIncreased by " + stakedChangeStr + " ₳\n"


    # tweet10 = "Tokens staked out of the circulating supply: \n" + totalTokensStakedFormatted + " ₳ / " + totalCircTokensFormatted + " ₳"
    # tweet11 = "\n\nTotal Staked Percentage: " + stakedPercentageStr + "%\n"+ "$AMP #flexa #amp"

    
    # tweetText = (tweet10 + tweet12 + tweet11) # with difference
    # tweetText = (tweet10 + tweet11) # without difference

    

    currentTime = time.time()
    currentTime = int(currentTime)
    currentTime = str(currentTime)
    now = datetime.now() # current date and time
    currentTime = now.strftime("%m%d%Y_%H%M")
    # img.save('./image/{}.png'.format(currentTime))


    
    df = pd.DataFrame(
                    {'Pool': poolList,
                   'APY':apyList,
                   '     Amount of AMP Staked': stakedStrList

                   }
                   
                   )
 
    dfi.export(df, './image/{}.png'.format(currentTime))

    time.sleep(6)





    # authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    # authenticator.set_access_token(access_token, access_token_secret)

    # api = tweepy.API(authenticator, wait_on_rate_limit=True)

    # # upload image
    # media = api.media_upload('./image/{}.png'.format(currentTime))

    # # post tweet with image
    # api.update_status(status=tweetText,media_ids=[media.media_id])

    dateCurr = date.today()
    dateCurr = dateCurr.strftime("%m/%d/%y")

    timeCurr = datetime.now()
    timeCurr = timeCurr.strftime("%H:%M")
    
        # Date,Time,Spedn,Gemini,Lightning,SpednAPY,GeminiAPY,LightningAPY
    with open("./capacityStats.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([
        dateCurr, timeCurr,  
        stakedStrList[0],apyList[0],
        stakedStrList[1],apyList[1],
        stakedStrList[2],apyList[2],
        stakedStrList[3],apyList[3],
        stakedStrList[4],apyList[4],
        stakedStrList[5],apyList[5],
        stakedStrList[6],apyList[6],
        stakedStrList[7],apyList[7],
        stakedStrList[8],apyList[8],
        stakedStrList[9],apyList[9],
        stakedStrList[10],apyList[10],
        stakedStrList[11],apyList[11],
        stakedStrList[12],apyList[12],
        stakedStrList[13],apyList[13]
        ])
    await page.close()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
