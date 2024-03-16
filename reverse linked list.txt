a# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy=ListNode(0,head)
        leftprev,cur=dummy,head
        for i in range(left-1):
            leftprev,cur=cur,cur.next
        prev=None
        for i in range(right-left+1):
            tmpnext=cur.next
            cur.next=prev
            prev,cur=cur,tmpnext
        leftprev.next.next=cur
        leftprev.next=prev
        return dummy.next
