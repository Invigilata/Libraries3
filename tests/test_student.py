import unittest
from main import Student

class TestStudent(unittest.TestCase):

    def test_walk_10_times(self):
        student = Student("Walker")
        for _ in range(10):
            student.walk()

        expected_distance = 50
        actual_distance = student.distance

        self.assertEqual(expected_distance, actual_distance, f"Дистанции не равны {actual_distance} != {expected_distance}")

    def test_run_10_times(self):
        student = Student("Runner")
        for _ in range(10):
            student.run()

        expected_distance = 100
        actual_distance = student.distance

        self.assertEqual(expected_distance, actual_distance, f"Дистанции не равны {actual_distance} != {expected_distance}")

    def test_competition_walk_vs_run(self):
        runner = Student("Runner")
        walker = Student("Walker")

        for _ in range(10):
            runner.run()
            walker.walk()

        self.assertGreater(runner.distance, walker.distance,
                           f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}")

if __name__ == '__main__':
    unittest.main()
