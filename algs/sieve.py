# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcO8NJ4BnEmNwy-pAvuckvg>
# 🎥 Watch Sieve here: <https://youtu.be/kQAQULBRsDI>
# ==============================

def sieve(self, n):
  p_fac = [i for i in range(n + 1)] # Generate prime list
  p_fac[0], p_fac[1] = -1, -1 # 0 and 1 are not prime

  for i in range(2, int(sqrt(n)) + 1):
    for j in range(i*2, n + 1, i): # Start at 2*i as we dont want to assume i is not prime
      p_fac[j] = -1 # Not prime

  return [p for p in p_fac if p != -1] # Return all positive numbers (primes)
