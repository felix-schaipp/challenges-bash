import unittest
from src.classes.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def testInstantiation(self):
        rectangle = Rectangle()
        self.assertIsInstance(rectangle, Rectangle)

    def testMethodGetCoordinates(self):
        rectangle = Rectangle(1,2,3,4).getCoordinates()
        self.assertEqual(rectangle, (1,2,3,4)) 

    def testMethodGetCoordinatesWithDefaults(self):
        rectangle = Rectangle().getCoordinates()
        self.assertEqual(rectangle, (0,0,0,0))

    def testMethodGetCoordinatesWithNegatives(self):
        rectangle = Rectangle(-1,-1,-4,-8).getCoordinates()
        self.assertEqual(rectangle, (-1,-1,-4,-8))       
    
    def testMethodGetCoordinatesWithFloats(self):
        rectangle = Rectangle(-1,-1,-4,-8.5).getCoordinates()
        self.assertEqual(rectangle, (-1,-1,-4,-8.5))       

if __name__ == '__main__':
    unittest.main()
