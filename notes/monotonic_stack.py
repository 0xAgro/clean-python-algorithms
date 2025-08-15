# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# ==============================


def NGE(self, A):
  A = A[:] # Input is modified so we create a copy
  stack = [] # Monotonic Stack
  res = []

  while A:
    a = A.pop() # Pop the last element 
            
    while stack and a >= stack[-1]:
      stack.pop() # Pop monotonic stack until we can insert to keep it monotonic

    res.append(-1 if not stack else stack[-1]) # Our result is the top of the stack or -1 if empty
    stack.append(a) # Add last seen to the Monotonic Stack

  return res[::-1] # Reversed since we append in reverse
