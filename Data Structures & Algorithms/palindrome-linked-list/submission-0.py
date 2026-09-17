# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        dummy = head
        while dummy:
            stack.append(dummy.val)
            dummy = dummy.next
        
        while stack:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True
        