import unittest
from src.classes.point import Point

class TestPoint(unittest.TestCase):

    def testInstantiation(self):
        """
        Initialize the point with two values
        """
        point = Point()
        self.assertIsInstance(point, Point)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 0)

    def testWithNegativeValues(self):
        """
        Initialize the point with two negative values
        """
        point = Point(-1, -3)
        self.assertIsInstance(point, Point)
        self.assertEqual(point.x, -1)
        self.assertEqual(point.y, -3)

    def testWithFloatValues(self):
        """
        Initialize the point with two float values
        """
        point = Point(-1.5, 3.3)
        self.assertIsInstance(point, Point)
        self.assertEqual(point.x, -1.5)
        self.assertEqual(point.y, 3.3)    

    def testMethodGetCoordinates(self):
        """
        Returns the coordinates of the point as a tuple
        """
        point = Point(1,1).getCoordinates()
        self.assertEqual(point, (1,1)) 

    def testMethodGetCoordinatesWithDefaults(self):
        """
        Returns the default coordinates of the point as a tuple
        """
        point = Point().getCoordinates()
        self.assertEqual(point, (0,0))

    def testMethodGetCoordinatesWithNegatives(self):
        """
        Returns the coordinates of the point as a tuple with negative inputs
        """
        point = Point(-1,-1).getCoordinates()
        self.assertEqual(point, (-1,-1))             

    def testMethodGetCoordinatesWithFloats(self):
        """
        Returns the coordinates of the point as a tuple with float inputs
        """
        point = Point(-1.5,1).getCoordinates()
        self.assertEqual(point, (-1.5,1))             

if __name__ == '__main__':
    unittest.main()
