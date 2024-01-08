# 

# Better Solution
class Solution:
    def deleteMiddle(self, head):
        temp = head
        slow_node = temp
        fast_node = temp
        prev = None
        
        # Single node in LL
        if temp.next == None :
            return None
        
        # two nodes in LL then delete last and return the first
        if temp.next.next == None:
            last = temp.next
            temp.next = None
            del(last)
            return temp 
        # traversing over the LL to get the middle node 
        while fast_node!= None and fast_node.next != None:
            prev = slow_node
            slow_node = slow_node.next 
            fast_node = fast_node.next.next

        # deleting the middle node 
        prev.next = slow_node.next
        del(slow_node)
        return head  
    
def deleteMiddle(self, head):
        if not head.next:
            return None
        slow, fast = head, head.next.next

        # traversing the LL to get the mdile node 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #removing the midile node 
        slow.next = slow.next.next
        return head
