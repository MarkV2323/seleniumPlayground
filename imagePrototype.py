import sys
import commonUtils
from selenium.webdriver.common.by import By
from PIL import ImageFile
import time

# For help with truncated files
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Constants variables
URL_ELEMENT_XPATH = "//a[@class='rel-link']"
IMPLICIT_WAIT_TIME = 2
SCROLL_WAIT_TIME = 2
START_PAGE = sys.argv[1]
TEXT_OUTPUT = "out_data.txt"
IMAGE_DIRECTORY = "images/"

"""
Program Pipeline
"""
# time program
start_time = time.time()
# Starts the driver with configured options and goes to start_page.
driver = commonUtils.build_driver(IMPLICIT_WAIT_TIME, True)
driver.get(START_PAGE)
print(f"Driver is now at start_page!")
# Scrolling to bottom to find all possible elements.
commonUtils.scroll_till_bottom(driver, SCROLL_WAIT_TIME)
# Begin finding URLs to content galleries, then compile URLs into a list.
galleries_to_vist = commonUtils.get_href_from_page(driver, By.XPATH, URL_ELEMENT_XPATH)
# vist links one by one, save image URLs to list
image_urls = commonUtils.get_hrefs_from_pages(driver, By.XPATH, URL_ELEMENT_XPATH, galleries_to_vist)
# output to a text file
commonUtils.write_text_file(image_urls, TEXT_OUTPUT)
print("--- %s seconds ---" % (time.time() - start_time))
driver.close()
exit(-1)

# TODO: Implement version that allows for downloading of images using asyncio
# download images from text file.
commonUtils.save_images_from_file(TEXT_OUTPUT, IMAGE_DIRECTORY)
# output total time for program to run.
print(f"Program completed in {time.time() - start_time} seconds.")
driver.close()
