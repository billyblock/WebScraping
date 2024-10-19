from selenium import webdriver
from selenium.webdriver.common.by import By # for locating HTML elements
import time

# For the basics of Selenium I was following their guide
# https://www.selenium.dev/selenium/docs/api/py/index.html

# For get the page source
# https://www.scrapingbee.com/blog/selenium-python/



# List for all players
players = []

def store_to_json():
    # This method will store the players name, salary, and country to a JSON object
    pass


# https://basketball.realgm.com/nba/players
# Get the players name and their country
def get_players_country():
    
    browser = webdriver.Chrome()
    browser.get("https://basketball.realgm.com/nba/players")
    
    # Locate all players names
    player_names_elements = browser.find_elements(By.XPATH, "//tr/td[@data-th='Player']/a")
    # Locate all player countries
    player_countries_elements = browser.find_elements(By.XPATH, "//tr/td[@data-th='Nationality']")

    for name_element, country_element in zip(player_names_elements, player_countries_elements):
        name = name_element.text
        
        # Gets the nationalities of the player
        # some players can have multiple countries so I made a list for the countries
        country = []
        for a in country_element.find_elements(By.TAG_NAME, "a"):
            country.append(a.text)
            
        # Create a dictionary for each player so it emulates a json file for now
        player_dictionary = {
            "name": name,
            "country": country,
            "salary": None
        }
        players.append(player_dictionary)
    print(players)
    browser.quit() # Properly exit browser



# https://hoopshype.com/salaries/players/
# Get the players name and their salaries
def get_players_salary():
    browser = webdriver.Chrome()
    browser.get("https://hoopshype.com/salaries/players/")
    
    # Gets both specified elements 
    player_rows = browser.find_elements(By.XPATH, "//tr[td[@class='name']/a and td[@class='hh-salaries-sorted']]")
    
    # Print the name and salary of each player
    for row in player_rows:
        name = row.find_element(By.TAG_NAME, "a").text
                
        salary = row.find_element(By.CLASS_NAME, "hh-salaries-sorted").text
                
        print(f"Name: {name}, Salary: {salary}")


def main():
    #get_players_country()
    get_players_salary()

if __name__ == "__main__":
    main()