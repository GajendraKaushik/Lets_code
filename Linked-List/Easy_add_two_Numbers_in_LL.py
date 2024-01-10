# https://youtu.be/XmRrGzR6udg?si=6UkMJYCRC-vBalo3  


class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        pass

Node1 = Node(3)
Node2 = Node(8)
Node3 = Node(7)
Node21 = Node(5)
Node22 = Node(2)
Node23 = Node(4)
Node24 = Node(1)

head1 = Node1
Node1.next = Node2
Node2.next = Node3
print(Node1,"Node1") 
temp = head1
while(temp):
    print(temp.data)
    temp = temp.next
head2 = Node21
Node21.next = Node22
Node22.next = Node23 
print(Node21.next.data,"Node2")

def add_2_Numbers_LL(node1, node2):
    t1 = node1
    t2= node2
    carry = 0 
    dummy = Node(-1)
    curr = dummy
    while t1 or t2:
        sum = 0
        if t1: 
            sum = sum + t1.data 
            t1 = t1.next
        if t2 :
            sum = sum + t2.data
            t2 = t2.next 
        sum += carry
        carry = sum // 10
        new_node = Node(sum % 10)
        curr.next = new_node
        curr = new_node
    if carry:
        new_node = Node(carry)
        curr.next = new_node

    return dummy.next     

ans1 = add_2_Numbers_LL(head1, head2)
ans = ans1

while(ans):
    print(ans.data)
    ans = ans.next