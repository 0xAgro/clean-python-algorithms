# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# ==============================


def NGE(self, A):
  A = A[:]
  stack = []
  res = []

  while A:
    a = A.pop()
            
    while stack and a > stack[-1]:
      stack.pop()

    res.append(-1 if not stack else stack[-1])
    stack.append(a)

  return res[::-1]
