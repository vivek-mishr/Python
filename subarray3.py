class Solution:

    def maxSubArray(self, A):
        max_ending_here = max_so_far = A[0]
        for number in A[1:]:
            max_ending_here = max(max_ending_here + number, number)
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far


sol=Solution()
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", sol.maxSubArray(a))