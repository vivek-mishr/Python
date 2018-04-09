import re


class Solution:

    def ispalindrome(self, A):
        rev = re.sub(r'\W+', '', A)
        rev = rev.lower()
        final = rev[::-1]
        if rev == final:
            return 1
        else:
            return 0


sol = Solution()
x = input("enter the string ")
y = sol.ispalindrome(x)  # type: int
if y == 1:
    print("yes")
else:
    print("no")