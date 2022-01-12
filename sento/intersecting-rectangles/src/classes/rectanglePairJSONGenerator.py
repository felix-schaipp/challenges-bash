import random
import json
from .point import Point
from .rectangle import Rectangle

class RectanglePairJSONGenerator:
    def __init__(self, numberOfPairs=1):
        self.numberOfPairs = numberOfPairs
        self.rectanglePairStorage = {}

    def generateRectangle(self):
        p1 = Point(random.randint(1, 100), random.randint(1, 100)).getCoordinates()
        p2 = Point(random.randint(1, 100), random.randint(1, 100)).getCoordinates()
        p3 = Point(random.randint(1, 100), random.randint(1, 100)).getCoordinates()
        p4 = Point(random.randint(1, 100), random.randint(1, 100)).getCoordinates()
        return Rectangle(p1,p2,p3,p4).getCoordinates()

    def generateRectanglePair(self, pairNumber):
        rectangle1 = self.generateRectangle()
        rectangle2 = self.generateRectangle()
        return { f"r{pairNumber}-1": rectangle1, f"r{pairNumber}-2": rectangle2 }

    def generatePairs(self):
        for i in range(self.numberOfPairs):
            self.rectanglePairStorage[f"pair-{i+1}"] = self.generateRectanglePair(i+1)

    def saveToJson(self, path):
        if len(path) == 0 or path == None:
            raise ValueError("You must define a path to save your pairs")
        with open(path, 'w') as outputFile:
            json.dump(self.rectanglePairStorage, outputFile, indent=2, sort_keys=True)
