from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev to None, which will be the new tail of the reversed list
        prev = None
        
        # Initialize temp variable to hold the next node temporarily
        temp = None
        
        # Initialize curr to the head of the input list
        curr = head
        
        # Traverse the input list
        while curr:
            # Store the next node of the current node in the temp variable
            temp = curr.next
            
            # Reverse the link of the current node to point to the previous node
            curr.next = prev
            
            # Move prev to the current node
            prev = curr
            
            # Move curr to the next node (temporarily stored)
            curr = temp
        
        # When curr becomes None, prev will be the new head of the reversed list
        return prev
