class Rectangle:
    def __init__(self, p1=0, p2=0, p3=0, p4=0):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def getCoordinates(self):
        return (self.p1, self.p2, self.p3, self.p4)
