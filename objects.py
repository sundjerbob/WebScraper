# sports keys
football_key = 'football'
basketball_key = 'basketball'
ice_hokey_key = 'ice_hockey'
tennis_key = 'tennis'
handball_key = 'handball'
volleyball_key = 'volleyball'

# betting games storing: dictionary types
game_dict = 1
odds_dict = 2


class Event:

    def __init__(self, company1, company2, datetime, sport, league):
        self.company1 = company1
        self.company2 = company2
        self.datetime = datetime
        self.sport = sport
        self.league = league
        self.event_key = self.company1 + ' | ' + self.company2 + ' | ' + self.datetime
        self.games = dict()

    def __str__(self):
        return self.sport + ' event:\n' + self.league + '\n' + self.event_key


class FootballEvent(Event):
    def __init__(self, team1, team2, datetime, league):
        super().__init__(team1, team2, datetime, football_key, league)

    def __str__(self):
        return super().__str__()


class BasketballEvent(Event):
    def __init__(self, company1, company2, datetime, league):
        super().__init__(company1, company2, datetime, basketball_key, league)

    def __str__(self):
        return super().__str__()


class IceHokeyEvent(Event):
    def __init__(self, company1, company2, datetime, league):
        super().__init__(company1, company2, datetime, ice_hokey_key, league)

    def __str__(self):
        return super().__str__()


class TennisEvent(Event):
    def __init__(self, company1, company2, datetime, league):
        super().__init__(company1, company2, datetime, tennis_key, league)

    def __str__(self):
        return super().__str__()


class HandballEvent(Event):
    def __init__(self, company1, company2, datetime, league):
        super().__init__(company1, company2, datetime, handball_key, league)

    def __str__(self):
        return super().__str__()


class VolleyballEvent(Event):
    def __init__(self, company1, company2, datetime, league):
        super().__init__(company1, company2, datetime, volleyball_key, league)

    def __str__(self):
        return super().__str__()
