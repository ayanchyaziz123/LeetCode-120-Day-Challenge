from collections import Counter
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert paragraph to lowercase and split into words
        words = re.findall(r'\w+', paragraph.lower())
        
        # Create a set of banned words for efficient lookup
        banned_set = set(banned)
        
        # Count the frequency of each word
        word_count = Counter(word for word in words if word not in banned_set)
        
        # Find the most common word that is not banned
        most_common_word = max(word_count, key=word_count.get)
        
        return most_common_word
