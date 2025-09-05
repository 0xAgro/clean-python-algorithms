# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVeWoPtKptbuBXNDccVAGOdU>
# 🎥 Watch Note # Monotonic Qeue here: <>
# ==============================

# Seg Tree is nlogn, this is n
def max_window(self, A):
    q = deque()  # Monotonic Queue
    res = []

    while A:
        a = A.pop()

        while q and a >= q[-1]:
            q.pop()
        
        res.append(-1 if not q else q[0])
        q.append(a)

    return res
