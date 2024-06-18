import unittest
from math import pi
from geometry import rectangle_area, rectangle_perimeter, circle_area, circle_circumference

class TestGeometry(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(3.5, 1), 3.5)
        self.assertEqual(rectangle_area(0, 0), 0)
        with self.assertRaises(ValueError):
            rectangle_area(-10, 2)
            rectangle_area(10, -2)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10)
        self.assertEqual(rectangle_perimeter(3.5, 1), 9.5)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-10, 2)
            rectangle_perimeter(10, -2)

    def test_circle_area(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(1), math.pi)
        self.assertEqual(circle_area(5), 25 * math.pi)
        with self.assertRaises(ValueError):
            circle_area(-10)

    def test_circle_circumference(self):
        self.assertEqual(circle_circumference(0), 0)
        self.assertEqual(circle_circumference(1), 2 * math.pi)
        self.assertEqual(circle_circumference(5), 10 * math.pi)
        with self.assertRaises(ValueError):
            circle_circumference(-10)

if __name__ == '__main__':
    unittest.main()