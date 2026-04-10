class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack = []
        
        for ch in s:
            while stack and stack[-1] < ch and k > 0:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # If k is still left, remove from end
        while k > 0:
            stack.pop()
            k -= 1
        
        return "".join(stack)
