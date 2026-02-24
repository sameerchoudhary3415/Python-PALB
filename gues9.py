#Given an array arr[] denoting heights of n towers and a positive integer k.  
#For each tower, you must perform exactly one of the following operations exactly once. 
 
#Increase the height of the tower by k 
#Decrease the height of the tower by k 
#Find out the minimum possible difference between the height of the shortest and tallest towers 
#after you have modified each tower. 
 
#You can find a slight modification of the problem here. 
#Note: It is compulsory to increase or decrease the height by k for each tower. After the operation, 
#the resultant array should not contain any negative integers. 
 
#Examples : 
 
#Input: k = 2, arr[] = [1, 5, 8, 10] 
#Output: 5 
class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n = len(arr)
        arr.sort()

        ans = arr[n-1] - arr[0]   # initial difference

        smallest = arr[0] + k
        largest = arr[n-1] - k

        for i in range(n-1):

            if arr[i+1] - k < 0:
                continue

            min_height = min(smallest, arr[i+1] - k)
            max_height = max(largest, arr[i] + k)

            ans = min(ans, max_height - min_height)

        return ans
