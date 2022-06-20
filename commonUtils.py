from io import BytesIO
from PIL import Image
import requests

"""
@Author - Mark Alan Vincent II
@Date - 6/20/2022
This small Util Library contains common functions used in scraping a web page.
------------------------------------------------------------------------------

---                  Selenium Based Utils                       ---
get_href_from_page    - Will build a list of URLs found at driver's current page.
get_hrefs_from_pages  - Will build a list of URLs found from list of pages.

---                 Ordinary Python Utils                       ---
print_progress  - Progress viewer of a loop via prints.
write_text_file - Will write a passed list contents into a text file.

---         Image Saving Utils via Requests & PIL libs          ---
download_image_from_url - Will download an image from a URL with the given name.
save_images             - Will download all images from a URL list to a specified path.
save_images_from_file   - Will download all images from a URL text file to a specified path.

"""


# Function for building a list of URLs found on a page.
def get_href_from_page(driver, by, search) -> list:
    url_list = list()
    found_elements = driver.find_elements(by, search)
    found_amount = len(found_elements)
    for i, element in enumerate(found_elements):
        print_progress(i, found_amount, "Building URL List from page: ")
        url_list.append(element.get_attribute("href"))
    print(f" - Total HREFs found: {len(url_list)}")
    return url_list


# Function for gathering URLs from several pages.
def get_hrefs_from_pages(driver, by, search, pages) -> list:
    urls = list()
    pages_total = len(pages)
    for i, url in enumerate(pages):
        print_progress(i, pages_total, "Building URL List from pages: ")
        driver.get(url)
        tmp_url_dump = driver.find_elements(by, search)
        for element in tmp_url_dump:
            urls.append(element.get_attribute("href"))
        del tmp_url_dump
    print(f" - Total HREFs found: {len(urls)}")
    return urls


# Function for printing progress of a loop.
def print_progress(i, total, suffix=""):
    print(f'\r{suffix}Progress: {i+1}/{total}', end='')


# Function for writing a list to a text file.
def write_text_file(out_list, path):
    out_file = open(path, "w")
    f_len = len(out_list)
    for i, line in enumerate(out_list):
        print_progress(i, f_len, f"Starting write to {path}: ")
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
    f_len = len(image_url_list)
    for i, image_url in enumerate(image_url_list):
        print_progress(i, f_len, f"Starting download from URL list: ")
        download_image_from_url(image_url, path + f"{i+1}_image.jpg")
    print(f"  - Download Complete!")


# Function for downloading and saving multiple images from a URL text file.
def save_images_from_file(input_file, path, quite=False):
    try:
        num_lines = sum(1 for _ in open(input_file))
        f_read = open(input_file, "r").read().splitlines()
        line = 0
        for url in f_read:
            print_progress(line, num_lines, f"Starting download from {input_file}: ")
            save_path = path + f"{line+1}_image.jpg"
            download_image_from_url(url, save_path)
            line += 1
        print(f"  - Download Complete!")
    except FileNotFoundError:
        print(f"Failed to find input file at, {input_file}\n No images have been downloaded.")
        return
