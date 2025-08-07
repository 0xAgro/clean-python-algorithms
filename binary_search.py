# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcch1TmsDfeJJ6cjyJTFwGW>
# ==============================

def bin_search(self, A, target):
  l, r = 0, len(A) - 1
  
  while l <= r:
    m = (l + r) // 2
    
    if A[m] < target:
      l = m + 1
    elif A[m] > target: 
      r = m - 1
    else:
      return m
      
    return -1
