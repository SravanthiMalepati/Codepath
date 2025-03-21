class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.st = []
        while root:
            self.st.append(root)
            root = root.left

    def next(self):
        """
        :rtype: int
        """
        res = self.st.pop()
        curr = res.right
        while curr:
            self.st.append(curr)
            curr = curr.left
        return res.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0


# Construct the BST [7, 3, 15, None, None, 9, 20]
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

# Initialize BST Iterator
obj = BSTIterator(root)

# Debugging Execution
print(obj.next())      # 3
print(obj.next())      # 7
print(obj.hasNext())   # True
print(obj.next())      # 9
print(obj.hasNext())   # True
print(obj.next())      # 15
print(obj.hasNext())   # True
print(obj.next())      # 20
print(obj.hasNext())   # False
