class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

node1 = Node("data1")
node2 = Node("data2")
node3 = Node("data3")

node1.next_node = node2
node2.next_node = node3

current_node = node1
while current_node:
    print(current_node.data)
    current_node = current_node.next_node
