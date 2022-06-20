from io import BytesIO
from PIL import Image
import requests


# Function for printing progress of a loop.
def print_progress(i, total):
    print(f'\rProgress: {i+1}/{total}', end='')


# Function for downloading an image from an url.
def download_image_from_url(url, name):
    data = requests.get(url)
    if data.status_code == 200:
        img = Image.open(BytesIO(data.content))
        img.save(name)


# Function for downloading and saving multiple images from a URL list.
def save_images(image_url_list, path, quite=False):
    if quite:
        for i, image_url in enumerate(image_url_list):
            download_image_from_url(image_url, path + f"{i}_image.jpg")
        return

    print(f"Starting download from URL list, ", end='')
    for i, image_url in enumerate(image_url_list):
        print_progress(i, len(image_url_list))
        download_image_from_url(image_url, path + f"{i}_image.jpg")
    print(f"  - Download Complete!")
