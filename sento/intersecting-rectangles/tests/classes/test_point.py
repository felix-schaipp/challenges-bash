import unittest
from src.classes.point import Point

class TestPoint(unittest.TestCase):

    def testInstantiation(self):
        point = Point()
        self.assertIsInstance(point, Point)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def testMethodGetCoordinates(self):
        point = Point(1,1).getCoordinates()
        self.assertEqual(point, (1,1)) 

    def testMethodGetCoordinatesWithDefaults(self):
        point = Point().getCoordinates()
        self.assertEqual(point, (0,0))

    def testMethodGetCoordinatesWithNegatives(self):
        point = Point(-1,-1).getCoordinates()
        self.assertEqual(point, (-1,-1))             

if __name__ == '__main__':
    unittest.main()
