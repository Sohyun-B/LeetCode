class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root = ans = ListNode(0)
        carry = sum = 0

        while l1 or l2 or carry: # 셋 중 하나라도 있으면 덧셈 필요
            sum = 0
            if l1: # l1이 비어있을 때 오류가 나면 안 되므로
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            carry, value = divmod(sum + carry, 10) #값의 합과 올림을 더한 몫은 다시 올림(carry)가 되고 나머지가 현재 자릿수 값
            ans.next = ListNode(value)
            ans = ans.next
        return root.next