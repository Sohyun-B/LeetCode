class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        root = ans = ListNode(0)
        while list1 or list2:
            if list2 and ((not list1) or (list1.val > list2.val)):
                ans.next = ListNode(list2.val)
                list2 = list2.next
                ans = ans.next
                pass
            elif (not list2) or (list2.val > list1.val):
                ans.next = ListNode(list1.val)
                list1 = list1.next
                ans = ans.next
                pass
            else:
                ans.next = ListNode(list1.val)
                ans = ans.next
                ans.next = ListNode(list2.val)
                ans = ans.next
                list1, list2 = list1.next, list2.next
        return root.next
###############################################################
# Helper function to convert list to ListNode
def list_to_listnode(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert ListNode to list
def listnode_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Test case
list1 = list_to_listnode([1])
list2 = list_to_listnode([])

# Merge the lists
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Convert result to list and print
result = listnode_to_list(merged_list)
print(result)