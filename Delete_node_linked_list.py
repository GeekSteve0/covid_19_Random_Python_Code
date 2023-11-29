class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None



def delete_node(head, node_to_delete ):


    previous_node= None
    current_node = head
    while current_node:
        if current_node.data == node_to_delete.data:
          previous_node.next_node = current_node.next_node
          return(head)
        previous_node = current_node
        print("-------------------------")
        print(previous_node.data)

        current_node = current_node.next_node
        print(current_node.data)

    print("*******")

node1 = Node("data1")
node2 = Node("data2")
node3 = Node("data3")
node4 = Node("data4")
node5 = Node("data5")
node6 = Node("data6")
node7 = Node("data7")


node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5
node5.next_node = node6
node6.next_node = node7


new_head = delete_node(node1, node4)

# Printing the reversed linked list
current_node = new_head
print("hhhhhhhhhhhhhh")
while current_node:
    print(current_node.data)
    current_node = current_node.next_node
