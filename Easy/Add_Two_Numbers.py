# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def traverse(self,nodes):
        list1 = []
        while nodes is not None:
            list1.append(nodes.val)
            nodes = nodes.next
        return list1
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = int(''.join(str(i).strip() for i in self.traverse(l1)[::-1]))
        val2 = int(''.join(str(i).strip() for i in self.traverse(l2)[::-1]))
        sum_val = list(map(int, str(val1+val2)[::-1]))
        out = None
        head = None
        for item in sum_val:
            if out is not None:
                out.next =  ListNode(item,None)
                out = out.next
        
            else:
                out = ListNode(item,None)
                head = out

                 
        return head
        
