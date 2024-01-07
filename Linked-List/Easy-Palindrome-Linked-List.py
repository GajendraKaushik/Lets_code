# https://leetcode.com/problems/palindrome-linked-list/ 

def isPalindrom_LL(head):
    s =""
    temp = head
    
    # traverse all the data and store it in variable 
    while temp != None:
        s += str(temp.data)
        temp = temp.next

    # reverse the data 
    reverse = s[::-1]
   
    # compaire the reversed and origin data 
    if s == reverse:
        return True
    else:
        return False

## Optimal Approach 

# reverse LL   
def reverseLL(head):
    p = q = None
    temp = head 
    while temp != None:
        p = q 
        q = temp
        temp = temp.next
        q.next = p
    return q 


def Optime_isPalindrom(head):
    if head == None or head.next == None :
        return True
    
    slow = fast = head
    
    # get the middile of LL
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    # reverse LL from middle 
    slow.next = reverseLL(slow.next)
    slow = slow.next
    dummy_node = head
    
    # start compairing the LL from beggining and middle 
    while slow != None:
        if dummy_node.val != slow.val :
            return False
        slow = slow.next
        dummy_node = dummy_node.next
    return True
     


    


