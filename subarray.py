class Solution:

    def maxSubArray(self, A):
        maxSum = -100000000000000000000
        maxHere = 0
        for e in A:
            maxHere += e
            if maxSum < maxHere:
                maxSum = maxHere
            if maxHere < 0:
                maxHere = 0
        return maxSum


sol=Solution()


a = [2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum contiguous sum is", sol.maxSubArray(a))