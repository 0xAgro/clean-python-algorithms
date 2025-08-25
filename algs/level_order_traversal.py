# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcO8NJ4BnEmNwy-pAvuckvg>
# 🎥 Watch Level Order Traversal here: <>
# ==============================

# BFS but allows us to do computation per level
def lot(self, root):
  if not root:
    return -1 # To prevent trying to access a None value later
  q = deque([root]) # Initialize our double ended q

  while q: # Loop while q is full
    
    for idx in range(len(q)): # IMPORTANT: allows us to access each level
      node = q.popleft()

      if not node:
        continue

      print(node) # Computation logic

      if node.left:
        q.append(node.left)

      if node.right:
        q.append(node.right)

    # Level Logic goes here outside the for loop
      
  return -1 
