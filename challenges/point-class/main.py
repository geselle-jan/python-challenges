import unittest
from Point import Point


class TestPointClass(unittest.TestCase):

    def setUp(self):
        self.points = [
            Point( 0,  0),
            Point(10, 10)
        ]

    def test_distance(self):
        dist1 = self.points[0].distance_to(self.points[1])
        self.assertAlmostEqual(dist1, 14.14, 2)

    def test_angle(self):
        angle1 = self.points[0].angle_to(self.points[1])
        self.assertAlmostEqual(angle1, 45.0, 1)


if __name__ == '__main__':
    unittest.main()