from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Advance fast by n + 1 steps to create an n-node gap
        for _ in range(n + 1):
            fast = fast.next

        # Shift both pointers until fast hits the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Unlink the nth node from the end
        slow.next = slow.next.next
        return dummy.next
