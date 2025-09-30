class Solution:
    def findOrder(self, n: int, P: List[List[int]]) -> List[int]:
        if not self.noCycle(n, P):
            return []

        g = [[] for _ in range(n)]
        res = []

        for a, b in P:
            g[b].append(a)

        seen = set()
        stack = [(i, False) for i in range(n)]

        while len(stack):
            node, flag = stack.pop()

            if node in seen and not flag:
                continue

            if flag:
                res.append(node)
                seen.add(node)
                continue

            stack.append((node, True))
            for adj in g[node]:
                if adj not in seen:
                    stack.append((adj, False))

        return res[::-1]

    def noCycle(self, n, P):
        g = [[] for _ in range(n)]
        for a, b in P:
            g[b].append(a)

        stack = [(i, 0 | (1 << i)) for i in range(n)]

        s = 0

        while len(stack):
            node, seen = stack.pop()

            if (s >> node) & 1:
                continue
            s |= (1 << node)

            for adj in g[node]:
                if (seen >> adj) & 1:
                    return False
                stack.append((adj, seen | (1 << adj)))

        return True
