# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        newHead = self.reverse(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        first = head
        newHead = self.reverse(slow.next)
        second = newHead
        while(second is not None):
            if first.val is not second.val:
                self.reverse(newHead)
                return False
            first = first.next
            second = second.next
        self.reverse(newHead)
        return True

      
        