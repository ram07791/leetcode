"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def new(self,head):
        temp = head
        while temp!=None:
            nexte = temp.next
            copyNode = Node(temp.val)
            copyNode.next = nexte
            temp.next = copyNode
            temp = nexte
    def connectRandom(self,head):
        temp = head
        while temp!=None:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None
            temp = temp.next.next
    def getCopy(self,head):
        dummyNode = Node(-1)
        temp = head
        res = dummyNode
        while(temp!=None):
            res.next = temp.next
            res = res.next
            temp.next = temp.next.next
            temp = temp.next
        return dummyNode.next
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.new(head)
        self.connectRandom(head)
        return self.getCopy(head)