# "Методы Юнит-тестирования".
from unittest import TestCase, main
from runner_and_tournament import Runner, Tournament
class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    def setUp(self):
        self.runner1 = Runner('Уэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)
    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(value)

    def test_race1(self):
        race1 = Tournament(90, self.runner1, self.runner3)
        result = race1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race1'] = {place: str(runner) for place, runner in result.items()}

    def test_race2(self):
        race2 = Tournament(90, self.runner2, self.runner3)
        result = race2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race2'] = {place: str(runner) for place, runner in result.items()}

    def test_race3(self):
        race3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = race3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race3'] = {place: str(runner) for place, runner in result.items()}

    if __name__ == '__main__':
        main()
