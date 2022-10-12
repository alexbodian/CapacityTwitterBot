from multiprocessing import pool
import config
import json
import requests
from pprint import pprint
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
def main():

    '''
    Change apy in tweet to yield
    '''
#APY on capacity site   https://app.flexa.network/account/supply 
#Capacity site   https://app.flexa.network/
    total_balance = 0
    pools = []

    '''
    Index Order for poolWithStrings
    0 : Pool Name
    1 : APY/Yield Percentage
    2 : Pool Balance
    '''
    poolsWithStrings = [[],[],[]]
    
    
    

    req = requests.get("https://tstdrv971555.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=37&deploy=1&compid=TSTDRV971555&h=d0e4ab08a3fd5eeceec6")

    req_obj = req.json()
    # pool info order - name, total, yield/apy
    for i in req_obj['pools']:
        pools.append([(i['name']), i["balance"], i["yield"]])
        

    pools.sort()

    for x in pools:
        total_balance += x[1] #Sums the pool balances to get total balance
        poolsWithStrings[0].append(x[0]) #Adds the list of pool names
        # poolsWithStrings[1].append(locale.format("%d", x[1], grouping=True)) #Adds the list of pool balances
        poolsWithStrings[1].append(f"{x[1]:,}") #Adds the list of pool balances
        poolsWithStrings[2].append(f'{x[2]:.2%}') #Adds the list of pool yields

    currentTime = time.time()
    currentTime = int(currentTime)
    currentTime = str(currentTime)
    now = datetime.now()  # current date and time
    currentTime = now.strftime("%m%d%Y_%H%M")
    df = pd.DataFrame(
                {'Pool': poolsWithStrings[0],
                'Yield': poolsWithStrings[2],
                'Amount of AMP Staked': poolsWithStrings[1]
                

                }

                )
    df.reset_index(drop=True, inplace=True)  # remove row numbers
    df_styled = df.style.set_properties(**{
        'background-color': 'black',
        'color': 'white',
        'border': '1px solid white'
        })

    df_styled = df_styled.set_table_styles([
        {
           'selector': 'th',
           'props': [
               ('background-color', 'black'),
               ('color', 'grey'),
               ('border', '1px solide white')
               ]
       }])
    dfi.export(df_styled, './{}.png'.format(currentTime))
    # dfi.export(df_styled, './image/{}.png'.format(currentTime))
    
    # tweetText1 = "Total tokens staked: " + (f"{total_balance:,}") + " ₳"
    # actualTweet = tweetText1
    # print(actualTweet)

    
    # authenticator=tweepy.OAuthHandler(config.api_key, config.api_key_secret)
    # authenticator.set_access_token(config.access_token, config.access_token_secret)

    # api=tweepy.API(authenticator, wait_on_rate_limit=True)

    # # upload image
    # media=api.media_upload('./image/{}.png'.format(currentTime))

    # # post tweet with image
    # api.update_status(status=tweetText, media_ids=[media.media_id])


    # CSV Stuff
    
    dateCurr=date.today()
    dateCurr=dateCurr.strftime("%m/%d/%y")

    timeCurr=datetime.now()
    timeCurr=timeCurr.strftime("%H:%M")

    with open("./capacityStatsAPI.csv", "a", newline='') as csvfile:
        writer=csv.writer(csvfile)

        writer.writerow([
            dateCurr, timeCurr,
            poolsWithStrings[1][0],poolsWithStrings[2][0],
            poolsWithStrings[1][1],poolsWithStrings[2][1],
            poolsWithStrings[1][2],poolsWithStrings[2][2],
            poolsWithStrings[1][3],poolsWithStrings[2][3],
            poolsWithStrings[1][4],poolsWithStrings[2][4],
            poolsWithStrings[1][5],poolsWithStrings[2][5],
            poolsWithStrings[1][6],poolsWithStrings[2][6],
            poolsWithStrings[1][7],poolsWithStrings[2][7],
            poolsWithStrings[1][8],poolsWithStrings[2][8],
            poolsWithStrings[1][9],poolsWithStrings[2][9],
            poolsWithStrings[1][10],poolsWithStrings[2][10],
            poolsWithStrings[1][11],poolsWithStrings[2][11],
            poolsWithStrings[1][12],poolsWithStrings[2][12],
            poolsWithStrings[1][13],poolsWithStrings[2][13]


        ])


if __name__ == "__main__":
    main()



