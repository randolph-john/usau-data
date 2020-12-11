import pandas as pd
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
game_url = "https://play.usaultimate.org/teams/events/match_report/?EventGameId=3hs5ujsctprlTJCac%2bhMUowzWJY6lVT%2fOm6C39JPRNI%3d"
teams = ["home_team", "away_team"]

def main():
    home_team, away_team = get_data_from_one_page(game_url)
    print(home_team)
    print(away_team)

def get_data_from_one_page(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(game_url)
    for team in teams:
        # scrape data
        result = driver.find_element_by_id(team).text
        index = 0
        result_list = result.splitlines()

        # cut out unneccessary rows
        for i in range(len(result)):
            if "G A D T" in result_list[i]:
                index = i
                break;
        result_list = result_list[index+1:]

        # convert to dataframe
        data = list()
        for guy in result_list:
            guy_list = list()
            split_guy = str.split(guy)
            guy_list.append(' '.join(split_guy[:-4]))
            guy_list.append(int(split_guy[-4]))
            guy_list.append(int(split_guy[-3]))
            guy_list.append(int(split_guy[-2]))
            guy_list.append(int(split_guy[-1]))
            data.append(guy_list)
        df = pd.DataFrame(data, columns = ['Name', 'G', 'A', 'D', 'T'])
        df['+/-'] = df.apply (lambda row: row['G'] + row['A'] + row['D'] - row['T'], axis=1)
        yield df

if __name__ == '__main__':
    main()
