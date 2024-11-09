from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:/Users/DELL/AppData/Local/Google/Chrome/User Data")  # Use your own path
chrome_options.add_argument("--profile-directory=Default")  # Use your own profile directory if needed

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Open Google homepage
driver.get("https://www.google.com")

# Wait for the search input to load
time.sleep(2)

# Find the search input field and enter "boy"
search_input = driver.find_element(By.ID, "input")  # Find input by ID
search_input.send_keys("boy")  # Type "boy" into the search bar

# Press ENTER to search
search_input.send_keys(Keys.RETURN)

# Optionally, wait to see the results page before closing
time.sleep(5)

# Quit the driver
driver.quit()
