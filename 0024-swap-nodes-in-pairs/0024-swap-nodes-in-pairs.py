class Solution(object):
    def swapPairs(self, head):
        root = prev = ListNode(0)
        prev.next = head
        while head and head.next:
            temp = head.next 
            head.next = temp.next # temp.next가 없을 경우 none을 반환한다
            temp.next = head

            prev.next = temp

            # 다음으로 이동
            head = head.next 
            prev = prev.next.next
        return root.next