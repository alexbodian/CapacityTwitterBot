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


    
    # Gemini Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/app/gemini')
    time.sleep(10)
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
    time.sleep(11)
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
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    lightningStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    lightningStaked = lightningStaked.group(0)
    lightningStakedStr = lightningStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    lightningStaked = lightningStaked.replace(",", "")
    lightningStaked = float(lightningStaked)

    # # Bitcoin Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/bitcoin')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    bitcoinStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    bitcoinStaked = bitcoinStaked.group(0)
    bitcoinStakedStr = bitcoinStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    bitcoinStaked = bitcoinStaked.replace(",", "")
    bitcoinStaked = float(bitcoinStaked)

    # # Bitcoin Cash Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/bitcoin-cash')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    bitcoincashStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    bitcoincashStaked = bitcoincashStaked.group(0)
    bitcoincashStakedStr = bitcoincashStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    bitcoincashStaked = bitcoincashStaked.replace(",", "")
    bitcoincashStaked = float(bitcoincashStaked)

    # # Cardano Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/cardano')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    cardanoStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    cardanoStaked = cardanoStaked.group(0)
    cardanoStakedStr = cardanoStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    cardanoStaked = cardanoStaked.replace(",", "")
    cardanoStaked = float(cardanoStaked)

    # # Celo Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/celo')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    celoStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    celoStaked = celoStaked.group(0)
    celoStakedStr = celoStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    celoStaked = celoStaked.replace(",", "")
    celoStaked = float(celoStaked)

    # # Dogecoin Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/dogecoin')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    dogecoinStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    dogecoinStaked = dogecoinStaked.group(0)
    dogecoinStakedStr = dogecoinStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    dogecoinStaked = dogecoinStaked.replace(",", "")
    dogecoinStaked = float(dogecoinStaked)

    # # Ethereum Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/ethereum')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    ethereumStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    ethereumStaked = ethereumStaked.group(0)
    ethereumStakedStr = ethereumStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    ethereumStaked = ethereumStaked.replace(",", "")
    ethereumStaked = float(ethereumStaked)

    # # Polygon Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/polygon')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    polygonStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    polygonStaked = polygonStaked.group(0)
    polygonStakedStr = polygonStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    polygonStaked = polygonStaked.replace(",", "")
    polygonStaked = float(polygonStaked)

    # # Litecoin Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/litecoin')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    litecoinStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    litecoinStaked = litecoinStaked.group(0)
    litecoinStakedStr = litecoinStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    litecoinStaked = litecoinStaked.replace(",", "")
    litecoinStaked = float(litecoinStaked)

    # # Solana Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/solana')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    solanaStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    solanaStaked = solanaStaked.group(0)
    solanaStakedStr = solanaStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    solanaStaked = solanaStaked.replace(",", "")
    solanaStaked = float(solanaStaked)
    
    # # Tezos Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/tezos')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    tezosStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    tezosStaked = tezosStaked.group(0)
    tezosStakedStr = tezosStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    tezosStaked = tezosStaked.replace(",", "")
    tezosStaked = float(tezosStaked)


    # # zcash Pool
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/transformer/zcash')
    time.sleep(11)
    element = await page.querySelector(".css-i3vmyo")
    title = await page.evaluate('(element) => element.textContent', element)
    zcashStaked = re.search("(?s)(?<=currently ).*?(?= of)", title)
    zcashStaked = zcashStaked.group(0)
    zcashStakedStr = zcashStaked
    # print("Total Staked on Lightning: " + lightningStaked)
    zcashStaked = zcashStaked.replace(",", "")
    zcashStaked = float(zcashStaked)







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
    time.sleep(11)
    element = await page.querySelectorAll(".css-1bvmc47")
    geminiAPY = await page.evaluate('(element) => element.textContent', element[0])
    spednAPY = await page.evaluate('(element) => element.textContent', element[1])
    bitcoinAPY = await page.evaluate('(element) => element.textContent', element[2])
    bitcoincashAPY = await page.evaluate('(element) => element.textContent', element[3])
    cardanoAPY = await page.evaluate('(element) => element.textContent', element[4])
    celoAPY = await page.evaluate('(element) => element.textContent', element[5])
    dogecoinAPY = await page.evaluate('(element) => element.textContent', element[6])
    ethereumAPY = await page.evaluate('(element) => element.textContent', element[7])
    lightningAPY = await page.evaluate('(element) => element.textContent', element[8])
    litecoinAPY = await page.evaluate('(element) => element.textContent', element[9])
    polygonAPY = await page.evaluate('(element) => element.textContent', element[10])
    solanaAPY = await page.evaluate('(element) => element.textContent', element[11])
    tezosAPY = await page.evaluate('(element) => element.textContent', element[12])
    zcashAPY = await page.evaluate('(element) => element.textContent', element[13])

    
    geminiAPY = geminiAPY.replace("APY", "")
    spednAPY = spednAPY.replace("APY", "")
    bitcoinAPY = bitcoinAPY.replace("APY", "")
    bitcoincashAPY = bitcoincashAPY.replace("APY", "")
    cardanoAPY = cardanoAPY.replace("APY", "")
    celoAPY = celoAPY.replace("APY", "")
    dogecoinAPY = dogecoinAPY.replace("APY", "")
    ethereumAPY = ethereumAPY.replace("APY", "")
    lightningAPY = lightningAPY.replace("APY", "")
    litecoinAPY = litecoinAPY.replace("APY", "")
    polygonAPY = polygonAPY.replace("APY", "")
    solanaAPY = solanaAPY.replace("APY", "")
    tezosAPY = tezosAPY.replace("APY", "")
    zcashAPY = zcashAPY.replace("APY", "")







    # Pulls the current circ supply from the website
    page = await browser.newPage()
    time.sleep(11)
    await page.goto('https://amptoken.org/metrics/circulating-supply/')
    element = await page.querySelector("pre")
    title = await page.evaluate('(element) => element.textContent', element)
    totalCircTokens = float(title)
    totalCircTokensFormatted = locale.format_string("%d", totalCircTokens, grouping=True)
    
    
    totalTokensStaked = geminiStaked+spednStaked+bitcoinStaked+bitcoincashStaked+cardanoStaked+celoStaked+dogecoinStaked+ethereumStaked+lightningStaked+litecoinStaked+polygonStaked+solanaStaked+tezosStaked+zcashStaked
    
    totalTokensStakedFormatted = locale.format_string("%d", totalTokensStaked, grouping=True)


    stakedPercentage = (((geminiStaked+spednStaked+lightningStaked)/totalCircTokens)*100)
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
    
    tweet1 = "                              Flexa Capacity Stats\n\n"
    tweet2 =   "    Pool                 APY                Amount of AMP Staked                       \n"
    tweet2_5 = " -----------         ----------          ----------------------------------                 \n"
    tweet3 = "   Gemini           " + geminiAPY + "                 "  +geminiStakedStr +  " ₳\n\n"
    tweet3_5 = "   Spedn             " + spednAPY + "                 "  +spednStakedstr +  " ₳\n\n"
    tweet4 = "   Bitcoin             " + bitcoinAPY + "                 "  +bitcoinStakedStr +  " ₳\n\n"
    tweet4_5 = "   Bitcoin Cash     " + bitcoincashAPY + "                 "  +bitcoincashStakedStr +  " ₳\n\n"
    tweet5 = "   Cardano          " + cardanoAPY + "                 "  +cardanoStakedStr +  " ₳\n\n"
    tweet5_5 = "   Celo                   " + celoAPY + "                  "  +celoStakedStr +  " ₳\n\n"
    tweet6 = "   Dogecoin          " + dogecoinAPY + "                 "  +dogecoinStakedStr +  " ₳\n\n"
    tweet6_5 = "   Ethereum          " + ethereumAPY + "                 "  +ethereumStakedStr +  " ₳\n\n"
    tweet7 = "   Lightning            " + lightningAPY + "                 "  +lightningStakedStr +  " ₳\n\n"
    tweet7_5 = "   Litecoin             " + litecoinAPY + "                 "  +litecoinStakedStr +  " ₳\n\n"
    tweet8 = "   Polygon            " + polygonAPY + "                 "  +polygonStakedStr +  " ₳\n\n"
    tweet8_5 = "   Solana            " + solanaAPY + "                 "  +solanaStakedStr +  " ₳\n\n"
    tweet9 = "   Tezos              " + tezosAPY + "                 "  +tezosStakedStr +  " ₳\n\n"
    tweet9_5 = "   Zcash              " + zcashAPY + "                 "  +zcashStakedStr +  " ₳\n\n"

    tweet10 = "Tokens staked out of the circulating supply: \n" + totalTokensStakedFormatted + " ₳ / " + totalCircTokensFormatted + " ₳"
    tweet11 = "\n\nTotal Staked Percentage: " + stakedPercentageStr + "%\n"+ "$AMP #flexa #amp"

    tweet = (tweet1 + tweet2 + tweet2_5 + tweet3 + tweet3_5 + tweet4 + tweet4_5 + tweet5 + tweet5_5 + tweet6 +tweet6_5+tweet7+tweet7_5+tweet8+tweet8_5+tweet9+tweet9_5)
    tweetText = (tweet10 + tweet12 + tweet11) # with difference
    tweetText = (tweet10 + tweet11) # without difference

    

    # https://python.plainenglish.io/generating-text-on-image-with-python-eefe4430fe77
    # https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html
    width = 512
    height = 846
    img = Image.new('RGB', (width, height), color='black')
    fnt = ImageFont.truetype("NotoSans-Regular.ttf", 20)
    imgDraw = ImageDraw.Draw(img)

    imgDraw.text((10, 10), tweet,font=fnt, fill=(255, 255, 255))

    # currentTime = time.time()
    # currentTime = int(currentTime)
    # currentTime = str(currentTime)
    now = datetime.now() # current date and time
    currentTime = now.strftime("%m%d%Y_%H%M")
    img.save('./image/{}.png'.format(currentTime))

    time.sleep(6)





    authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
    authenticator.set_access_token(access_token, access_token_secret)

    api = tweepy.API(authenticator, wait_on_rate_limit=True)

    # upload image
    media = api.media_upload('./image/{}.png'.format(currentTime))

    # post tweet with image
    api.update_status(status=tweetText,media_ids=[media.media_id])

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
        geminiStakedStr,geminiAPY,
        spednStakedstr,spednAPY,
        bitcoinStakedStr,bitcoinAPY,
        bitcoincashStakedStr,bitcoincashAPY,
        cardanoStakedStr,cardanoAPY,
        celoStakedStr,celoAPY,
        dogecoinStakedStr,dogecoinAPY,
        ethereumStakedStr,ethereumAPY,
        lightningStakedStr,lightningAPY,
        litecoinStakedStr, litecoinAPY,
        polygonStakedStr,polygonAPY,
        solanaStakedStr,solanaAPY,
        tezosStakedStr,tezosAPY,
        zcashStakedStr,zcashStakedStr
        ])
    await page.close()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
