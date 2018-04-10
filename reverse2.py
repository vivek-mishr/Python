class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        
        i = len(A) - 1
        S = ''
        
        while i >= 0:
            while i >= 0 and A[i] == ' ':
                i -= 1
            
            S += ' '
            j = i
            
            while j >= 0 and A[j] != ' ':
                j -= 1
            
            S += A[j+1:i+1]
            i = j
            
        S = S.strip()
       
        return S


sol = Solution()
x = input("enter the string ")
y = sol.reverseWords(x)
print(y)