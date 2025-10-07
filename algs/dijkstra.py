class Solution:
    def networkDelayTime(self, T: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        for u, v, w in T:
            g[u].append((v, w))

        dis = [float(inf)]*n
        dis[k - 1] = 0

        h = [(0, k)]
        heapify(h)
        seen = set()

        while h:
            cur_dis, node = heappop(h)

            if node in seen:
                continue
            seen.add(node)

            for adj, w in g[node]:
                if adj not in seen and w + cur_dis < dis[adj - 1]:
                    dis[adj - 1] = cur_dis + w
                    heappush(h, (dis[adj - 1], adj))

        if float(inf) in dis:
            return -1
        return max(dis)
