# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        # Sort the nodes based on their values
        nodes.sort(key=lambda node: node.val)

        # Reconstruct the sorted linked list
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        nodes[-1].next = None  # Important to terminate the list

        return nodes[0]

        