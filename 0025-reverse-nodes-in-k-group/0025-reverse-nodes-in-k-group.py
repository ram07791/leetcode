# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self,temp):
        if temp is None or temp.next== None:
            return temp
        newHead = self.reverseList(temp.next)
        front = temp.next
        front.next = temp
        temp.next = None
        return newHead
    def getK(self,temp,k):
        k -=1
        while(temp !=None and k>0):
            temp =temp.next
            k-=1
        return temp
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        prevNode = None
        while temp != None:
            kNode = self.getK(temp,k)
            if(kNode == None):
                if prevNode:
                    prevNode.next = temp
                    break
            newNode = kNode.next
            kNode.next = None
            self.reverseList(temp)
            if(temp == head):
                head = kNode
            else:
                prevNode.next = kNode
            prevNode = temp
            temp = newNode
        return head



