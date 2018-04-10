class Solution:

    def ispalindrome(self, A):

        char_list = []

        for i in range(len(A)):
            if A[i].isalnum():
                char_list.append(A[i].lower())

        N = len(char_list)

        for i in range(N // 2):
            if char_list[i] != char_list[N - i - 1]:
                return 0

        return 1


sol = Solution()
for line in open('/home/vivek/x.txt', 'r').readlines():
    y = sol.ispalindrome(line)  # type: int
    if y == 1:
        print(line + "is a palindrom")
    else:
        print(line + " not a palindrom ")
