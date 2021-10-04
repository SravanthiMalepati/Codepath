class Node:
 
    # Constructor to initialize
    # the node object
    def __init__(self, data):
         
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
         
        self.head = None
    
    def ispalindromelist(head):
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        if vals == vals[::-1]:
            return True
        else:
            return False