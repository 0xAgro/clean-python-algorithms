# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note # Interval Merge here: <>
# ==============================

def merge(self, I):
  I.sort()
  res = []

  for s, e in I:
    if not res or s > res[-1][1]:
      res.append([s, e])
    else:
      res[-1][1] = max(res[-1][1], e)

  return res
