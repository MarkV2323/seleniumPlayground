import sys
import commonUtils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
# Constants
URL_ELEMENT_XPATH = "//a[@class='rel-link']"

# Starts the driver with configured options, Headless mode.
start_time = time.time()
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
scroll_pause = 0.5
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
galleries_to_vist = commonUtils.get_href_from_page(driver, By.XPATH, URL_ELEMENT_XPATH)

# vist links one by one, save image URLs to list
image_urls = commonUtils.get_hrefs_from_pages(driver, By.XPATH, URL_ELEMENT_XPATH, galleries_to_vist)

# output to a text file
commonUtils.write_text_file(image_urls, "out_data.txt")

# download images from text file.
commonUtils.save_images_from_file("out_data.txt", "images/")

# output total time for program to run.
print(f"Program completed in {time.time() - start_time} seconds.")
driver.close()
