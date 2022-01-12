import unittest
import json
import math
from src.classes.rectanglePairJSONGenerator import RectanglePairJSONGenerator
from src.classes.point import Point

# helper function to check if we really generate rectangles here
def isRectangle(a: Point, b: Point, c: Point, d: Point, precision = 1E-6) -> bool:
    cx = (a.x + b.x + c.x + d.x) / 4
    cy = (a.y + b.y + c.y + d.y) / 4

    dd1=pow(cx-a.x, 2)+pow(cy-a.y, 2)
    dd2=pow(cx-b.x, 2)+pow(cy-b.y, 2)
    dd3=pow(cx-c.x, 2)+pow(cy-c.y, 2)
    dd4=pow(cx-d.x, 2)+pow(cy-d.y, 2)

    return math.isclose(dd1, dd2, rel_tol=precision) and math.isclose(dd1, dd3, rel_tol=precision) and math.isclose(dd1, dd4, rel_tol=precision)

class TestRectanglePairJSONGenerator(unittest.TestCase):

    def testInstantiation(self):
        """
        Initialize correctly
        """
        generator = RectanglePairJSONGenerator()
        self.assertIsInstance(generator, RectanglePairJSONGenerator)
        self.assertEqual(generator.numberOfPairs, 1)
        self.assertEqual(generator.rectanglePairStorage, {})

    def testMethodGenerateRectangle(self):
        """
        Generates a rectangle with four point values
        """
        generator = RectanglePairJSONGenerator()
        rectangle = generator.generateRectangle(2)
        self.assertEqual(type(rectangle), tuple )    
        self.assertEqual(len(rectangle), 4 )
        p1 = Point(rectangle[0][0], rectangle[0][1])
        p2 = Point(rectangle[1][0], rectangle[1][1])
        p3 = Point(rectangle[2][0], rectangle[2][1])
        p4 = Point(rectangle[3][0], rectangle[3][1])
        
        self.assertTrue(isRectangle(p1,p2,p3,p4))

    def testMethodGenerateRectanglePairError(self):
        """
        Raises an error if no pairNumber is provided
        """
        generator = RectanglePairJSONGenerator()
        self.assertRaises(TypeError, lambda: generator.generateRectanglePair())
    
    def testMethodGenerateRectanglePair(self):
        """
        Generates a pair of random rectangles
        """
        generator = RectanglePairJSONGenerator()
        pair = generator.generateRectanglePair(1)
        self.assertEqual(type(pair), dict)
        self.assertIn('r1-1', pair)
        self.assertIn('r1-2', pair)

    def testMethodGeneratePairs(self):
        """
        Add the generated pair to the class storage 
        """
        generator = RectanglePairJSONGenerator()
        generator.generatePairs()
        pair1Key = 'pair-1'
        self.assertIn(pair1Key,generator.rectanglePairStorage)
        self.assertIn('r1-1', generator.rectanglePairStorage[pair1Key])
        self.assertIn('r1-2', generator.rectanglePairStorage[pair1Key])

    def testMethodSaveToJson(self):
        """
        Saves the class storage to json
        """
        generator = RectanglePairJSONGenerator()
        PATH = './tests/classes/test_rectangle-pairs.json'
        generator.saveToJson(PATH)
        with open(PATH) as json_file:
            data = json.load(json_file)
            self.assertEqual(data, {})

    def testMethodSaveToJsonError(self):
        """
        Raises an error if no path is provided
        """
        generator = RectanglePairJSONGenerator()
        self.assertRaises(TypeError, lambda: generator.saveToJson())

    def testIntegration(self):
        """
        Saves class storage with data to json
        """
        generator = RectanglePairJSONGenerator(1)
        generator.generatePairs()
        PATH = './tests/classes/test_rectangle-pairs.json'
        generator.saveToJson(PATH)
        with open(PATH) as json_file:
            data = json.load(json_file)
            pair1Key = 'pair-1'
            self.assertIn(pair1Key, data)
            self.assertIn('r1-1', data[pair1Key])
            self.assertIn('r1-2', data[pair1Key])      

if __name__ == '__main__':
    unittest.main()
