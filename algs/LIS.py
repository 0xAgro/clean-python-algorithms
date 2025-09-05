def LIS(self, A):
  res = []
  for a in A:
    idx = bisect_left(res, a)
    if idx == len(res):
      res.append(a)
    else:
      res[idx] = a
  return len(res)
