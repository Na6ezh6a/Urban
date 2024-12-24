# "Систематизация и пропуск тестов".
# Задача "Заморозка кейсов".

import unittest
from runner import Runner
def skip(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print('Тесты в этом кейсе заморожены')
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper
class RunnerTest(unittest.TestCase):
    is_frozen = False
    @skip
    def test_walk(self):
        runner = Runner('Johnny Depp')
        self.assertEqual(runner.distance, 0)
    @skip
    def test_run(self):
        runner = Runner('Willy Wonka')
        for f in range(9):
            runner.run()
        self.assertIn(runner.distance, [9, 19, 21, 90])
    @skip
    def test_challenge(self):
        runner1 = Runner('Edward Scissorhands')
        runner2 = Runner('Jack Sparrow')
        for f in range(10):
            runner1.walk()
            runner2.run()
        self.assertLess(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @skip
    def setUp(self):
        self.runner1 = Runner('Уэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in sorted(cls.all_results.items()):
            print(value)

    @skip
    def test_race1(self):
        race1 = Tournament(90, self.runner1, self.runner3)
        result = race1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race1'] = {place: str(runner) for place, runner in result.items()}

    @skip
    def test_race2(self):
        race2 = Tournament(90, self.runner2, self.runner3)
        result = race2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race2'] = {place: str(runner) for place, runner in result.items()}

    @skip
    def test_race3(self):
        race3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        result = race3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ник всегда должен быть последним!')
        self.all_results['test_race3'] = {place: str(runner) for place, runner in result.items()}

if __name__ == '__main__':
    unittest.main()