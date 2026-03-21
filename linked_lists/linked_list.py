class Node:
    def __init__(self, number):
        self.number = number
        self.prev = None
        self.next = None

class LinkedList:
    """
    Problem: Static or contiguous collections like arrays (or standard Python lists, which act as dynamic arrays 
    under the hood) have an O(n) time complexity for insertions and deletions at the beginning or in the middle. 
    This is because it requires shifting all subsequent elements in memory to create or fill the space.
    
    How it works: A Doubly Linked List solves this by using dynamically allocated nodes spread across non-contiguous 
    memory locations. Each node carries its data and two pointers: 'prev' for the previous node and 'next' for the 
    subsequent node. This approach makes add and remove operations at the extremities (head or tail) O(1) constant 
    time, since it only requires updating pointer references. Edge cases like empty lists or removing the final 
    element are handled smoothly.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def append_head(self, number):
        new_node = Node(number)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append_tail(self, number):
        new_node = Node(number)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            print("Empty List")
            return

        print(self.head.number)
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def remove_tail(self):
        if not self.tail:
            print("Empty List")
            return

        print(self.tail.number)
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None


# Test cases
import io
import sys

ll = LinkedList()

# empty list initialization check
assert ll.head is None
assert ll.tail is None

# appending to head on an empty list
ll.append_head(10)
assert ll.head.number == 10
assert ll.tail.number == 10

# appending to tail and head with multiple elements
ll.append_tail(20)
ll.append_head(5)

# current list state: 5 <-> 10 <-> 20
assert ll.head.number == 5
assert ll.head.next.number == 10
assert ll.tail.number == 20
assert ll.tail.prev.number == 10

# remove head preserves next sequence (removes 5)
captured_output = io.StringIO()
sys.stdout = captured_output
ll.remove_head()
sys.stdout = sys.__stdout__
assert captured_output.getvalue().strip() == "5"
assert ll.head.number == 10
    
# remove tail preserves prev sequence (removes 20)
captured_output = io.StringIO()
sys.stdout = captured_output
ll.remove_tail()
sys.stdout = sys.__stdout__
assert captured_output.getvalue().strip() == "20"
assert ll.tail.number == 10

# edge case: remove the last remaining element (10)
captured_output = io.StringIO()
sys.stdout = captured_output
ll.remove_tail()
sys.stdout = sys.__stdout__
assert captured_output.getvalue().strip() == "10"
assert ll.head is None
assert ll.tail is None

# edge case: fails safely when removing from empty list
captured_output = io.StringIO()
sys.stdout = captured_output
ll.remove_head()
sys.stdout = sys.__stdout__
assert "Empty List" in captured_output.getvalue()
