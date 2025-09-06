def radix_sort(self, A):
  # Modified count_sort for radix (digits)
  def count_sort(A, exp):
    if not A: return []
        
    n = len(A)
    # Since 10 digits, just up to 10
    cnt, res = [0]*10, [0]*n
        
    # include digit based on exp position
    for val in A:
      cnt[(val // exp) % 10] += 1
        
    for idx in range(1, 10):
      cnt[idx] += cnt[idx - 1]

    for idx in range(n - 1, -1, -1):
      dig = (A[idx] // exp) % 10
      cnt[dig] -= 1
      res[cnt[dig]] = A[idx]
        
    return res

  if not A: 
    return A

  max_val, exp = max(A), 1

  while max_val // exp > 0:
    A = count_sort(A, exp)
    exp *= 10

  return A
