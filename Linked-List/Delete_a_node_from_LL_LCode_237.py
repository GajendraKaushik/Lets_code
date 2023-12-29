#problem : https://leetcode.com/problems/delete-node-in-a-linked-list/description/

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # if node is the last node 
        if node.next == None:
            return -1
        
        # creating a copy of the node  
        temp = node 
        # storing the next node
        p = temp.next
        # storing the data of nextnode 
        d = p.val
        #passing the refference of the next not the temp 
        temp.next = p.next
        # coping the data of next node to temp
        temp.val = d 
        #deleting the previous node 
        del(p)
        