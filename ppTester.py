import sys
import commonUtils
from selenium.webdriver.common.by import By
import time

# Constants & useful variables
URL_ELEMENT_XPATH = "//a[@class='rel-link']"
start_page = sys.argv[1]

# time program
start_time = time.time()

# Starts the driver with configured options and goes to start_page.
driver = commonUtils.build_driver(2, True)
driver.get(start_page)
print(f"Driver is now at start_page!")

# Scrolling to bottom to find all possible elements.
commonUtils.scroll_till_bottom(driver, 0.5)

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
