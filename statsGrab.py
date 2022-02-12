import os
import time
import asyncio
import time
import pyppeteer
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://app.flexa.network/explore/app/gemini')
    time.sleep(3)

    stakedGemini = page.xpath('/html/body/div/div[2]/main/div[2]/div[2]/div/div[4]/h3/span')

    print(stakedGemini)