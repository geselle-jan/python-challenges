import unittest
from Color import Color


class TestColorClass(unittest.TestCase):

    def setUp(self):
        self.rgb = {
            'red':      Color(  r= 255, g=   0, b=   0  ),
            'green':    Color(  r=   0, g= 255, b=   0  ),
            'blue':     Color(  r=   0, g=   0, b= 255  ),
            'yellow':   Color(  r= 255, g= 255, b=   0  ),
            'cyan':     Color(  r=   0, g= 255, b= 255  ),
            'magenta':  Color(  r= 255, g=   0, b= 255  ),
            'white':    Color(  r= 255, g= 255, b= 255  ),
            'black':    Color(  r=   0, g=   0, b=   0  ),
            'random':   Color(  r=  33, g= 212, b=  42  ),
            'purple':   Color(  r= 191, g=  64, b= 191  )
        }
        self.hsl = {
            'red':      Color(  h=   0, s= 100, l=  50  ),
            'green':    Color(  h= 120, s= 100, l=  50  ),
            'blue':     Color(  h= 240, s= 100, l=  50  ),
            'yellow':   Color(  h=  60, s= 100, l=  50  ),
            'cyan':     Color(  h= 180, s= 100, l=  50  ),
            'magenta':  Color(  h= 300, s= 100, l=  50  ),
            'white':    Color(  h=   0, s=   0, l= 100  ),
            'black':    Color(  h=   0, s=   0, l=   0  ),
            'random':   Color(  h= 123, s=  73, l=  48  ),
            'purple':   Color(  h= 300, s=  50, l=  50  )
        }

    def is_same_color(self, color1, color2):
        return (
            color1.r == color2.r
            and
            color1.g == color2.g
            and
            color1.b == color2.b
            and
            color1.h == color2.h
            and
            color1.s == color2.s
            and
            color1.l == color2.l
        )

    def color_test(self, color_name):
        self.assertTrue(
            self.is_same_color(
                self.hsl[color_name],
                self.rgb[color_name]
            )
        )

    def test_value_error_rgb_missing_red(self):
        self.assertRaises(ValueError, lambda: Color(g=255, b=255))

    def test_value_error_rgb_missing_green(self):
        self.assertRaises(ValueError, lambda: Color(r=255, b=255))

    def test_value_error_rgb_missing_blue(self):
        self.assertRaises(ValueError, lambda: Color(r=255, g=255))

    def test_value_error_hsl_missing_hue(self):
        self.assertRaises(ValueError, lambda: Color(s=100, l=100))

    def test_value_error_hsl_missing_saturation(self):
        self.assertRaises(ValueError, lambda: Color(h=0, l=100))

    def test_value_error_hsl_missing_luminance(self):
        self.assertRaises(ValueError, lambda: Color(h=0, s=100))

    def test_red(self):
        self.color_test('red')

    def test_green(self):
        self.color_test('green')

    def test_blue(self):
        self.color_test('blue')

    def test_yellow(self):
        self.color_test('yellow')

    def test_cyan(self):
        self.color_test('cyan')

    def test_magenta(self):
        self.color_test('magenta')

    def test_white(self):
        self.color_test('white')

    def test_black(self):
        self.color_test('black')

    def test_random(self):
        self.color_test('random')

    def test_change_red(self):
        color = self.rgb['cyan']
        color.r = 255
        self.assertTrue(
            self.is_same_color(
                self.rgb['white'],
                color
            )
        )

    def test_change_green(self):
        color = self.rgb['magenta']
        color.g = 255
        self.assertTrue(
            self.is_same_color(
                self.rgb['white'],
                color
            )
        )

    def test_change_blue(self):
        color = self.rgb['yellow']
        color.b = 255
        self.assertTrue(
            self.is_same_color(
                self.rgb['white'],
                color
            )
        )

    def test_change_hue(self):
        color = self.hsl['cyan']
        color.h = 300
        self.assertTrue(
            self.is_same_color(
                self.hsl['magenta'],
                color
            )
        )

    def test_change_saturation(self):
        color = self.hsl['magenta']
        color.s = 50
        self.assertTrue(
            self.is_same_color(
                self.hsl['purple'],
                color
            )
        )

    def test_change_luminance(self):
        color = self.rgb['white']
        color.l = 0
        self.assertTrue(
            self.is_same_color(
                self.rgb['black'],
                color
            )
        )

    def test_str_red(self):
        self.assertEqual(str(self.hsl['red']), '#ff0000')

    def test_str_green(self):
        self.assertEqual(str(self.hsl['green']), '#00ff00')

    def test_str_blue(self):
        self.assertEqual(str(self.hsl['blue']), '#0000ff')

    def test_str_yellow(self):
        self.assertEqual(str(self.hsl['yellow']), '#ffff00')

    def test_str_cyan(self):
        self.assertEqual(str(self.hsl['cyan']), '#00ffff')

    def test_str_magenta(self):
        self.assertEqual(str(self.hsl['magenta']), '#ff00ff')

    def test_str_white(self):
        self.assertEqual(str(self.hsl['white']), '#ffffff')

    def test_str_black(self):
        self.assertEqual(str(self.hsl['black']), '#000000')

    def test_str_random(self):
        self.assertEqual(str(self.hsl['random']), '#21d42a')

    def test_str_purple(self):
        self.assertEqual(str(self.hsl['purple']), '#bf40bf')

if __name__ == '__main__':
    unittest.main()