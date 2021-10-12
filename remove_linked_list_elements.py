"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []

Input: head = [5, 6, 7, 5], val = 5
Output: [6, 7]

UMPIRE!

Understand:
- What if the LinkedList has a cycle?
- Can the LinkedList empty?
- What can the value of the nodes be?
- Given two lists, will the be the same size?

We're given a LinkedList, we want to remove all nodes with val = val we're given

Match:
Linked Lists
Maybe use a dummyNode approach?

Plan:
Instantiate a dummyNode
For each node in our LinkedList...
    If node.val is not equal to val:
        put it at the end of our list!
    
return dummyNode.next (our true head node)

Implementation:

"""
from utilities import ListNode, arrayToLinkedList, linkedListToArray, linkedListsAreSame


def removeLinkedListElements(listnode: ListNode, val: int):
    dummyNode = ListNode(0, None)
    curTail = dummyNode

    curNode = listnode
    while curNode:
        if curNode.val != val:
            # Put it on the end of our list
            curTail.next = curNode
            curTail = curNode
        curNode = curNode.next

    # Explicitly set curTail.next to None
    curTail.next = None
    return dummyNode.next


# Warning! This code is broken! It's harder to get all the conditionals correct
# when you're not using a dummy node.
def removeLinkedListElementsWithoutDummyNode(listnode: ListNode, val: int):
    headNode = None
    curTail = None
    curNode = listnode
    while curNode:
        if curNode.val != val:
            # Put it on the end of our list
            if not headNode:
                headNode = curNode
                curTail = headNode
            else:
                curTail.next = curNode
                curTail = curNode
        curNode = curNode.next

    # Explicitly set curTail.next to None
    curTail.next = None
    return headNode


def runTests():
    test_cases = [
        {
            "inputLinkedList": arrayToLinkedList([1, 2, 6, 3, 4, 5, 6]),
            "inputVal": 6,
            "expectedOutput": arrayToLinkedList([1, 2, 3, 4, 5]),
        },
        {
            "inputLinkedList": arrayToLinkedList([]),
            "inputVal": 1,
            "expectedOutput": arrayToLinkedList([]),
        },
        {
            "inputLinkedList": arrayToLinkedList([7, 7, 7, 7]),
            "inputVal": 7,
            "expectedOutput": arrayToLinkedList([]),
        },
        {
            "inputLinkedList": arrayToLinkedList([5, 6, 7, 5]),
            "inputVal": 5,
            "expectedOutput": arrayToLinkedList([6, 7]),
        },
    ]
    for case in test_cases:
        actual = removeLinkedListElements2(case["inputLinkedList"], case["inputVal"])
        expected = case["expectedOutput"]

        if linkedListsAreSame(actual, expected):
            print("Success")
        else:
            print(
                f"Failure! Expected {linkedListToArray(expected)}, but got {linkedListToArray(actual)}"
            )


# Our basic ListNode class definition
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper functions!
# Quick recursive function to turn an array into a LinkedList
def arrayToLinkedList(nums):
    returnNode = None

    if nums:
        returnNode = ListNode(val=nums[0], next=arrayToLinkedList(nums[1:]))

    return returnNode


# Quick function to check whether two Linked Lists are the same
def linkedListsAreSame(l1: ListNode, l2: ListNode):
    # Check each node for same value
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    # If we only have one node, return false
    if l1 or l2:
        return False

    return True


if __name__ == "__main__":
    runTests()
