def longestSubarray(self, A: List[int]) -> int:
  l, zeros, res = 0, 0, 0

  for r, val in enumerate(A):
    zeros += not val

    while zeros > 1:
      zeros -= not A[l]
      l += 1

    res = max(res, r - l)
            
  return res
