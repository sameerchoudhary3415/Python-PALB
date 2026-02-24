class Solution:
    def minJumps(self, arr):
        n = len(arr)

        # If only one element → already at end
        if n <= 1:
            return 0

        # Cannot move anywhere
        if arr[0] == 0:
            return -1

        maxReach = arr[0]
        steps = arr[0]
        jumps = 1

        for i in range(1, n):

            # Reached last index
            if i == n - 1:
                return jumps

            # Update maximum reachable index
            maxReach = max(maxReach, i + arr[i])

            steps -= 1

            # Need another jump
            if steps == 0:
                jumps += 1

                # Cannot move forward
                if i >= maxReach:
                    return -1

                steps = maxReach - i

        return -1
