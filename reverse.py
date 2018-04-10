class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        words = A.split(" ")
        words.reverse()
        ans=" ".join(words)
        return ans


sol = Solution()
x = input("enter the string ")
y = sol.reverseWords(x)
print(y)