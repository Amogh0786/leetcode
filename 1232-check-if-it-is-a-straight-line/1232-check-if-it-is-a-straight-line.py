class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y - y0) * dx != (x - x0) * dy:
                return False
        return True