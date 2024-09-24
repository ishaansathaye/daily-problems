from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        '''BFS'''
        if root is None:
            return ""
        q = deque()
        q.append(root)
        res = []
        while len(q) != 0:
            curr = q.popleft()
            if curr is not None:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        '''BFS'''
        print(data)
        if data is None or len(data) == 0:
            return None
        data = data.split(",")
        q = deque()
        root = TreeNode(data[0])
        q.append(root)
        pt = 1
        while len(q) != 0:
            curr = q.popleft()
            left = data[pt]
            pt += 1
            right = data[pt]
            pt += 1
            if left != '#':
                curr.left = TreeNode(left)
                q.append(curr.left)
            if right != '#':
                curr.right = TreeNode(right)
                q.append(curr.right)
        return root

    def _serialize(self, root):
        '''DFS'''
        if root is None:
            return ""
        self.sb = []
        self.serializeHelper(root)
        print(self.sb)
        return ",".join(self.sb)

    def serializeHelper(self, root):
        if root is None:
            self.sb.append("#")
            return
        self.sb.append(str(root.val))
        self.serializeHelper(root.left)
        self.serializeHelper(root.right)

    def _deserialize(self, data):
        '''DFS'''
        if data is None or len(data) == 0:
            return None
        self.i = 0
        data = data.split(',')
        return self.deserializeHelper(data)

    def deserializeHelper(self, data):
        # base
        if data[self.i] == '#':
            self.i += 1
            return None
        # logic
        # root
        root = TreeNode(int(data[self.i]))
        self.i += 1
        # left
        root.left = self.deserializeHelper(data)
        # right
        root.right = self.deserializeHelper(data)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
