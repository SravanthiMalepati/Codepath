from typing import List
from collections import deque

"""
TreeNode class definition.
Default val = 0, left = None, right = None
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Helper function to take a list representation of a binary tree
and return the corresponding binary tree.

Ex:

[2,1,3]

            2
           / \
          1   3

[2,2,4,None,5,7,9]

            2
           / \
          2   4
          \   / \
           5  7  9

[3, 9, 20, None, None, 15, 22]
            3
           / \
          9   20
              / \
             15  22
"""


def listToBinaryTree(vals: List[int]):
    if not vals:
        return None

    valsQueue = deque(vals)
    nodesForAppend = deque([TreeNode(val=valsQueue.popleft())])
    rootNode = nodesForAppend[0]

    while valsQueue:
        curNode = nodesForAppend.popleft()

        if valsQueue:
            leftVal = valsQueue.popleft()
            if leftVal:
                leftNode = TreeNode(val=leftVal)
                nodesForAppend.append(leftNode)
                curNode.left = leftNode

        if valsQueue:
            rightVal = valsQueue.popleft()
            if rightVal:
                rightNode = TreeNode(val=rightVal)
                nodesForAppend.append(rightNode)
                curNode.right = rightNode

    return rootNode


### Three recursive traversals
def preorderTraversal(root: TreeNode):
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)


def postorderTraversal(root: TreeNode):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val)


def inorderTraversal(root: TreeNode):
    if root:
        inorderTraversal(root.left)
        print(root.val)
        inorderTraversal(root.right)


if __name__ == "__main__":
    """
    [6, 3, 10, None, 5, 9, 11]

            6
           / \
          3   10
          \   / \
           5  9  11
    """
    myTree = listToBinaryTree([6, 3, 10, None, 5, 9, 11])
    print(myTree)
    inorderTraversal(myTree)
