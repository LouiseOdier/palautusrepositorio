import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.total = dict['goals']+dict['assists']
    

    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals:2} + {self.assists:2} = {self.total:2}"
    

class PlayerReader:
    def __init__(self, url):
        self.players=self.get_players(url)

    def get_players(self, url):
        self.response = requests.get(url).json()
        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        
        return players
    
    def __iter__(self):
        return iter(self.players)
    

class PlayerStats:
    def __init__(self, players):
        self.players=list(players)
        
    def top_scorers_by_nationality(self, nationality):
        players=[]
        for player in self.players:
            if player.nationality == nationality:
                #nat_player = Player(player)
                players.append(player)
        players.sort(key=lambda p: p.total, reverse=True)

        return players