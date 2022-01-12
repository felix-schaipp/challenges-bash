import unittest
from src.classes.intersector import Intersector
from src.classes.rectangle import Rectangle

class TestIntersector(unittest.TestCase):
    def testMethodFindBottomLeftCorner(self):
        """
        Finds the bottom left corner for a given rectangle
        """
        intersector = Intersector()
        rectangle = Rectangle().getCoordinates()
        self.assertEqual(intersector.findBottomLeftCorner(rectangle), (0,0))

    def testMethodFindTopRightCorner(self):
        """
        Finds the top right corner for a given rectangle
        """
        intersector = Intersector()
        rectangle = Rectangle().getCoordinates()
        self.assertEqual(intersector.findTopRightCorner(rectangle), (1,1))

    def testMethodFindCorners(self):
        """
        Finds the bottom left and top right corner for a given rectangle
        """
        intersector = Intersector()
        rectangle = Rectangle().getCoordinates()
        self.assertEqual(intersector.findCorners(rectangle), [0,0,1,1])

    def testMethodCheckIntersectionPositive(self):
        """
        Returns true for intersecting rectangles
        """
        intersector = Intersector()
        rectangle1 = Rectangle().getCoordinates()
        rectangle2 = Rectangle((0.5,0.5), (0.5,1.5), (1.5, 0.5), (1.5, 1.5)).getCoordinates()
        corners1 = intersector.findCorners(rectangle1)
        corners2 = intersector.findCorners(rectangle2)
        self.assertEqual(intersector.checkIntersection(corners1, corners2), True)

    def testMethodCheckIntersectionNegative(self):
        """
        Returns false for intersecting rectangles
        """
        intersector = Intersector()
        rectangle1 = Rectangle().getCoordinates()
        rectangle2 = Rectangle((10,10), (10,11), (11, 10), (11, 11)).getCoordinates()
        corners1 = intersector.findCorners(rectangle1)
        corners2 = intersector.findCorners(rectangle2)
        self.assertEqual(intersector.checkIntersection(corners1, corners2), False)

if __name__ == '__main__':
    unittest.main()
