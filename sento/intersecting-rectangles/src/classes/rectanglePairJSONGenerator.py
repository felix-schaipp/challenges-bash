import random
import json
import math
from .point import Point
from .rectangle import Rectangle

class RectanglePairJSONGenerator:
    def __init__(self, numberOfPairs=1):
        self.numberOfPairs = numberOfPairs
        self.rectanglePairStorage = {}

    def generateRectangle(self, length: int) -> tuple:
        # based on https://www.geeksforgeeks.org/find-corners-of-rectangle-using-mid-points/
        # generate two random mid points
        p = Point(random.randint(1, 10), random.randint(1, 10))
        q = Point(random.randint(1, 10), random.randint(1, 10))

        # define corner points with defaults
        a,b,c,d = Point(), Point(), Point(), Point() 
        # Horizontal rectangle
        if (p.x == q.x):
            a.x = p.x - (length / 2.0)
            a.y = p.y
            
            d.x = p.x + (length / 2.0)
            d.y = p.y
            
            b.x = q.x - (length / 2.0)
            b.y = q.y
            
            c.x = q.x + (length / 2.0)
            c.y = q.y
            
        # Vertical rectangle
        elif (p.y == q.y):
            a.y = p.y - (length / 2.0)
            a.x = p.x
            
            d.y = p.y + (length / 2.0)
            d.x = p.x
            
            b.y = q.y - (length / 2.0)
            b.x = q.x
            
            c.y = q.y + (length / 2.0)
            c.x = q.x
        
        # Slanted rectangle
        else:
            
            # Calculate slope of the side
            m = (p.x - q.x) / (q.y - p.y)
            
            # Calculate displacements along axes
            dx = (length / math.sqrt(1 + (m * m))) * 0.5 
            dy = m * dx
            
            a.x = p.x - dx
            a.y = p.y - dy
            
            d.x = p.x + dx
            d.y = p.y + dy
            
            b.x = q.x - dx
            b.y = q.y - dy
            
            c.x = q.x + dx
            c.y = q.y + dy

        return Rectangle(a.getCoordinates(),b.getCoordinates(),c.getCoordinates(),d.getCoordinates()).getCoordinates()

    def generateRectanglePair(self, pairNumber: int) -> dict[str, tuple]:
        length1 = random.randint(3,6)
        length2 = random.randint(3,6)
        rectangle1 = self.generateRectangle(length1)
        rectangle2 = self.generateRectangle(length2)
        return { f"r{pairNumber}-1": rectangle1, f"r{pairNumber}-2": rectangle2 }

    def generatePairs(self):
        for i in range(self.numberOfPairs):
            self.rectanglePairStorage[f"pair-{i+1}"] = self.generateRectanglePair(i+1)

    def saveToJson(self, path):
        if len(path) == 0 or path == None:
            raise ValueError("You must define a path to save your pairs")
        with open(path, 'w') as outputFile:
            json.dump(self.rectanglePairStorage, outputFile, indent=2)
