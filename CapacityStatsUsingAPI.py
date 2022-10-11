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
    


    req = requests.get("https://tstdrv971555.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=37&deploy=1&compid=TSTDRV971555&h=d0e4ab08a3fd5eeceec6")

    req_obj = req.json()

    pprint(req_obj)


        




    



if __name__ == "__main__":
    main()



