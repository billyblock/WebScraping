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

def get_players_country():
    # https://basketball.realgm.com/nba/players
    # Get the players name and their country
    browser = webdriver.Chrome()
    browser.get("https://basketball.realgm.com/nba/players")
    
    # Gets the first players name on the site
    player_name = browser.find_element(By.XPATH, "//tr/td[@data-th='Player']/a").text
    
    print(player_name)
    
    browser.quit() # Properly exit browser

def get_players_salary():
    # https://hoopshype.com/salaries/players/
    # Get the players name and their salaries
    pass


def main():
    country = get_players_country()

if __name__ == "__main__":
    main()