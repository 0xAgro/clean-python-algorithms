# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #15 Rolling Hash here: <https://youtu.be/1KPtZ7eaO7Y>
# ==============================

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


# Rolling hash class to avoid mental overhead
class RollingHash:

  def __init__(self, s = ""):
    self.hash = 0
    self.length = 0
    self.pow = [1]
    self.MOD = 2**61 - 1
    self.BASE = 1315423911

    for c in s:
        self.append(c)

  def check_pow(self, n):
    while len(self.pow) <= n:
      self.pow.append((self.pow[-1] * self.BASE) % self.MOD)

  def append(self, c):
    val = ord(c) - ord('a') + 1
    self.hash = (self.hash * self.BASE + val) % self.MOD
    self.length += 1

  def appendleft(self, c):
    val = ord(c) - ord('a') + 1
    self.check_pow(self.length) 
    self.hash = (val * self.pow[self.length] + self.hash) % self.MOD
    self.length += 1

  def pop(self, c):
    val = ord(c) - ord('a') + 1
    inv_base = pow(self.BASE, self.MOD-2, self.MOD)
    self.hash = (self.hash - val) * inv_base % self.MOD
    self.length -= 1

  def popleft(self, c):
    val = ord(c) - ord('a') + 1
    self.check_pow(self.length-1)
    self.hash = (self.hash - val * self.pow[self.length-1]) % self.MOD
    self.length -= 1
