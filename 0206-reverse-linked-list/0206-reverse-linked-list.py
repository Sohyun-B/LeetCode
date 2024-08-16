class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):

        node, prev = head, None
        while node:
            next_val, node.next = node.next, prev
            prev, node = node, next_val
        return prev
solution = Solution()
ans = solution.reverseList(ListNode([1,2,2,1]))
print(ans)
                
                    
