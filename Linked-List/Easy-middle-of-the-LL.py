class Solution:
    def middleNode(self, head):
        temp = head 
        temp1 = head

        # here we are using two pointer approach
        # temp1 will move one step and temp will move two step
        # when temp will reach to null temp1 will be on the mid.
        
        while(temp != None and temp.next != None):
            temp1 = temp1.next
            temp = temp.next.next
        return temp1