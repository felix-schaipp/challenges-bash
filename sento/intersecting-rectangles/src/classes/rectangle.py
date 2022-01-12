class Rectangle:
    def __init__(self, p1=(0,0), p2=(0,1), p3=(1,0), p4=(1,1)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def getCoordinates(self):
        if (type(self.p1) != tuple or type(self.p2) != tuple or type(self.p3) != tuple or type(self.p4) != tuple):
            raise ValueError("Point must be a tuple")
        return (self.p1, self.p2, self.p3, self.p4)
