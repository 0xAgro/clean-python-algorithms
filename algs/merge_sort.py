def merge_sort(A):
  def merge(l, r):
    res = []
    l, r = l[::-1], r[::-1]

    while l and r:
      if l[-1] > r[-1]:
        res.append(r.pop())
      else:
        res.append(l.pop())
            
      res.extend(l[::-1])
      res.extend(r[::-1])

      return res


  if len(A) <= 1:
    return A

  m = len(A) // 2
  l = self.merge_sort(A[:m])
  r = self.merge_sort(A[m:])

  return merge(l, r)
