# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize pointers and temporary variables
        temp = list1  # Pointer to traverse list1
        temp2 = list1  # Another pointer to traverse list1
        pt1 = None  # Pointer to mark the node before segment a
        pt2 = None  # Pointer to mark the node after segment b
        
        # Traverse list1 to find the node before segment a
        while temp:
            a -= 1
            if a == 0:
                pt1 = temp
                break
            temp = temp.next
        
        # Traverse list1 to find the node after segment b
        while temp2:
            if b == 0:
                pt2 = temp2
                break
            temp2 = temp2.next
            b -= 1
            
        # Merge list2 into list1
        while list2:
            # Connect the end of segment a to the start of list2
            pt1.next = list2
            pt1 = pt1.next
            list2 = list2.next
            
            # If list2 reaches its end, connect the end of list2 to the node after segment b
            if list2 is None:
                pt1.next = pt2.next
                pt1 = pt1.next
                
        # Return the modified list1
        return list1
