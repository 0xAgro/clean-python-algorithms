def gen_factors(self, n):
  res = set()

  for fac in range(1, int(sqrt(n)) + 1):
    if n % fac == 0:
      res.add(fac)
      res.add(n // fac)

  return list(res)
