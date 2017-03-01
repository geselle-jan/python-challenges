class Leftpad():
    def __init__(self, value, length):
        self.value = value
        self.length = length

        if len(str(self.value)) < self.length:
            self.numberOf0 = int(self.length) - len(str(self.value))
            self.output = []
            while self.numberOf0 > 0:
                self.output.append('0')
                self.numberOf0 -= 1
            self.output.append(self.value)
            if self.numberOf0 < 0:
                self.output = []
                self.output.append(str(self.value)[-int(self.length):])