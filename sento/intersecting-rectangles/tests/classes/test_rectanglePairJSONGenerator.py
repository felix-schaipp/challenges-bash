import unittest
from pathlib import Path
import os
import json
from src.classes.rectanglePairJSONGenerator import RectanglePairJSONGenerator

class TestRectanglePairJSONGenerator(unittest.TestCase):

    def testInstantiation(self):
        generator = RectanglePairJSONGenerator()
        self.assertIsInstance(generator, RectanglePairJSONGenerator)
        self.assertEqual(generator.numberOfPairs, 1)
        self.assertEqual(generator.rectanglePairStorage, {})

    def testMethodGenerateRectangle(self):
        generator = RectanglePairJSONGenerator()
        rectangle = generator.generateRectangle()
        self.assertEqual(type(rectangle), tuple )    
        self.assertEqual(len(rectangle), 4 )

    def testMethodGenerateRectanglePairError(self):
        generator = RectanglePairJSONGenerator()
        self.assertRaises(TypeError, lambda: generator.generateRectanglePair())
    
    def testMethodGenerateRectanglePair(self):
        generator = RectanglePairJSONGenerator()
        pair = generator.generateRectanglePair(1)
        self.assertEqual(type(pair), dict)
        self.assertIn('r1-1', pair)
        self.assertIn('r1-2', pair)

    def testMethodGeneratePairs(self):
        generator = RectanglePairJSONGenerator()
        generator.generatePairs()
        pair1Key = 'pair-1'
        self.assertIn(pair1Key,generator.rectanglePairStorage)
        self.assertIn('r1-1', generator.rectanglePairStorage[pair1Key])
        self.assertIn('r1-2', generator.rectanglePairStorage[pair1Key])

    def testMethodSaveToJson(self):
        generator = RectanglePairJSONGenerator()
        generator.saveToJson()
        BASE_PATH = str(Path(__file__).parents[2].absolute())
        PATH = os.path.join(BASE_PATH, 'src', 'rectangle-pairs.json')
        with open(PATH) as json_file:
            data = json.load(json_file)
            self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()
