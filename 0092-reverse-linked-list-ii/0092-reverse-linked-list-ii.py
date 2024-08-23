class Solution(object):
    def reverseBetween(self, head, left, right):
        # 예외처리
        if not head or left==right:
            return head
        
        root = start = ListNode(0)
        root.next = head

        #변경이 필요 없는 앞부분
        for _ in range(left -1):
            start = start.next 
        end = start.next

        for _ in range(right - left): #구간의 길이만큼
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
            # start.next => end.next: start가 가리키는거 end가 가리키는 걸로 교환
            # end.next => end.next.next: end가 가리키는거 end의 다음다음으로 교환
            # start.next.next => start.next: start의 다음다음을 start가 가리키는걸로 교환
        return root.next
