def serialize(self, root):
        if not root:
            return ""

        q = deque([root])
        res = ""

        while q:
            node = q.popleft()

            if node:
                res += str(node.val) + "."
            else:
                res += "X."
                continue

            q.append(node.left)
            q.append(node.right)

        return res[:-1]
        

    def deserialize(self, data):
        if not data:
            return []

        val = data.split(".")[::-1]
        root = TreeNode(int(val.pop()))
        q = deque([root])

        while q:
            node = q.popleft()

            if val[-1] != 'X':
                node.left = TreeNode(int(val.pop()))
                q.append(node.left)
            else:
                val.pop()
            
            if val[-1] != 'X':
                node.right = TreeNode(int(val.pop()))
                q.append(node.right)
            else:
                val.pop()

        return root
