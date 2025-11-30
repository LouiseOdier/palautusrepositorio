class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: 0, player2_name: 0}
        self.player1_name = player1_name
        self.player2_name = player2_name

    def won_point(self, player_name):
        new_result = self.players[player_name] + 1
        self.players[player_name] = new_result

    def get_score(self):

        def low_scores(scores):
            result = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
            return result[scores]

        def even_scores(scores):
            result = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
            if scores < 3:
                return result[scores]
            else:
                return "Deuce"
        
        def high_scores(player1, player2):
            if self.players[player1] > self.players[player2]:
                leader, loser = player1, player2
            else:
                leader, loser = player2, player1
            if self.players[leader] - self.players[loser] == 1:
                return f"Advantage {leader}"
            else:
                return f"Win for {leader}"

        if self.players[self.player1_name] == self.players[self.player2_name]:
            return even_scores(self.players[self.player1_name])

        elif self.players[self.player1_name] >= 4 or self.players[self.player2_name] >= 4:
            return high_scores(self.player1_name, self.player2_name)
        
        else:
            return low_scores(self.players[self.player1_name]) + "-" + low_scores(self.players[self.player2_name])