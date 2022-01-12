import unittest
from src.classes.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def testInstantiation(self):
        """
        Initialize the rectangle with four point values
        """
        rectangle = Rectangle()
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.p1, (0,0))
        self.assertEqual(rectangle.p2, (0,1))
        self.assertEqual(rectangle.p3, (1,0))
        self.assertEqual(rectangle.p4, (1,1))

    def testMethodGetCoordinates(self):
        """
        Returns the coordinates in tuple form
        """
        p1 = (5,5)
        p2 = (1,5)
        p3 = (5,1)
        p4 = (0,0)
        rectangle = Rectangle(p1,p2,p3,p4).getCoordinates()
        self.assertEqual(rectangle, (p1,p2,p3,p4)) 

    def testMethodGetCoordinatesError(self):
        """
        Raises an error if one of the values is not a tuple
        """
        p1 = (5,5)
        p2 = 1
        p3 = (5,1)
        p4 = (0,0)
        self.assertRaises(ValueError, lambda: Rectangle(p1,p2,p3,p4).getCoordinates())

    def testMethodGetCoordinatesWithDefaults(self):
        """
        Returns the default coordinates in tuple form
        """
        rectangle = Rectangle().getCoordinates()
        self.assertEqual(rectangle, ((0,0),(0,1),(1,0),(1,1)))

    def testMethodGetCoordinatesWithNegatives(self):
        """
        Returns the coordinates with negative inputs
        """
        p1 = (-1,-1)
        p2 = (-1,0)
        p3 = (4,0)
        p4 = (8,2)
        rectangle = Rectangle(p1,p2,p3,p4).getCoordinates()
        self.assertEqual(rectangle, (p1,p2,p3,p4))       
    
    def testMethodGetCoordinatesWithFloats(self):
        """
        Returns the coordinates in tuple form with float inputs
        """
        p1 = (-1,-1)
        p2 = (-1.5,0)
        p3= (4,0)
        p4= (8.5,2)
        rectangle = Rectangle(p1,p2,p3,p4).getCoordinates()
        self.assertEqual(rectangle, (p1,p2,p3,p4))       

if __name__ == '__main__':
    unittest.main()
