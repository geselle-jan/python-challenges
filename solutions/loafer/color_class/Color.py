class Color():
    def __init__(self, r = -1, g = -1, b = -1, h = -1, s = -1, l = -1):
        self._r = r
        self._g = g
        self._b = b
        self._h = h
        self._s = s
        self._l = l
        if r > -1 and g > -1 and b > -1:
            self.calculate_hsl()
        elif h > -1 and s > -1 and l > -1:
            self.calculate_rgb()
        else:
            raise ValueError('Specify "r", "g" and "b" or "h", "s" and "l"!')

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value
        self.calculate_hsl()

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value
        self.calculate_hsl()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value
        self.calculate_hsl()

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value
        self.calculate_rgb()

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, value):
        self._s = value
        self.calculate_rgb()

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, value):
        self._l = value
        self.calculate_rgb()

    def __str__(self):
        return "#{0:02x}{1:02x}{2:02x}".format(self.r, self.g, self.b)

    def calculate_hsl(self):

        r = (self.r / 255)
        g = (self.g / 255)
        b = (self.b / 255)

        value_min = min(r, g, b)
        value_max = max(r, g, b)
        delta_max = value_max - value_min

        l = (value_max + value_min) / 2

        if delta_max == 0:

            h = s = 0

        else:

            if l < 0.5:
                s = delta_max / (value_max + value_min)
            else:
                s = delta_max / (2 - value_max - value_min)

            delta_r = (((value_max - r) / 6) + (delta_max / 2)) / delta_max
            delta_g = (((value_max - g) / 6) + (delta_max / 2)) / delta_max
            delta_b = (((value_max - b) / 6) + (delta_max / 2)) / delta_max

            if r == value_max:
                h = delta_b - delta_g
            elif g == value_max:
                h = ( 1 / 3 ) + delta_r - delta_b
            elif b == value_max:
                h = ( 2 / 3 ) + delta_g - delta_r

            if h < 0:
                h += 1
            if h > 1:
                h -= 1

        self._h = round(h * 360)
        self._s = round(s * 100)
        self._l = round(l * 100)

    def hue_to_rgb(self, v1, v2, vh):
        if vh < 0:
            vh += 1
        if vh > 1:
            vh -= 1
        if (6 * vh) < 1:
            return v1 + ( v2 - v1 ) * 6 * vh
        if (2 * vh) < 1:
            return v2
        if (3 * vh) < 2:
            return v1 + ( v2 - v1 ) * ( ( 2 / 3 ) - vh ) * 6
        return v1

    def calculate_rgb(self):

        h = (self.h / 360)
        s = (self.s / 100)
        l = (self.l / 100)

        if s == 0:
            r = g = b = l * 255
        else:
            if l < 0.5:
                v2 = l * ( 1 + s )
            else:
                v2 = ( l + s ) - ( s * l )

            v1 = 2 * l - v2

            r = 255 * self.hue_to_rgb(v1, v2, h + (1 / 3))
            g = 255 * self.hue_to_rgb(v1, v2, h)
            b = 255 * self.hue_to_rgb(v1, v2, h - (1 / 3))

        self._r = round(r)
        self._g = round(g)
        self._b = round(b)






