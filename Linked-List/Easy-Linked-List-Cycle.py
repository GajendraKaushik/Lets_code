# Problem : https://leetcode.com/problems/linked-list-cycle/description/

# To solve this problem we have used two pointer approach 

class Solution:
    def hasCycle(self, head) -> bool:
        node1 = node2 = None
        
        #checking for edge cases 
        if head == None or head.next == None:
            return False
        else:
            # initializing the temp nodes 
            node1= node2 = head 

        # traversing using two pointer      
        while( node2 != None and node2.next != None ):
            node2 = node2.next.next # moving two steps (fast )
            node1 = node1.next    # moving one step (slow)
            
            # if both nodes are pointing to the same node then there is a loop 
            if (node1 == node2): 
                return True
        return False  