class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # Stack to store unmatched parentheses along with their indices
        n = len(s)  # Length of the string
        
        # Iterate through each character of the string
        for i in range(n):
            if s[i] == '(' or s[i] == ')':  # Check if the character is a parenthesis
                if not stack:  # If the stack is empty
                    stack.append([s[i], i])  # Push the current parenthesis and its index to the stack
                    continue
                v1 = stack[-1][0]  # Get the value of the top element in the stack
                v2 = s[i]  # Get the value of the current character
                
                # If the top element in the stack and the current character form a valid pair of parentheses
                if v1 == '(' and v2 == ')':
                    stack.pop()  # Pop the top element from the stack (matching pair found)
                else:
                    stack.append([v2, i])  # Push the current character and its index to the stack (unmatched)
        
        check = []  # List to store indices of unmatched parentheses
        # Pop elements from the stack and store their indices in 'check'
        while stack:
            ind = stack[-1][1]
            check.append(ind)
            stack.pop()
        
        res = ""  # Initialize the result string
        # Reconstruct the string without the characters at indices present in 'check'
        for i in range(n):
            if i not in check:
                res += s[i]  # Append characters to the result string
        
        return res  # Return the resulting string

# Example usage:
sol = Solution()
print(sol.minRemoveToMakeValid("lee(t(c)o)de)"))  # Output: "lee(t(c)o)de"
