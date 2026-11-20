from typing import Optional

class Node:
    def __init__(self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # 1. Insert cloned node right after each original node
        curr = head
        while curr:
            nxt = curr.next
            copy = Node(curr.val, next=nxt)
            curr.next = copy
            curr = nxt

        # 2. Assign random pointers to cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Separate original list and cloned list
        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            copy = curr.next
            nxt = copy.next

            copy_curr.next = copy
            copy_curr = copy

            curr.next = nxt
            curr = nxt

        return dummy.next
