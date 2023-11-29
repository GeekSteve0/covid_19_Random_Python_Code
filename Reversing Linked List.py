class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

def reverse_linked_list_with_stack(head):
    stack = []
    current = head



    while current is not None:
        stack.append(current)
        print(current.data)

        current = current.next_node
    print ("+++++++++++++")
    print("before_first_pop")
    print(len(stack))
    new_head = stack.pop() if stack else None
    print(len(stack))
    current = new_head
    print(current.data)
    print(current.next_node)
    print ("^^^^^^^^^^^^^^^^^^^^^^^^")

    while stack:
        next=stack.pop()
        print(len(stack))
        print(next.data)

        current.next_node = next

        current = next
    print("===========================")
    if current:
        print(current.next_node.data)
        current.next_node = None
        print(current.next_node)
    print("&&&&&&&&&&")
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
