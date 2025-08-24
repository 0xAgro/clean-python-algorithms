# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #14 Counting Sort here: <>
# ==============================

def count_sort(self, A):
  if not A: 
    return []

  cnt, res = [0]*(max(A) + 1), []

  for val in A:
      cnt[val] += 1

  for val in range(len(cnt)):
      res.extend([val] * cnt[val])

  return res
