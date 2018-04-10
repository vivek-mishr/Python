class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        arr=A.split(" ")
        arr2=reversed(arr)
        return " ".join(arr2)


sol = Solution()
x = input("enter the string ")
y = sol.reverseWords(x)
print(y)