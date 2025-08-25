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
