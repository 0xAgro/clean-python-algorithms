# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #9 Sliding Window here: <https://youtu.be/XMQwiY-Mieo>
# ==============================

# This returns the max sum of a sliding window, change logic line for your use
def sliding_window(self, A):
  cnt, res = sum(A[:k]), 0 # Get initial sum seen in video

  for idx in range(k, len(A) + 1):
    res = max(cnt, res) # Logic line, replace and put cnt reading logic here
            
    if idx != len(A): # This logic was put in just so that all logic above can fit in the loop
      cnt += A[idx]
      cnt -= A[idx - k]

  return res
