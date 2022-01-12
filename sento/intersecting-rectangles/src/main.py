from classes.rectanglePairJSONGenerator import RectanglePairJSONGenerator
from classes.intersector import Intersector
from classes.terminalColors import TerminalColors
import json

def prettyOutput(bool, debug=False):
    if not bool:
        if debug:
            return f"{TerminalColors.FAIL}The two rectangles (R1{corners1} and R2{corners2}) are not intersecting.{TerminalColors.ENDC}"
        return f"{TerminalColors.FAIL}The two rectangles are not intersecting.{TerminalColors.ENDC}"
    if debug:
        return f"{TerminalColors.OKGREEN}The two rectangles (R1{corners1} and R2{corners2}) are intersecting.{TerminalColors.ENDC}"
    return f"{TerminalColors.OKGREEN}The two rectangles are intersecting.{TerminalColors.ENDC}"

if __name__ == "__main__":
    pairsToGenerate = int(input("How many rectangle pairs should be created?: "))
    if(pairsToGenerate < 1):
        print(print("Please enter a number bigger than 0"))
        exit(1)

    generator = RectanglePairJSONGenerator(pairsToGenerate)
    generator.generatePairs()

    PATH = './src/rectangle-pairs.json'
    generator.saveToJson(PATH)
    print(f"We created a json file (rectangle-pairs.json) with {pairsToGenerate} pairs of rectangles for you...")

    with open(PATH) as json_file:
            data = json.load(json_file)
            if not bool(data):
                raise ValueError("The saved files seems to be empty. Please try again")
            for index,pair in enumerate(data):
                intersector = Intersector()
                rectangle1 = data[pair][f"r{index+1}-1"]
                rectangle2 = data[pair][f"r{index+1}-2"]
                corners1 = intersector.findCorners(rectangle1)
                corners2 = intersector.findCorners(rectangle2)
                result = intersector.checkIntersection(corners1, corners2)
                print(prettyOutput(result))
