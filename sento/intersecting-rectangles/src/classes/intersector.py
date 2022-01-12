class Intersector:
    def findBottomLeftCorner(self, coordinates):
        return min(coordinates, key=lambda point: point[0] and point[1])

    def findTopRightCorner(self, coordinates):
        return max(coordinates, key=lambda point: point[0] and point[1])

    def findCorners(self, coordinates):
        topRight = self.findTopRightCorner(coordinates)
        bottomLeft = self.findBottomLeftCorner(coordinates)
        return list(bottomLeft + topRight)

    def checkIntersection(self, corners1, corners2):
        # after obtaining the corners we can check for 
        # intersection if the area of intersection is positive,
        # since they only touch if corners or edges do not overlap
        if(corners1[0] >= corners2[2]) or (corners1[2] <= corners2[0]) or (corners1[3] <= corners2[1]) or (corners1[1] >= corners2[3]): 
            return False
        return True
