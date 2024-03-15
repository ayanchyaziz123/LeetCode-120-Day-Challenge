class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # Initialize variables to track the start index, counts of 'F' and 'T', and the maximum consecutive answers
        start = 0
        false_cnt = 0
        true_cnt = 0
        mx = 0
        
        # Iterate through the answerKey string
        for i in range(len(answerKey)):
            # Increment the count of 'F' if the current answer is 'F'
            if answerKey[i] == 'F':
                false_cnt += 1
            # Increment the count of 'T' if the current answer is 'T'
            if answerKey[i] == 'T':
                true_cnt += 1
            
            # Check if the counts of 'F' and 'T' exceed the given value of k
            while start < i and (false_cnt > k and true_cnt > k):
                # Decrement the count of 'T' if the answer at the start index is 'T'
                if answerKey[start] == 'T':
                    true_cnt -= 1
                # Decrement the count of 'F' if the answer at the start index is 'F'
                if answerKey[start] == 'F':
                    false_cnt -= 1
                # Move the start index forward
                start += 1
            
            # Update the maximum consecutive answers by taking the maximum of the current count of 'T' and 'F'
            mx = max(mx, (true_cnt + false_cnt))
        
        # Return the maximum consecutive answers
        return mx
