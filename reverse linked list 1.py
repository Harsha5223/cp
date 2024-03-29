# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        tmp=ListNode()
        dummy=tmp
        while stack:
            tmp.next=stack.pop()
            tmp=tmp.next
        tmp.next=None
        return dummy.next
