def maxArea(self, H: List[int]) -> int:
        l, r = 0, len(H) - 1
        m = 0

        while l < r:
            w = r - l
            cur_h = min(H[l], H[r])
            m = max(m, w * cur_h)

            if H[l] < H[r]:
                l += 1
            else:
                r -= 1
        
        return m
