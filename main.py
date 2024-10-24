from selenium import webdriver
from selenium.webdriver.common.by import By # for locating HTML elements
import json
import matplotlib.pyplot as plot
import re
from collections import defaultdict

# For the basics of Selenium I was following their guide
# https://www.selenium.dev/selenium/docs/api/py/index.html

# For get the page source
# https://www.scrapingbee.com/blog/selenium-python/



# List for all players
players = []


browser = webdriver.Chrome()

# https://basketball.realgm.com/nba/players
# Get the players name and their country
def get_players_country():
    
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



# https://hoopshype.com/salaries/players/
# Get the players name and their salaries
def get_players_salary():
    browser.get("https://hoopshype.com/salaries/players/")
    
    # Gets both specified elements 
    player_rows = browser.find_elements(By.XPATH, "//tr[td[@class='name']/a and td[@class='hh-salaries-sorted']]")
    
    # Print the name and salary of each player
    for row in player_rows:
        name = row.find_element(By.TAG_NAME, "a").text
                
        salary = row.find_element(By.CLASS_NAME, "hh-salaries-sorted").text
        
        # Match the salary to the corresponding player in the list of players
        for player in players:
            if player["name"] == name:
                player["salary"] = salary
                break

def plot_salary_by_country():
    #https://www.geeksforgeeks.org/defaultdict-in-python/
    country_salaries = defaultdict(list)

    for player in players:
        if player["salary"]:
            salary = float(re.sub(r"[^\d.]", "", player["salary"]))
            for country in player["country"]:
                country_salaries[country].append(salary)
    print(country_salaries)

def main():
    get_players_country()
    get_players_salary()
    
    
    browser.quit() # Properly exit browser
    
    with open("player_data.json", "w") as file:
        json.dump(players, file, indent=4)
    plot_salary_by_country()

if __name__ == "__main__":
    main()