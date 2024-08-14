class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):

        def reverse(node, prev = None):
            if not node:
                return prev
            next_val, node.next = node.next, prev
            return reverse(next_val, node)
        
        return reverse(head)
        
        
        