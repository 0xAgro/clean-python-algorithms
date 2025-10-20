class Solution:
    def trap(self, A: List[int]) -> int:
        left, right = list(accumulate(A[::-1], max))[::-1], list(accumulate(A, max))
        res = 0

        for idx, h in enumerate(A):
            if h <= left[idx] and h <= right[idx]:
                res += min(left[idx], right[idx]) - h

        return res        
