from math import atan2, pi

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, point):
        a = abs(self.x - point.x)
        b = abs(self.y - point.y)
        return ( (a ** 2) + (b ** 2) ) ** 0.5

    def angle_to(self, point):
        delta_x = point.x - self.x
        delta_y = point.y - self.y
        angle_rad = atan2(delta_y, delta_x)
        angle_deg = angle_rad * 180.0 / pi
        return angle_deg