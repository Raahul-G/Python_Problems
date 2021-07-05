# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is not None:
            present = head
            forw = head.next
            while forw:
                if present.val == forw.val:
                    present.next = forw.next
                    forw = forw.next
                else:
                    forw = forw.next
                    present = present.next
        return head
