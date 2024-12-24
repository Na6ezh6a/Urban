# Задача "Проверка на выносливость".
from unittest import TestCase, main
from runner import Runner
class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Johnny Depp')
        for f in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    def test_run(self):
        runner = Runner('Willy Wonka')
        for f in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    def test_challenge(self):
        runner1 = Runner('Edward Scissorhands')
        runner2 = Runner('Jack Sparrow')
        for f in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == '__main__':
    main()