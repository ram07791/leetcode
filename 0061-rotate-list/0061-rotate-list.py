# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nNode(self,temp,k):
        cnt = 1
        while temp!= None:
            if cnt ==k:
                return temp
            cnt+=1
            temp = temp.next
        return temp
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head == None or k==0:
            return head
        tail = head
        length = 1

        while tail.next !=None:
            tail = tail.next
            length+=1
        if k %length ==0:
            return head
        k = k % length
        tail.next = head
        lastNode = self.nNode(head,length - k)
        head = lastNode.next
        lastNode.next = None
        return head

            
    
        