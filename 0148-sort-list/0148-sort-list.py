# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self,head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeLl(self,l1,l2):
        dummyNode = ListNode(-1)
        temp = dummyNode
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        else:
            temp.next = l2
        return dummyNode.next
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        middle = self.middleNode(head)
        right = middle.next
        middle.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeLl(left,right)
        