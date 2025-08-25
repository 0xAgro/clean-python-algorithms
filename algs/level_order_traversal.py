# ==============================
# 📹 0xAgro Code Tutorial Playlist
# ==============================
# This code is part of a tutorial series.
# For detailed explanations and demonstrations, check out the playlist:
# 
# 🎥 Watch the full playlist here: <https://www.youtube.com/playlist?list=PLpCYhic-IxVcO8NJ4BnEmNwy-pAvuckvg>
# 🎥 Watch Level Order Traversal here: <>
# ==============================

def lot(self, root):
  if not root:
    return -1
  q = deque([root])

  while q:
    
    for idx in range(len(q)):
      node = q.popleft()

      if not node:
        continue

      print(node)

      if node.left:
        q.append(node.left)

      if node.right:
        q.append(node.right)
      
  return -1 
