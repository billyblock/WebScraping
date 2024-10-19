from selenium import webdriver
from selenium.webdriver.common.by import By # for locating HTML elements
import time

# For the basics of Selenium I was following their guide
# https://www.selenium.dev/selenium/docs/api/py/index.html

# For get the page source
# https://www.scrapingbee.com/blog/selenium-python/

def store_to_json():
    # This method will store the players name, salary, and country to a JSON object
    pass


# https://basketball.realgm.com/nba/players
# Get the players name and their country
def get_players_country():
    
    browser = webdriver.Chrome()
    browser.get("https://basketball.realgm.com/nba/players")
    
    # Locate all players names
    player_name_elements = browser.find_elements(By.XPATH, "//tr/td[@data-th='Player']/a")

    # Extract and print all player names
    player_names = []
    for element in player_name_elements:
        player_names.append(element.text)
        print(element.text)
    
    '''
    There is not element between Council IV and Craig so I am currently unsure why it is throwing error.
    Ricky Council IV
    [14276:15224:1018/223149.331:ERROR:device_event_log_impl.cc(201)] [22:31:49.331] USB: usb_service_win.cc:105 SetupDiGetDeviceProperty({{A45C254E-DF1C-4EFD-8020-67D146A850E0}, 6}) failed: Element not found. (0x490)
    Torrey Craig
    '''
    
    browser.quit() # Properly exit browser

def get_players_salary():
    # https://hoopshype.com/salaries/players/
    # Get the players name and their salaries
    pass


def main():
    country = get_players_country()

if __name__ == "__main__":
    main()