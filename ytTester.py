import sys
import commonUtils
from selenium.webdriver.common.by import By
import time

# Constants variables
ELEMENT_XPATH = "//yt-formatted-string[@id='content-text']"
IMPLICIT_WAIT_TIME = 2
SCROLL_WAIT_TIME = 1
START_PAGE = sys.argv[1]
TEXT_OUTPUT = "out_data.txt"

"""
Program Pipeline
"""
# time program
start_time = time.time()

# Starts the driver with configured options and goes to start_page.
driver = commonUtils.build_driver(IMPLICIT_WAIT_TIME, headless=True)
driver.get(START_PAGE)
time.sleep(1)

# Scrolling to bottom to find all possible elements.
# commonUtils.scroll_till_bottom(driver, SCROLL_WAIT_TIME, scrolling_element_id="content", quite=False)

# scrape youtube comments
driver.execute_script(f"var element = document.getElementById('content');"
                      f"window.scrollTo(0, element.scrollHeight);")
comments = commonUtils.get_elements_from_page(driver, By.XPATH, ELEMENT_XPATH, quite=True)

# output to a text file
# commonUtils.write_text_file(image_urls, TEXT_OUTPUT)

# output total time for program to run.
print(f"Program completed in {time.time() - start_time} seconds.")
driver.close()
