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
def max_window(self, A, k):
    q = deque()  # Monotonic Queue
    res = []

    for idx, a in enumerate(A):

        while q and A[q[-1]] <= a:
            q.pop()

        q.append(idx)

        if q[0] <= idx - k:
            q.popleft()

        if idx >= k - 1:
            res.append(A[q[0]])

    return res
