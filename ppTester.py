import sys
import commonUtils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Starts the driver with configured options, Headless mode.
start_time = time.time()
url_element = "//a[@class='rel-link']"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chromedriver = Service(f"driver/chromedriver.exe")
driver = webdriver.Chrome(service=chromedriver, options=chrome_options)
driver.implicitly_wait(2)
print("Chrome Web Driver has been successfully configured for headless mode!")

# Go to start page from program argument 0.
start_page = sys.argv[1]
print(f"Driver now navigating to page argument, {start_page}")
driver.get(start_page)
time.sleep(0.5)
print(f"Start page found successfully.")

# Scrolling to bottom to find all possible elements.
scroll_pause = 4
total_time_slept = 0
last_h = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(scroll_pause)
    total_time_slept += scroll_pause
    print(f"\rTime spent scrolling so far, {total_time_slept} seconds.", end='')
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    # print(f"LH:{last_h}, NH:{new_height}")
    if new_height == last_h:
        break
    last_h = new_height
print(f"\nDone scrolling, spent {total_time_slept} seconds scrolling.")

# Begin finding URLs to content galleries, then compile URLs into a list.
print(f"Building Content Gallery List:")
galleries_to_vist = list()
content_galleries = driver.find_elements(By.XPATH, url_element)
for i, element in enumerate(content_galleries):
    commonUtils.print_progress(i, len(content_galleries))
    galleries_to_vist.append(element.get_attribute("href"))
print(f" - Total Galleries found: {len(galleries_to_vist)}")

# vist links one by one, save image URLs to list
image_urls = list()
print(f"Building Image URL list:")
for i, url in enumerate(galleries_to_vist):
    commonUtils.print_progress(i, len(galleries_to_vist))
    # Go to page
    driver.get(url)
    # begin finding image URLs
    tmp_url_dump = driver.find_elements(By.XPATH, url_element)
    for element in tmp_url_dump:
        image_urls.append(element.get_attribute("href"))
print(f" - Total Images found: {len(image_urls)}")

# output to a text file
print(f"Building Image URL Text File:")
f_path = "images/url_data.txt"
out_file = open(f_path, "w")
for i, url in enumerate(image_urls):
    commonUtils.print_progress(i, len(image_urls))
    out_file.write(url)
    out_file.write("\n")
out_file.close()
print(f"\nImage URL Text File at {f_path}. Program completed in {time.time() - start_time} seconds.!")
driver.close()
