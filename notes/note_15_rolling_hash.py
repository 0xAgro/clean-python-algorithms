def rolling_hash(self, s, k):
  if not k:
      return True

  MOD, BASE, res = 10**9 + 7, 31, []
  POW = pow(BASE, k - 1, MOD)

  h = 0
  for c in s[:k]:
      h = (h * BASE + ord(c) - ord('a') + 1) % MOD

  for idx in range(k, len(s) + 1):
      res.append(h)
                    
      if idx != len(s): 
          l = ord(s[idx - k]) - ord('a') + 1
          r = ord(s[idx]) - ord('a') + 1

          h = (h - l * POW) % MOD
          h = (h * BASE + r) % MOD

  return len(set(res)) != len(res)
