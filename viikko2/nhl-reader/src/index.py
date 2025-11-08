import requests
from player import Player, PlayerReader, PlayerStats
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

def main():

    valid_nationalities = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA", "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "AUS"]
    nationality = Prompt.ask("Nationality", choices=valid_nationalities)


    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console = Console()
    table = Table(title=f"Season 2024-25 players from {nationality}")

    table.add_column("Name", style="#ff69b4")       
    table.add_column("Team", style="#ffb6c1")        
    table.add_column("Points", justify="right", style="#db7093") 

    for player in players:
        table.add_row(player.name, player.team, str(player.points))

    console.print(table)

if __name__ == "__main__":
    main()


