# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # For easier visualization of the list
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return "->".join(result)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Implement your reverse logic here
        curr = head
        prev = None

        while curr:
            next_temp = curr.next

            curr.next = prev

            prev = curr

            curr = next_temp

        # by then "curr" becomes null, it also acts as the stopping condition
        return prev
            



def create_linked_list(lst):
    """Creates a linked list from a list of values and returns the head."""
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    """Prints the linked list in a readable format."""
    if not head:
        print("Empty List")
    else:
        print(head)

def main():
    # Example Test Case
    input_values = [1, 2, 3, 4, 5]
    print("Original Linked List:")
    head = create_linked_list(input_values)
    print_linked_list(head)

    # Create a Solution instance and reverse the list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("\nReversed Linked List:")
    print_linked_list(reversed_head)

if __name__ == "__main__":
    main()
