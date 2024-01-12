
#https://leetcode.com/problems/merge-k-sorted-lists/submissions/1143040617/

# approach heapq 

import heapq

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
def merge_K_LL(lists):
    minNode =[]
    for i in range(len(lists)):
        heapq.heappush(minNode,lists[i].val, lists[i]) # some error is here 
    dummy = Node(-1)
    curr = dummy

    while minNode:
        top = heapq.heappop(minNode)
        curr.next = top[1]
        if top.next :
            heapq.heappush((top[1].next.data, top[0].next))
            curr = curr.next
    return dummy.next 

# approach divide and conquore and merge 

def mergeKLists(self, lists):
 
        def merge(l1, l2):
            dummy = Node(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            curr.next = l1 or l2
            return dummy.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return merge(left, right)




