# implimentation of DLL 

class Node:
    def __init__(self, data):
        self.prev = None
        self.val = data
        self.next = None

def Array_to_DLL(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        while(temp.next != None):
            temp = temp.next
        new_node.prev = temp
        temp.next = new_node
    return head 

def Insert_at_the_starting_of_DLL(head, n):
    temp =head
    new_Node = Node(n)
    new_Node.next = head
    head.prev = new_Node
    head = new_Node
    return head

def Delete_From_End(head):
    temp = head
    val = 0
    
    while temp.next != None:
        temp = temp.next
    val = temp.data
    print(val)
    temp.prev.next = None 
    del(temp)
    return head

     



arr = [1,2,34,5]

DLL = Array_to_DLL(arr)

Dll_updated = Insert_at_the_starting_of_DLL(DLL, 60)

print("Normal")
while DLL :
    print(DLL.val)
    DLL = DLL.next
    
print("Done")


print("updated")
while Dll_updated :
    print(Dll_updated.val)
    Dll_updated = Dll_updated.next
    
print("Deleted")
while Dll_updated :
    print(Dll_updated.val)
    Dll_updated = Dll_updated.next 


