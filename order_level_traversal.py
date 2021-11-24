from typing import List
from utilities import TreeNode, listToBinaryTree

"""

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
            3
           / \
          9   20
              / \
             15  7

Returns:

[[3], [9, 20], [15, 7]]

Example:
            3
           / \
          9   20
         /    / \
        10   15  7


Returns:

[[3], [9, 20], [10, 15, 7]]


Example:
            3
             \
              4
                \
                 5
                  \
                   6
                    \
                     7
        

Returns:

[[3], [4], [5], [6], [7]]



"""

"""
Understand:
Given a binary tree, we want to return a list of lists, where each list is all node values for that binary tree level

Plan:
- Do an iterative breadth-first search
- Instantiate a list of lists to return
- For each level, grab all the node values, add them to appropriate list
- Add all children of current level to a list to look at next
"""

# Example of a breadth-first search, level-by-level
def orderLevelTraversal(root: TreeNode) -> List[List[int]]:
    cur_level_nodes = [root]
    order_level_values = []

    while cur_level_nodes:  # As long as we have nodes to look at
        next_level_nodes = []
        order_level_values.append([])
        for node in cur_level_nodes:
            order_level_values[-1].append(node.val)
            if node.left:
                next_level_nodes.append(node.left)
            if node.right:
                next_level_nodes.append(node.right)
        cur_level_nodes = next_level_nodes

    return order_level_values


def runTests() -> None:
    test_cases = [
        #     3
        #    / \
        #   9   20
        #       / \
        #      15  7
        {
            "input": listToBinaryTree([3, 9, 20, None, None, 15, 7]),
            "expectedOutput": [[3], [9, 20], [15, 7]],
        },
        #     3
        #    / \
        #   9   20
        #  /    / \
        # 10   15  7
        {
            "input": listToBinaryTree([3, 9, 20, 10, None, 15, 7]),
            "expectedOutput": [[3], [9, 20], [10, 15, 7]],
        },
        # 3
        #  \
        #   4
        #     \
        #      5
        #       \
        #        6
        #         \
        #          7
        {
            "input": listToBinaryTree([3, None, 4, None, 5, None, 6, None, 7]),
            "expectedOutput": [[3], [4], [5], [6], [7]],
        },
    ]
    for case in test_cases:
        actual = orderLevelTraversal(case["input"])
        expected = case["expectedOutput"]

        if actual == expected:
            print("Test success!")
        else:
            print(
                f"""Test failed - {case["input"]} returned {actual}, but expected {expected}"""
            )


if __name__ == "__main__":
    runTests()
