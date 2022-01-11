from classes.rectanglePairJSONGenerator import RectanglePairJSONGenerator

if __name__ == "__main__":
    pairsToGenerate = int(input("How many rectangles should be created?: "))
    if(pairsToGenerate < 1):
        print(print("Please enter a number bigger than 0"))
        exit(1)
    generator = RectanglePairJSONGenerator(pairsToGenerate)
    generator.generatePairs()
    generator.saveToJson()
    print(f"We created a json file (rectangle-pairs.json) with {pairsToGenerate} pairs of rectangles for you...")
    
    # read in the generated json
    # let a checker class run through to the pairs
    # pretty print the output of the check
