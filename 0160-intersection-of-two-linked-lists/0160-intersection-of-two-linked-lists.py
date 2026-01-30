# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        t1 = headA
        t2 = headB
        while(t1 is not t2):
            t1 = t1.next
            t2 = t2.next
            if t1 is t2:
                return t1
            if t1 is None:
                t1 = headB
            if t2 is None:
                t2 = headA
        return t1