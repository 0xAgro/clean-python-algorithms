

def count_sort(self, A):
  if not A: 
    return []

  cnt, res = [0]*(max(A) + 1), []

  for val in A:
      cnt[val] += 1

  for val in range(len(cnt)):
      res.extend([val] * cnt[val])

  return res
