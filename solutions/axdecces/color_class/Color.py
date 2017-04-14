class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        pass

    @property
    def h(self):
        if self.r / 255 == max(self.calculateHSL):
            return (self.g - self.b) / (max(self.calculateHSL) - min(self.calculateHSL)) * 60
        if self.g / 255 == max(self.calculateHSL):
            return (self.b - self.r) / (max(self.calculateHSL) - min(self.calculateHSL)) * 60
        if self.b / 255 == max(self.calculateHSL):
            return (self.r - self.g) / (max(self.calculateHSL) - min(self.calculateHSL)) * 60

    @h.setter
    def h(self, h, s, l):
        self.r = None
        self.g = None
        self.b = None

    @property
    def s(self):
        if max(self.calculateHSL) == min(self.calculateHSL):
            return 0
        if self.l < 0.5:
            return round((max(self.calculateHSL) - min(self.calculateHSL)) / (max(self.calculateHSL) + min(self.calculateHSL)), 2) * 100
        if self.l > 0.5:
            return round((max(self.calculateHSL) - min(self.calculateHSL)) / (2.0 - max(self.calculateHSL) - min(self.calculateHSL)), 2) * 100

    @s.setter
    def s(self, h, s, l):
        self.r = None
        self.g = None
        self.b = None

    @property
    def l(self):
        self.calculateHSL = []
        self.calculateHSL.append(self.r / 255 * 1.0)
        self.calculateHSL.append(self.g / 255 * 1.0)
        self.calculateHSL.append(self.b / 255 * 1.0)
        return round((max(self.calculateHSL) + min(self.calculateHSL)) / 2, 2) * 100

    @l.setter
    def l(self, h, s, l):
        self.r = None
        self.g = None
        self.b = None
