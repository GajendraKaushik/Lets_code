
# Node claas or data type 
class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

# initializing the node 
node1 = Node(4)
node2 = Node(5)
node3 = Node(6)
node4 = Node(7)
node5 = Node(8)

# connecting the node with each other 
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None
temp = head

#traversing the node 
 
while (temp != None):
    print(temp.data,end=" ")
    temp = temp.next
