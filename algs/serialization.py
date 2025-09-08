


def generate_all_serials(self, root):
        val = []
        res = []

        def dfs(node):
            if not node:
                return 'X'
            
            l = dfs(node.left)
            r = dfs(node.right)
            s = str(node.val) + '.' + l + '.' + r

            res.append(s)
            return s
        
        dfs(root)
        return res

def serialize(self, root):
        val = []

        def dfs(node):
            if not node:
                val.append('X')
                return
            
            val.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return '.'.join(val)
        

    def deserialize(self, data):
        val = data.split('.')[::-1]

        def dfs():
            if val[-1] == 'X':
                val.pop()
                return None
            node = TreeNode(int(val.pop()))
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()


# BFS Less overhead, but isnt good for linear node serialization
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
