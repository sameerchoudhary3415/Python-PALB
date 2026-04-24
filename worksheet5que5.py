class Solution:
    def has132Pattern(self, arr):
        # code here 
        n = len(arr)
        if n < 3:
            return False

        stack = []
        third = float('-inf')

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            if arr[i] < third:
                return True

            while stack and stack[-1] < arr[i]:
                third = stack.pop()

            stack.append(arr[i])

        return False
