# Definition for singly-linked list.
from traceback import print_list
from time import sleep


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
   
    
    # define Optional
    # print list, print out all values in the linked list
    def printList(self, head):
        while head != None:
            print(head.val)
            head = head.next


    def mergeTwoLists_Ans(self, list1, list2):
        cur = dummy = ListNode()
        
        # while they are not empty
        while list1 and list2:

            # drop away the result [] by...
            # straightaway attach to cursor    
            if list1.val < list2.val:
                print(list1)
                cur.next = list1

                # move on to the next node
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

    def mergeTwoLists(self, list1, list2):
        # create a dummy cursor, to be overwritten any time
        dummy = ListNode(0)

        # create a cursor to traverse the list
        cursor = dummy

        result = []

        # traverse in list1
        while list1 != None and list2 != None:
            # print("list1: ", list1.val, "next:", list1.next)
            # move on to the next node
            

            # HOW DO YOU APPEND THO?
            if list1.val <= list2.val:
                result.append(ListNode(list1.val))
                cursor = list1.next
                list1 = cursor
        
            elif list1.val > list2.val:
                cursor = list2.next
                list2 = cursor
                result.append(ListNode(list2.val))
        print(result)
        return result




solution = Solution()
# solution.mergeTwoLists([1,2,4], [1,3,4])

# create a list of ListNode
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print("list 1: ", list1)
print("list 2: ", list2)
solution.mergeTwoLists(list1, list2)