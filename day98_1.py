# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Store the values of the linked list in an array
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        # Initialize pointers for the left and right ends of the array
        left = 0
        right = len(arr)-1
        # Initialize a counter for alternating between left and right values
        cnt = 1
        # Pointer to iterate through the linked list
        curr = head
        
        # Traverse the linked list and update node values from the array alternately
        while head:
            if cnt%2==1:
                head.val = arr[left]
                left+=1
            else:
                head.val = arr[right]
                right-=1
            head=head.next
            cnt+=1
        
        return curr
