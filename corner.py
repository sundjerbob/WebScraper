from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from cornerdatabase import corner_link
from cornerdatabase import football_key
from cornerdatabase import basketball_key
from cornerdatabase import ice_hokey_key
from cornerdatabase import tennis_key
from cornerdatabase import handball_key
from cornerdatabase import volleyball_key


def start(database):
    web_driver = webdriver.Chrome("C:/Users/Tadija/chromedriver.exe")
    web_driver.get(corner_link)
    web_driver.maximize_window()
    time.sleep(2)
    fill_events(web_driver, database)


def fill_events(web_driver, database):
    sports_buttons = WebDriverWait(web_driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#dataTree div.sport.ng-scope')))
    sports_names = WebDriverWait(web_driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#dataTree div.sport.ng-scope div.sportName')))
    sports_names = sports_names[0:1]
    for i in range(0, len(sports_names)):

        if sports_names[i].text is None:
            break

        curr_sport = format_sport(sports_names[i].text)

        if curr_sport is None:
            continue

        WebDriverWait(web_driver, 5).until(EC.element_to_be_clickable(sports_buttons[i]))
        ActionChains(web_driver).move_to_element(sports_buttons[i]).click().perform()

        daily_events_button = sports_buttons[i].find_element(By.CSS_SELECTOR, 'div.dailyEvents')
        WebDriverWait(web_driver, 5).until(EC.element_to_be_clickable(daily_events_button))
        ActionChains(web_driver).move_to_element(daily_events_button).click().perform()

        events = WebDriverWait(web_driver, 5).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#events div.eventName')))

        events = events[0:3]

        for event in events:

            WebDriverWait(web_driver, 20).until(EC.element_to_be_clickable(event))

            if event is None or event.text is None:
                continue

            ActionChains(web_driver).move_to_element(event).click().perform()

            event_header = WebDriverWait(web_driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#event #eventHeader')))

            if event is None or event.text is None or event_header is None or event_header.text is None:
                continue

            event_data = format_event(event.text, event_header.text)

            if event_data is None:
                continue

            new_event = database.add_event(company1=event_data[0], company2=event_data[1], datetime=event_data[2],
                                           league=event_data[3], sport=curr_sport)
            fill_games(web_driver, database, new_event)


def fill_games(web_driver, database, event):
    games = WebDriverWait(web_driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#oddsData '
                                                                                                      'div.oddsGroup'
                                                                                                      '.ng-scope')))
    for game in games:

        game_header = game.find_element(By.CSS_SELECTOR, 'div.groupHeader')
        game_data = game.find_elements(By.CSS_SELECTOR, 'div.groupData span')

        if game_header.text is None:
            continue

        counter = 0
        bets_names = list()
        bets_odds = list()
        curr_bet = None

        for i in range(0, len(game_data)):

            if game_data[i] is None or game_data[i].text is None :
                continue

            if is_betting_odds(game_data[i].text):

                if curr_bet is not None:
                    bets_names.append(curr_bet)
                    bets_odds.append(game_data[i].text)
                    counter += 1
                    curr_bet = None
                else:
                    print('corner.py fill_games(): there is no bet for this odd')

            else:

                if curr_bet is not None:
                    bets_names.append(curr_bet)
                    bets_odds.append('0.00')
                    print('added bet is locked')
                    counter += 1

                curr_bet = game_data[i].text.strip()

        database.add_game_to_event(event, game_header.text.strip(), bets_names, bets_odds)


# String formatting ####################################################################################################


def format_sport(sport):
    if sport is None:
        return None

    sport = sport.split('\n')[0].strip().lower().replace(' ', '_')

    if sport in {football_key, basketball_key, ice_hokey_key, tennis_key, handball_key, volleyball_key}:
        return sport

    return None


def format_event(event_text, league_and_datetime):
    if event_text is None or league_and_datetime is None:
        return None

    event_data = event_text.split('\n')
    buff = league_and_datetime.split('\n')

    if len(event_data) == 4 and len(buff) == 3:
        event_data[0].strip()
        event_data[1].strip()
        event_data[2] = buff[1].strip()
        event_data[3] = buff[0].strip()
        return event_data

    print('corner.py: format_event()\n')
    return None


def is_betting_odds(string):
    string.strip()

    if len(string) == 4 or len(string) == 3:

        for i in range(0, len(string)):

            if string[i] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}:
                continue

            return False

        return True

    return False
