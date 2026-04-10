class Solution:

    def winner(self, arr):
        pass
        from collections import Counter
        
        freq = Counter(arr)
        
        max_votes = 0
        winner = ""
        
        for name in freq:
            if freq[name] > max_votes:
                max_votes = freq[name]
                winner = name
            elif freq[name] == max_votes:
                if name < winner:
                    winner = name
        
        return [winner, str(max_votes)]
