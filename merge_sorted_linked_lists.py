# Our basic ListNode class definition
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoSortedLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Let's use a dummyNode because I don't know which our head node will be
    dummyNode = ListNode(0, None)

    # We want to keep track to the end of our list
    curTailNode = dummyNode

    while l1 or l2:
        # If l1 <= l2, we want to append l1 to our return list:
        if (not l2) or (l1 and l2 and l1.val <= l2.val):
            curTailNode.next = l1
            curTailNode = curTailNode.next
            l1 = l1.next
        # If l1 > l2, we want to append l2 to our return list:
        elif (not l1) or (l1 and l2 and l1.val > l2.val):
            curTailNode.next = l2
            curTailNode = curTailNode.next
            l2 = l2.next

    return dummyNode.next


def printLinkedList(listnode: ListNode):
    while listnode:
        print(listnode.val)
        listnode = listnode.next


def runTests():
    test_cases = [
        {
            "inputL1": arrayToLinkedList([1, 3]),
            "inputL2": arrayToLinkedList([2, 4]),
            "expectedOutput": arrayToLinkedList([1, 2, 3, 4]),
        },
        {
            "inputL1": arrayToLinkedList([1, 2]),
            "inputL2": arrayToLinkedList([2, 3]),
            "expectedOutput": arrayToLinkedList([1, 2, 2, 3]),
        },
        # {
        #     "inputL1": arrayToLinkedList([1, 2]),
        #     "inputL2": arrayToLinkedList([1, 3]),
        #     "expectedOutput": arrayToLinkedList([1, 1, 2, 3]),
        # },
        # {
        #     "inputL1": arrayToLinkedList([]),
        #     "inputL2": arrayToLinkedList([1]),
        #     "expectedOutput": arrayToLinkedList([1]),
        # },
        # {
        #     "inputL1": arrayToLinkedList([1]),
        #     "inputL2": arrayToLinkedList([]),
        #     "expectedOutput": arrayToLinkedList([1]),
        # },
        # {
        #     "inputL1": arrayToLinkedList([]),
        #     "inputL2": arrayToLinkedList([]),
        #     "expectedOutput": arrayToLinkedList([]),
        # },
    ]
    for case in test_cases:
        actual = mergeTwoSortedLists(case["inputL1"], case["inputL2"])
        expected = case["expectedOutput"]

        if linkedListsAreSame(actual, expected):
            print("Test success!")
        else:
            print(f"Warning - test failed!")


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
