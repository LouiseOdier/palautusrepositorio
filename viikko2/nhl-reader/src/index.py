import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Oliot:")

    #player_dict ={}
    fin_players = []

    for player in players:
        if player.nationality == "FIN":
            #print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists} total {player.total}")
            #fin_player = Player(player)
            fin_players.append(player)

    
    for player in fin_players:
        #if player.nationality == "FIN":
        print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists} total {player.total}")

    fin_players.sort(key=lambda p: p.total, reverse=True)
    for player in fin_players:
        #if player.nationality == "FIN":
        print(f"{player.name} \t {player.team} \t {player.goals} + {player.assists} = {player.total}")

    #print(fin_players)

    #print(player.print_players())

if __name__ == "__main__":
    main()

#Juuso Välimäki team UTA  goals 2 assists 3
