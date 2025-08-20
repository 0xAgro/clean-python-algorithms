# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcO8NJ4BnEmNwy-pAvuckvg>
# 🎥 Watch Breadth First Search here: <>
# ==============================

# g -> some graph
# In this case g is of form: [[1,4], [1, 2], ...] 
# (each index indicate what other indecies they are connected to)
def bfs(self, g):
  q = deque([0]) # Initialize double ended queue with root / desired start

  while q:
    node = q.popleft() # Pop node and other items if needed for logic

    print(node) # Replace with some logic

    for adj in g[node]: # Check all adjacent nodes
      q.append(adj)

  return -1 # Return desired value
