

class ListNode:
     def __init__(self, data):
          self.data = data
          self.next = None
def find_mid(self,head):
        temp = head
        temp1 = head.next.next
        right = head 
        while temp1 != None and temp1.next != None:
            right = right.next 
            temp1 = temp1.next.next
        return right

def merge_LL(self, head1, head2):
        t1 = head1
        t2 = head2
        dummy = ListNode(0)
        curr = dummy 
        while t1 and t2 :
            
            if t1.val > t2.val :
                curr.next = t2
                curr = t2 
                t2 = t2.next 
            else:
                curr.next = t1
                curr = t1 
                t1 = t1.next
        curr.next = t1 or t2
        return dummy.next

def sortList(self, head):
        if  not head :
            return None
        if head.next == None:
            return head
        left = head
        mid = self.find_mid(head)
        right = mid.next 
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge_LL(left, right)