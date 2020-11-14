import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
game_url = "https://play.usaultimate.org/teams/events/match_report/?EventGameId=3hs5ujsctprlTJCac%2bhMUowzWJY6lVT%2fOm6C39JPRNI%3d"

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(game_url)
    result = driver.find_element_by_id("away_team").text
    print(result)
    result_list = result.splitlines()
    print(result_list)

if __name__ == '__main__':
    main()
