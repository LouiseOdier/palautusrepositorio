import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [Player("Semenko", "EDM", 4, 12), Player("Lemieux", "PIT", 45, 54), Player("Kurri", "EDM", 37, 53), Player("Yzerman", "DET", 42, 56), Player("Gretzky", "EDM", 35, 89)]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_palauttaa_oikean_tiimin(self):
        tiimi=self.stats.team("EDM")
        pelaajat=[]
        for player in tiimi:
            pelaajat.append(player.name)

        self.assertEqual(pelaajat, ["Semenko", "Kurri", "Gretzky"])

    
    #def test_korkeimmat_pisteet(self):
    #    tiimi=self.stats.top(2)
    #    pelaajat=[]
    #    for player in tiimi:
    #        pelaajat.append(player.name)

    #    self.assertEqual(pelaajat, ["Gretzky", "Lemieux", "Yzerman"])

    def test_haku(self):
        tiimi=self.stats.search("Semenko")

        self.assertEqual(tiimi.name, "Semenko")

    def test_tyhja_haku(self):
        tiimi=self.stats.search("kissa")

        self.assertEqual(tiimi, None)

    def test_sort_by_points(self):
        tiimi=self.stats.top(2, SortBy.POINTS)
        pelaajat=[]
        for player in tiimi:
            pelaajat.append(player.name)

        self.assertEqual(pelaajat, ["Gretzky", "Lemieux", "Yzerman"])

    def test_sort_by_goals(self):
        tiimi=self.stats.top(2, SortBy.GOALS)
        pelaajat=[]
        for player in tiimi:
            pelaajat.append(player.name)

        self.assertEqual(pelaajat, ["Lemieux", "Yzerman", "Kurri"])

    def test_sort_by_assits(self):
        tiimi=self.stats.top(2, SortBy.ASSISTS)
        pelaajat=[]
        for player in tiimi:
            pelaajat.append(player.name)

        self.assertEqual(pelaajat, ["Gretzky", "Yzerman", "Lemieux"])

    
