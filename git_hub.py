# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# # Path to your Chrome user data directory
# chrome_user_data_path = r"C:\Users\DELL\AppData\Local\Google\Chrome\User Data"

# # Set up Chrome options to load the user data and profile
# chrome_options = Options()
# chrome_options.add_argument(f"user-data-dir={chrome_user_data_path}")  # Point to the user data directory
# chrome_options.add_argument("profile-directory=Default")  # Use "Default" profile or change it to another profile if needed

# # Set up the Chrome WebDriver with the options
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Maximize the window to ensure all elements are visible
# driver.maximize_window()

# # Wait for the window to stay open
# print("Your Chrome profile is now loaded. The browser will remain open.")




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your Chrome user data directory
chrome_user_data_path = r"C:\Users\DELL\AppData\Local\Google\Chrome\User Data"

# Set up Chrome options to load the user data and profile
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={chrome_user_data_path}")  # Point to the user data directory
chrome_options.add_argument("profile-directory=Default")  # Use "Default" profile or change it to another profile if needed

# Allow Chrome to be controlled by automation (prevent crash issue)
chrome_options.add_argument("--remote-debugging-port=9222")

# Set up the Chrome WebDriver with the options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Maximize the window to ensure all elements are visible
driver.maximize_window()

# Open the GitHub topics page
driver.get("https://github.com/topics/login?new_signup=true")

# Wait for the page to load completely
print("Page loaded, now performing the search.")

# Find the search input field by its ID and pass the link to it
search_input = driver.find_element(By.ID, "input")  # Locate the input field by ID
search_input.send_keys("https://github.com/topics/login?new_signup=true")  # Pass the URL as the search query
search_input.send_keys(Keys.RETURN)  # Press Enter to perform the search

# Wait for the search results to load
time.sleep(5)

# Optional: Perform any further actions or extract information
print("Search performed with the provided link.")

