class Solution:
    def combinationSum(self, n, k):
        # code here
        
        ans = []

        def solve(start, k, target, path):
            if k == 0:
                if target == 0:
                    ans.append(path[:])
                return

            for num in range(start, 10):
                if num > target:
                    break
                path.append(num)
                solve(num + 1, k - 1, target - num, path)
                path.pop()

        solve(1, k, n, [])
        return ans
