from io import BytesIO
from PIL import Image
import requests

"""
@Author - Mark Alan Vincent II
@Date - 6/20/2022
This small Util Library contains common functions used in scraping a web page.
------------------------------------------------------------------------------

---                 Ordinary Python Utils                       ---
print_progress  - Progress viewer of a loop via prints.
write_text_file - Will write a passed list contents into a text file.

---         Image Saving Utils via Requests & PIL libs          ---
download_image_from_url - Will download an image from a URL with the given name.
save_images             - Will download all images from a URL list to a specified path.
save_images_from_file   - Will download all images from a URL text file to a specified path.

"""


# Function for printing progress of a loop.
def print_progress(i, total):
    print(f'\rProgress: {i+1}/{total}', end='')


# Function for writing a list to a text file.
def write_text_file(out_list, path):
    print(f"Starting write to {path}")
    out_file = open(path, "w")
    f_len = len(out_list)
    for i, line in enumerate(out_list):
        print_progress(i, f_len)
        out_file.write(line + "\n")
    out_file.close()
    print(f"  - Write File Complete!")


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
            download_image_from_url(image_url, path + f"{i+1}_image.jpg")
        return

    print(f"Starting download from URL list...")
    f_len = len(image_url_list)
    for i, image_url in enumerate(image_url_list):
        print_progress(i, f_len)
        download_image_from_url(image_url, path + f"{i+1}_image.jpg")
    print(f"  - Download Complete!")


# Function for downloading and saving multiple images from a URL text file.
def save_images_from_file(input_file, path, quite=False):
    print(f"Starting download from {input_file}")
    try:
        num_lines = sum(1 for _ in open(input_file))
        f_read = open(input_file, "r").read().splitlines()
        line = 0
        for url in f_read:
            print_progress(line, num_lines)
            save_path = path + f"{line+1}_image.jpg"
            download_image_from_url(url, save_path)
            line += 1
        print(f"  - Download Complete!")
    except FileNotFoundError:
        print(f"Failed to find input file at, {input_file}\n No images have been downloaded.")
        return
