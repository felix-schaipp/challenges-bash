import unittest
import json
from src.classes.rectanglePairJSONGenerator import RectanglePairJSONGenerator

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
        rectangle = generator.generateRectangle()
        self.assertEqual(type(rectangle), tuple )    
        self.assertEqual(len(rectangle), 4 )

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
