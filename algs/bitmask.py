class Bitmask:
    def __init__(self):
        self.mask = 0

    def add(self, i):
        self.mask |= (1 << i)

    def flip(self, i):
        self.mask ^= (1 << i)

    def delete(self, i):
        self.mask &= ~(1 << i)

    def read(self, i):
        return (self.mask >> i) & 1
