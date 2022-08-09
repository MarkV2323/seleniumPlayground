"""
Author: Mark Vincent II
Summary: This is a basic level program to begin testing with the asyncio library and webscraping.

"""
import os
import time
from io import BytesIO
import asyncio

import aiohttp
import aiofiles
import requests
from PIL import Image


# Function for loading lines into a list.
def line_to_list(input_file: str) -> list[str]:
    res_list = list()
    try:
        f_read = open(input_file, "r").read().splitlines()
        for line in f_read:
            res_list.append(line.strip())
    except FileNotFoundError:
        print(f"Failed to find input file at, {input_file}\n")
    return res_list


# Function for downloading an image from an url (NOT async).
def download_image_from_url(url, name):
    data = requests.get(url)
    if data.status_code == 200:
        img = Image.open(BytesIO(data.content))
        img.save(name)


# Function for downloading an image from an url (async).
async def download_image_from_url_async(url: str, name: str, session):
    async with session.get(url) as resp:
        if resp.status == 200:
            # Must use async file writer (aiofiles)
            tmp_img_f = await aiofiles.open(name, mode="wb")
            await tmp_img_f.write(await resp.read())
            await tmp_img_f.close()

# Function for downloading all images from a url list (async, uses gather)
async def download_all_images_async(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i, url in enumerate(url_list):
            img_name = f"async_tester/image_{i}.jpg"
            tasks.append(asyncio.ensure_future(download_image_from_url_async(url, img_name, session)))
        await asyncio.gather(*tasks)


# Start of tests
text_file_path = "out_data.txt"
url_list = line_to_list(text_file_path)

# Dirs for holding data
sync_dir = "sync_tester"
async_dir = "async_tester"
if os.path.exists(sync_dir) is False:
    os.makedirs(sync_dir)
if os.path.exists(async_dir) is False:
    os.makedirs(async_dir)

# Sync Version
print("starting SYNC version")
start_time = time.time()
for i, url in enumerate(url_list):
    img_name = f"sync_tester/image_{i}.jpg"
    download_image_from_url(url, img_name)
print("--- %s seconds ---" % (time.time() - start_time))

# aSync Version
print("starting ASYNC version")
start_time = time.time()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(download_all_images_async(url_list))
print("--- %s seconds ---" % (time.time() - start_time))
