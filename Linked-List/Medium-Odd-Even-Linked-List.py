#https://leetcode.com/problems/odd-even-linked-list/description/


def Odd_EvenLL(head):
    backup = head
    odd_node = head
    even_node = head.next
    temp = head.next.next
    check = 3

    while temp != None:
        if check % 2 ==0:
            even_node.next = temp 
        else:
            odd_node.next = temp 
    odd_node = even_node
    return head 


# Optimal Solution 

def Odd_Even_Optimal_LL(head):
    if head == None:
        return head
    #node starting from odd index
    odd_node = head

    #node starting from even index
    even_node = head.next
    even_node_head = even_node
    
    # moving till even_node becomes None because even will reach to the end first 
    while even_node.next != None  and even_node.next.next != None :
        # moving two steps and attaching only odd nodes 
        odd_node.next = odd_node.next.next 

         # moving two steps and attaching only even nodes 
        even_node.next = even_node.next.next 

        #Changing the odd and even node values 
        odd_node = odd_node.next
        even_node = even_node.next
    # adding the odd and even node together 
    odd_node.next =  even_node_head
    return head 
