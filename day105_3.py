class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start iterating from the end of the string
        i = len(s) - 1
        
        # Skip trailing spaces
        while s[i] == ' ' and 0 <= i:
            i -= 1
        
        # Count the length of the last word
        cnt = 0
        while s[i] != ' ' and 0 <= i:
            i -= 1
            cnt += 1
        
        # If no word is found, count the length of the entire string
        if cnt == 0:
            while 0 <= i:
                cnt += 1
        
        return cnt
