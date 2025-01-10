# Логирование
# Задача "Логирование бегунов".
import logging
import unittest
from rt_with_exceptions import Runner
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            first = Runner('Johnny Depp', -9)
            for i in range(9):
                first.walk()
            self.assertEqual(first.distance, 100)
            logging.info('"test_walk" выполнен успешно')

        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            second = Runner(1921)
            for i in range(9):
                second.run()
            self.assertEqual(second.distance, 200)
            logging.info('"test_walk" выполнен успешно')

        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='utf-8', format='%(levelname)s | %(message)s')
    unittest.main()

