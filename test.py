import unittest
import main


class TestMain(unittest.TestCase):
    def test_addition(self):
        num = 10
        result = main.addition(num)
        self.assertEqual(result, 15)

    def test_calculate_average(self):
        self.assertIsNone(main.calculate_average([]))
        self.assertEquals(main.calculate_average([1, 2, 3, 4, 5]) == 3.0)
        self.assertEquals(main.calculate_average([0]) == 0.0)
        self.assertEquals(main.calculate_average([10, 20, 30, 40, 50]) == 30.0)


unittest.main()
