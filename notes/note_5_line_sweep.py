# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #5 Line Sweep here: <https://www.youtube.com/shorts/8V5wkJgs9eU>
# ==============================

# Version shown in the video (expensive)
# I -> [[start, end]]
def line_sweep(self, I):
  A = [0]*(max([e for _, e in I]) + 2) # Setting array size to max end value

  # Add 1 to the start value, subtract 1 from the end
  for s, e in I:
    A[s] = A[s] + 1 
    A[e + 1] = A[e + 1] - 1

  # Running sum
  for idx in range(1, len(A)):
    A[idx] += A[idx - 1]

  return A #returning the interval overlap array

# I -> [[start, end]]
# SortedDict version (less expensive)
def line_sweep_sd(self, I):
  d = SortedDict()

  for s, e in I:
    d[s] = d[s] + 1 if s in d else 1
    d[e] = d[e + 1] - 1 if e + 1 in d else -1

  res, cnt = 0, 0 

  for val in self.sd.values():
    cnt += val
    # interact with the interval sizes here by setting res

  return res # Replace with the value you want to return
