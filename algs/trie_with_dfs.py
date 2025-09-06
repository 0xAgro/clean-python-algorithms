def findWords(self, B, W):
  t = Trie()
  res = []

  for w in W:
    t.insert(w)

  for m in range(len(B)):
    for n in range(len(B[0])):
      node = t.startsWith(B[m][n])
      if not node: continue
      stack = [(m, n, node, set([(m, n)]))]

      while stack:
        i, j, node, seen = stack.pop()

        if node.word != None:
          res.append(node.word)

        for u, v in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
          if 0 <= u < len(B) and 0 <= v < len(B[0]) and (u, v) not in seen and B[u][v] in node.children:
            stack.append((u, v, node.children[B[u][v]], seen | set([(u, v)])))

  return list(set(res))

class Node:
    def __init__(self):
        self.word = None
        self.children = {}
      
class Trie:

  def __init__(self):
    self.root = Node()

  def insert(self, word: str) -> None:
    node = self.root
    for c in word:
      if c not in node.children:
        node.children[c] = Node()
      node = node.children[c]
    node.word = word

  def search(self, word: str) -> bool:
    node = self.root
    for c in word:
      if c not in node.children:
        return False
      node = node.children[c]
    return node.word

  def startsWith(self, prefix: str) -> bool:
    node = self.root
    for c in prefix:
      if c not in node.children:
        return None
      node = node.children[c]
    return node
