# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note #7 Memoization here: <https://www.youtube.com/shorts/AKhz64wNcIc>
# ==============================

# Memoization
def fib(self, n, mem):
  if n in mem:
    return mem[n] # Return memo when available
  if n < 2:
    return n # Base case for 1 and 0
  mem[n] = self.fib(n - 1, mem) + self.fib(n - 2, mem)
  return mem[n]

# Simpler using @lru_cache()
@lru_cache()
def fib(self, n):
  return n if n == 1 or not n else self.fib(n - 1) + self.fib(n - 2)
