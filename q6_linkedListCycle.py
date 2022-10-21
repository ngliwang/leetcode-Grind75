# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        # floyd's tortoise and hare algorithm
            # having a FAST and SLOW pointer
            # eventually they will catch up with each other

            # 10+(1-2)
            # 10 represent the gap between fast and slow pointer
            # +1 means SLOW pointer moves 1 step at a time
            # -2 means FAST pointer moves 2 steps at a time

        try:
            slow = head
            fast = head.next

            while slow != fast:
                fast = fast.next.next
                slow = slow.next

            return True

        except:
            return False