class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        # Dictionary to store the frequency of elements in the current subarray
        freq = {}
        # Pointer to the start of the current subarray
        start = 0
        # Pointer to the start of the subarray with exactly K distinct elements
        start_k = 0
        # Variable to store the result
        res = 0
        
        # Iterate through the array A
        for i, x in enumerate(A):
            # Update the frequency count of the current element x
            freq[x] = freq.get(x, 0) + 1
            
            # If the number of distinct elements in the current subarray is K + 1,
            # adjust the subarray to have exactly K distinct elements
            if len(freq) == K + 1:
                # Remove the element at the start_k position from the frequency dictionary
                del freq[A[start_k]]
                # Move the start_k pointer to the next position
                start_k += 1
                # Move the start pointer to the new start_k position
                start = start_k
            
            # If the number of distinct elements in the current subarray is K,
            # calculate the number of subarrays with K distinct elements
            if len(freq) == K:
                # Update start_k and res
                while freq[A[start_k]] > 1:
                    # Decrement the frequency count of the element at start_k
                    freq[A[start_k]] -= 1
                    # Move the start_k pointer to the next position
                    start_k += 1
                # Calculate the length of the subarray with exactly K distinct elements
                # and add it to the result
                res += start_k - start + 1
        
        return res
