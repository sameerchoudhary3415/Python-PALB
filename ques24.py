class Solution:
    def median(self, mat):
    	# code here 

        n = len(mat)
        m = len(mat[0])

        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)

        desired = (n * m) // 2

        while low < high:
            mid = (low + high) // 2

            count = 0

            # Count elements <= mid
            for row in mat:
                # Binary search in each row
                l, r = 0, m
                while l < r:
                    mid2 = (l + r) // 2
                    if row[mid2] <= mid:
                        l = mid2 + 1
                    else:
                        r = mid2
                count += l

            if count <= desired:
                low = mid + 1
            else:
                high = mid

        return low
