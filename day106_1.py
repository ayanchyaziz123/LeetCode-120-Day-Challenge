class Solution:
    def makeGood(self, s: str) -> str:
        stack = []  # Initialize an empty stack to store characters
        n = len(s)  # Length of the input string
        i = 0  # Initialize a variable to traverse the string
        while i < n:  # Loop through the string until the end
            while i < n and stack and stack[-1] != s[i] and stack[-1].lower() == s[i].lower():
                # Check if there are characters in the stack, 
                # and if the last character in the stack is not equal to the current character
                # and if they are equal ignoring the case.
                stack.pop()  # If the conditions are met, remove the last character from the stack
                i += 1  # Move to the next character in the string
            if i >= n:  # If we have reached the end of the string, continue to the next iteration
                continue
            stack.append(s[i])  # Append the current character to the stack
            i += 1  # Move to the next character in the string
        return ''.join(stack)  # Join the characters in the stack to form the final string

# Example usage:
sol = Solution()
print(sol.makeGood("leEeetcode"))  # Output: "leetcode"
