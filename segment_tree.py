# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #13 Segment Tree here: <https://youtu.be/KJAtdznmCG8>
# ==============================

class SegTree:

  def __init__(self, A):  
    self.n = len(A)
    self.tree = [0] * (2*self.n)

    for idx, val in enumerate(A):
        self.tree[self.n + idx] = val

    for idx in range(self.n - 1, 0, -1):
        self.tree[idx] = self.tree[2*idx] + self.tree[2*idx + 1]

  def update(self, idx, val):
      idx += self.n
      self.tree[idx] = val
  
      idx //= 2
      while idx:
          self.tree[idx] = self.tree[2*idx] + self.tree[2*idx + 1]
          idx //= 2

  def query(self, l, r):
      l += self.n
      r += self.n
      res = 0

      while l <= r:
          if l % 2 == 1:
              res += self.tree[l]
              l += 1
          if r % 2 == 0:
              res += self.tree[r]
              r -= 1

          l //= 2
          r //= 2

      return res    
