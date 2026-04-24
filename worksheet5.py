class Solution:
  def minOperations(self, arr):
    # code here# User function Template for python3
        # Calculate original sum
        total = sum(arr)
        target = total / 2
        
        # Max heap using negative values
        max_heap = [-x for x in arr]
        heapq.heapify(max_heap)
        
        operations = 0
        reduced_sum = 0
        
        # Keep reducing until removed sum reaches half
        while reduced_sum < target:
            largest = -heapq.heappop(max_heap)
            
            half = largest / 2
            reduced_sum += half
            
            # Push halved value back
            heapq.heappush(max_heap, -half)
            
            operations += 1
        
        return operations
