class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

def reverse_linked_list_with_stack(head):
    stack = []
    current = head

    while current is not None:
        stack.append(current)
        current = current.next_node

    new_head = stack.pop() if stack else None
    current = new_head

    while stack:
        current.next_node = stack.pop()
        current = current.next_node

    if current:
        current.next_node = None

    return new_head

# Creating a linked list
node1 = Node("data1")
node2 = Node("data2")
node3 = Node("data3")

node1.next_node = node2
node2.next_node = node3

# Reversing the linked list using a stack
new_head = reverse_linked_list_with_stack(node1)

# Printing the reversed linked list
current_node = new_head
while current_node:
    print(current_node.data)
    current_node = current_node.next_node
