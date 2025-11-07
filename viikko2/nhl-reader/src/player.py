class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.total = dict['goals']+dict['assists']
    #    self.player_list = []
    
    #def players_list(self, player):
    #    self.player_list.append(player)
    #    print(player)
    
    def print_players(self):
        print(self.player_list)
        return self.player_list

    def sort(self, players):
        pass

    
    def __str__(self):
        return self.name

class PlayerReader:
    pass
class PlayerStats:

    def top_scorers_by_nationality():
        pass