class Solution:
    def sortByFreq(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        # Sort characters based on (frequency, character)
        sorted_chars = sorted(freq.keys(), key=lambda x: (freq[x], x))
        
        result = ""
        
        for ch in sorted_chars:
            result += ch * freq[ch]
        
        return result
