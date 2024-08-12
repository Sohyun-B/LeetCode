class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        
        #러너를 이용한 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
   
                    
