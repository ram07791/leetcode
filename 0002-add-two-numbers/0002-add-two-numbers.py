# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1 = l1
        t2 = l2
        dummyNode = ListNode(-1)
        current = dummyNode
        carry = 0
        while(t1 is not None or t2 is not None ):
            tsum = carry
            if t1:
                tsum = tsum + t1.val
            if t2:
                tsum = tsum + t2.val
            newNode = ListNode(tsum%10)
            carry = tsum//10
            current.next = newNode
            current = current.next
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry:
            newNodes = ListNode(carry)
            current.next = newNodes
        return dummyNode.next
            