# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], value: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr is not None:

            if curr.val == value:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return head
