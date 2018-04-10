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


sol=Solution()

x=input("enter file name ")  # type: str
with open(x, 'r') as infile:            #with open(r"/home/vivek/x.txt", 'r') as infile:
    data = infile.read()
    print(data)



                                                                 #filename = "/home/vivek/x.txt"
                                                                #file = open(filename, 'r')
                                                                #for line in open('fname','r').readlines(
y = sol.ispalindrome(data)                                       # type: int
print(data + "is ")
if y == 1:
    print("yes")
else:
    print("no")

# with open("/home/vivek/x.txt") as f:
 #3   for line in f:
#       print(f)