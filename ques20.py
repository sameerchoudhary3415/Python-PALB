class Solution:
    def minSwap(self, arr, k):
        n = len(arr)

        # Count good elements (<= k)
        good = 0
        for x in arr:
            if x <= k:
                good += 1

        # Count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1

        ans = bad

        # Slide window
        i = 0
        j = good

        while j < n:
            # Remove left element
            if arr[i] > k:
                bad -= 1

            # Add right element
            if arr[j] > k:
                bad += 1

            ans = min(ans, bad)

            i += 1
            j += 1

        return ans
