# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front 
        return prev
        """
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead