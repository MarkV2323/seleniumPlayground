"""
Ensures selenium is correctly installed and working. Any errors here will ensure that the other programs
will not work correctly.
"""
import sys
import time

from PIL import ImageFile

import commonUtils

# For help with truncated files
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Constants variables
IMPLICIT_WAIT_TIME = 2
START_PAGE = "https://selenium-python.readthedocs.io/installation.html#drivers"

"""
Program Pipeline
"""
# time program
start_time = time.time()
# Starts the driver with configured options and goes to start_page.
driver = commonUtils.build_driver(IMPLICIT_WAIT_TIME, True)
driver.get(START_PAGE)
print(f"Driver is now at start_page!")
