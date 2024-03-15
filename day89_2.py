class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initialize a stack to store vowels and a list to store the result
        st = []
        res = []
        # Define a list of vowels
        check = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        
        # Iterate through the input string to push vowels onto the stack
        for c in s:
            if c in check:
                st.append(c)
        
        # Initialize an index to access vowels from the stack
        e = len(st) - 1
        
        # Iterate through the input string again
        for c in s:
            # If the character is a vowel, pop a vowel from the stack and append it to the result
            if c in check:
                res.append(st[e])
                e -= 1
            # If the character is not a vowel, simply append it to the result
            else:
                res.append(c)
        
        # Return the result as a string
        return ''.join(res)
