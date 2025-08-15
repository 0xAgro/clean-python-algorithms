# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcch1TmsDfeJJ6cjyJTFwGW>
# ==============================

def bin_search(self, A, target):
  l, r = 0, len(A) - 1 # Initial Bounds
  
  while l <= r: # While our bounds dont meet
    m = (l + r) // 2 # Calculate midpoint between our bounds
    
    if A[m] < target: 
      l = m + 1 # We can cut off the left side
    elif A[m] > target: 
      r = m - 1 # We can cut off the right side
    else:
      return m # Found
      
  return -1 # Not found
