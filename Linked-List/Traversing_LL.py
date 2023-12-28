class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addNodeAtBeginning(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    else:
        new_node.next = head
        head = new_node
        return head  # Return the updated head

# Convert array into linked list
arr = [12, 34, 45, 67, 23]
head = Node(arr[0])
temp = head
for i in range(1, len(arr)):
    new_node = Node(arr[i])
    temp.next = new_node
    temp = new_node

arr1 = [12, 1, 2, 44, 5, 6]
head1 = None
for i in range(len(arr1)):
    head1 = addNodeAtBeginning(head1, arr1[i])  # Update head1

# Traversing the linked list
def traverseLL(head):
    temp1 = head
    while temp1 is not None:
        print(temp1.data)
        temp1 = temp1.next

traverseLL(head1)

