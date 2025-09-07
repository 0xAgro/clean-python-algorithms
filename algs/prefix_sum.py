# Clean up later
def subarraySum(self, A: List[int], k: int) -> int:
  s = Counter()
  s[0] = 1
  res = 0
  pre = 0

  for a in A:
    pre += a
    if pre - k in s:
      res += s[pre - k]
    s[pre] += 1
            
  return res
