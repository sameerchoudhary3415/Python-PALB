class Solution:
    def maxPeople(self, arr):
       
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []

        # Count visible on left side
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = i if not stack else i - stack[-1] - 1
            stack.append(i)

        stack = []

        # Count visible on right side
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            right[i] = (n - i - 1) if not stack else stack[-1] - i - 1
            stack.append(i)

        ans = 1
        for i in range(n):
            ans = max(ans, left[i] + right[i] + 1)

        return ans
