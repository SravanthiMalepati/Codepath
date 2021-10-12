class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(node):
    length = 0
    while node != None:
        length += 1
        node = node.next

    return length
# def addone (head: ListNode):
#     addwithCarry(head)
#     return head
# def addwithCarry (head: ListNode):
#     if (head == None) :
#         return 1
#     carry = addwithCarry(head.next)
#     sum = head.val + carry
#     head.val = (sum) % 10
#     return (sum) // 10

class Tests:
    if __name__ == "__main__":
        n0 = ListNode(val=9)
        n1 = ListNode(val=9)
        n0.next = n1
        print(f"Test 1 - getLength returned: {getLength(n0)}, expected: 2")

        n1 = ListNode(val=1)
        n2 = ListNode(val=9)
        n3 = ListNode(val=9)
        n4 = ListNode(val=9)
        n1.next = n2
        n2.next = n3
        n3.next = n4
        print(f"Test 2 - getLength returned: {getLength(n1)}, expected: 4")