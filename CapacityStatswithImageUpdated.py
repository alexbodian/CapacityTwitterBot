import os
import tweepy
import re
import time
import locale
import asyncio
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
    '''
    0   Gemini
    1   Spedn
    2   Bitcoin
    3   Bitcoin Cash
    4   Cardano
    5   Celo
    6   Dogecoin
    7   Ethereum
    8   Lightning
    9   Litecoin
    10  Polygon
    11  Solana
    12  Tezos
    13  Zcash
    '''


    page = await browser.newPage()
    await page.goto('https://app.flexa.network/account/supply')
    time.sleep(17)
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

        '''
    0   Gemini
    1   Spedn
    2   Bitcoin
    3   Bitcoin Cash
    4   Cardano
    5   Celo
    6   Dogecoin
    7   Ethereum
    8   Lightning
    9   Litecoin
    10  Polygon
    11  Solana
    12  Tezos
    13  Zcash
    '''
    
    # tweet1 = "                              Flexa Capacity Stats\n\n"
    # tweet2 =   "    Pool                 APY                Amount of AMP Staked                       \n"
    # tweet2_5 = " -----------         ----------          ----------------------------------                 \n"
    # tweet3 = "   Gemini           " + geminiAPY + "                 "  +geminiStakedStr +  " ₳\n\n"
    # tweet3_5 = "   Spedn             " + spednAPY + "                 "  +spednStakedstr +  " ₳\n\n"
    # tweet4 = "   Bitcoin             " + bitcoinAPY + "                 "  +bitcoinStakedStr +  " ₳\n\n"
    # tweet4_5 = "   Bitcoin Cash     " + bitcoincashAPY + "                 "  +bitcoincashStakedStr +  " ₳\n\n"
    # tweet5 = "   Cardano          " + cardanoAPY + "                 "  +cardanoStakedStr +  " ₳\n\n"
    # tweet5_5 = "   Celo                   " + celoAPY + "                  "  +celoStakedStr +  " ₳\n\n"
    # tweet6 = "   Dogecoin          " + dogecoinAPY + "                 "  +dogecoinStakedStr +  " ₳\n\n"
    # tweet6_5 = "   Ethereum          " + ethereumAPY + "                 "  +ethereumStakedStr +  " ₳\n\n"
    # tweet7 = "   Lightning            " + lightningAPY + "                 "  +lightningStakedStr +  " ₳\n\n"
    # tweet7_5 = "   Litecoin             " + litecoinAPY + "                 "  +litecoinStakedStr +  " ₳\n\n"
    # tweet8 = "   Polygon            " + polygonAPY + "                 "  +polygonStakedStr +  " ₳\n\n"
    # tweet8_5 = "   Solana            " + solanaAPY + "                 "  +solanaStakedStr +  " ₳\n\n"
    # tweet9 = "   Tezos              " + tezosAPY + "                 "  +tezosStakedStr +  " ₳\n\n"
    # tweet9_5 = "   Zcash              " + zcashAPY + "                 "  +zcashStakedStr +  " ₳\n\n"

    # tweet10 = "Tokens staked out of the circulating supply: \n" + totalTokensStakedFormatted + " ₳ / " + totalCircTokensFormatted + " ₳"
    # tweet11 = "\n\nTotal Staked Percentage: " + stakedPercentageStr + "%\n"+ "$AMP #flexa #amp"

    # tweet = (tweet1 + tweet2 + tweet2_5 + tweet3 + tweet3_5 + tweet4 + tweet4_5 + tweet5 + tweet5_5 + tweet6 +tweet6_5+tweet7+tweet7_5+tweet8+tweet8_5+tweet9+tweet9_5)
    # tweetText = (tweet10 + tweet12 + tweet11) # with difference
    # tweetText = (tweet10 + tweet11) # without difference

    

    # https://python.plainenglish.io/generating-text-on-image-with-python-eefe4430fe77
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    # width = 512
    # height = 846
    # img = Image.new('RGB', (width, height), color='black')
    # fnt = ImageFont.truetype("NotoSans-Regular.ttf", 20)
    # imgDraw = ImageDraw.Draw(img)

    # imgDraw.text((10, 10), tweet,font=fnt, fill=(255, 255, 255))

    # # currentTime = time.time()
    # # currentTime = int(currentTime)
    # # currentTime = str(currentTime)
    # now = datetime.now() # current date and time
    # currentTime = now.strftime("%m%d%Y_%H%M")
    # img.save('./image/{}.png'.format(currentTime))

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
        '''
        0   Gemini
        1   Spedn
        2   Bitcoin
        3   Bitcoin Cash
        4   Cardano
        5   Celo
        6   Dogecoin
        7   Ethereum
        8   Lightning
        9   Litecoin
        10  Polygon
        11  Solana
        12  Tezos
        13  Zcash
        '''
        # writer.writerow([dateCurr, timeCurr, spednStakedstr,geminiStakedStr,lightningStakedStr,spednAPY,geminiAPY,lightningAPY, ""])
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
        stakedStrList[10],apyList[11],
        stakedStrList[12],apyList[12],
        stakedStrList[13],apyList[13]
        ])
    await page.close()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
