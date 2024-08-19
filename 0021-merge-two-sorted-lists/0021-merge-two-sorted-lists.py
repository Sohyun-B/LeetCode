class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = ans = ListNode(0)
        while list1 or list2:
            if list1 and list2:
                if list1.val > list2.val:
                    ans.next = ListNode(list2.val)
                    list2 = list2.next
                    ans = ans.next
                elif list1.val < list2.val:
                    ans.next = ListNode(list1.val)
                    list1 = list1.next
                    ans = ans.next
                else: # list1.val == list2.val
                    ans.next = ListNode(list1.val)
                    ans = ans.next
                    ans.next = ListNode(list2.val)
                    ans = ans.next
                    list1 = list1.next
                    list2 = list2.next
            elif list1:
                ans.next = ListNode(list1.val)
                list1 = list1.next
                ans = ans.next
            elif list2:
                ans.next = ListNode(list2.val)
                list2 = list2.next
                ans = ans.next
        return root.next
    




            
