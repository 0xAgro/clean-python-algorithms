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



# CONSIDER ADDING: def bitmask_idx(self, mask):
        '''
        res = []
        idx = 0
        while mask:
            if mask & 1:
                res.append(idx)
            mask >>= 1
            idx += 1
        return res
    '''
