from math import atan2, pi

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        distanceX = point.x - self.x
        distanceY = point.y - self.y
        return (distanceX ** 2 + distanceY ** 2) ** .5

    def angle_to(self, point):
        deltaX = point.x - self.x
        deltaY = point.y - self.y
        radAngle = atan2(deltaY, deltaX)
        return 180 * radAngle / pi
