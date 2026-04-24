class Solution:
    def minMen(self, arr):
        #code here 
    # User function Template for python3
        n = len(arr)
        intervals = []

        # Build valid intervals
        for i in range(n):
            if arr[i] != -1:
                l = max(0, i - arr[i])
                r = min(n - 1, i + arr[i])
                intervals.append((l, r))

        # Sort intervals by start
        intervals.sort()

        ans = 0
        i = 0
        covered = 0   # next uncovered position

        while covered < n:
            farthest = -1

            # Find best interval starting before/equal covered
            while i < len(intervals) and intervals[i][0] <= covered:
                farthest = max(farthest, intervals[i][1])
                i += 1

            # Cannot cover current position
            if farthest < covered:
                return -1

            ans += 1
            covered = farthest + 1

        return ans
