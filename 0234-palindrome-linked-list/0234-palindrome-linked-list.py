# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []
        temp = head
        while temp:
            node_list.append(temp.val)
            temp = temp.next
        return node_list == node_list[::-1]
        