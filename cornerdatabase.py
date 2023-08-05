from objects import FootballEvent
from objects import BasketballEvent
from objects import IceHokeyEvent
from objects import TennisEvent
from objects import HandballEvent
from objects import VolleyballEvent
from objects import football_key
from objects import basketball_key
from objects import ice_hokey_key
from objects import tennis_key
from objects import handball_key
from objects import volleyball_key

corner_link = 'http://m.korneronline.com/#/pre-match'


def add_game_to_event(event, game_header, bets_names, bets_odds):

    event.games[game_header] = dict()

    for i in range(0, len(bets_names)):
        event.games[game_header][bets_names[i]] = bets_odds[i]


class CornerDatabase:
    def __init__(self):
        self.football_events = dict()
        self.basketball_events = dict()
        self.ice_hockey_events = dict()
        self.tennis_events = dict()
        self.handball_events = dict()
        self.volleyball_events = dict()

        self.all_events = {
            'football': self.football_events,
            'basketball': self.basketball_events,
            'ice_hockey': self.ice_hockey_events,
            'tennis': self.tennis_events,
            'handball': self.handball_events,
            'volleyball': self.volleyball_events,
        }

    def add_event(self, company1, company2, datetime, league, sport):

        new_event = None

        if sport == football_key:
            new_event = FootballEvent(company1, company2, datetime, league)

        if sport == basketball_key:
            new_event = BasketballEvent(company1, company2, datetime, league)

        if sport == ice_hokey_key:
            new_event = IceHokeyEvent(company1, company2, datetime, league)

        if sport == tennis_key:
            new_event = TennisEvent(company1, company2, datetime, league)

        if sport == handball_key:
            new_event = HandballEvent(company1, company2, datetime, league)

        if sport == volleyball_key:
            new_event = VolleyballEvent(company1, company2, datetime, league)

        self.all_events[new_event.sport][new_event.event_key] = new_event

        print(new_event)

        return new_event

    def get_event(self, company1, company2, datetime, sport=None):

        identifier = company1 + ' | ' + company2 + ' | ' + datetime

        if sport is None:

            for key in self.all_events.keys():
                if identifier in self.all_events[key].keys():
                    return self.all_events[key][identifier]
        else:
            if identifier in self.all_events.keys():
                return self.all_events[sport][identifier]

        return None

    def print_data(self):

        for sport_key in self.all_events.keys():

            for event_key in self.all_events[sport_key].keys():

                curr_event = self.all_events[sport_key][event_key]
                print("#################################################################################")
                print(curr_event)
                print("#################################################################################")

                for game_key in curr_event.games.keys():

                    print("--------------" + game_key + "--------------")

                    for bet_key in curr_event.games[game_key].keys():
                        print('[Bet: ' + bet_key + ' | ' + 'Odds: ' + curr_event.games[game_key][bet_key] + ']')
