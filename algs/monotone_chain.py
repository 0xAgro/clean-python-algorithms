# Including border points
def outerTrees(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) < 2:
            return A

        A.sort()

        def cross_prod(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        high, low = [], []

        for a in A:
            while len(low) > 1 and cross_prod(low[-2], low[-1], a) < 0:
                low.pop()
            low.append(tuple(a))

        for a in A[::-1]:
            while len(high) > 1 and cross_prod(high[-2], high[-1], a) < 0:
                high.pop()
            high.append(tuple(a))

        return list(set(low[:-1] + high[:-1]))

# Not border points
def outerTrees(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) < 2:
            return A

        A.sort()

        def cross_prod(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        high, low = [], []

        for a in A:
            while len(low) > 1 and cross_prod(low[-2], low[-1], a) < 1:
                low.pop()
            low.append(a)

        for a in A[::-1]:
            while len(high) > 1 and cross_prod(high[-2], high[-1], a) < 1:
                high.pop()
            high.append(a)

        return low[:-1] + high[:-1]
