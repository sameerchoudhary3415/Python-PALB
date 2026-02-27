class Solution(object):
    def combinationSum2(self, candidates, target):
       
        candidates.sort()  # Step 1: Sort to handle duplicates
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                
                # Step 2: Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # If current number exceeds remaining, stop (optimization)
                if candidates[i] > remaining:
                    break
                
                path.append(candidates[i])
                
                # Step 3: Use i+1 (cannot reuse same element)
                backtrack(i + 1, path, remaining - candidates[i])
                
                path.pop()

        backtrack(0, [], target)
        return result
