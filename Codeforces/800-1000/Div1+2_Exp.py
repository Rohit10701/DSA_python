# A. Exponential Equation
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# You are given an integer n
# .

# Find any pair of integers (x,y)
#  (1≤x,y≤n
# ) such that xy⋅y+yx⋅x=n
# .

# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.

# Each test case contains one line with a single integer n
#  (1≤n≤109
# ).

# Output
# For each test case, if possible, print two integers x
#  and y
#  (1≤x,y≤n
# ). If there are multiple answers, print any.

# Otherwise, print −1
# .

# 5
# 3
# 7
# 42
# 31250
# 20732790

# -1
# -1
# 2 3
# 5 5
# 3 13

    
def find(n):
    if(n%2==0):
        print(1,int(n/2))
    else:
        print(-1)


n= int(input())
w=[]
for _ in range(n):
    w.append(int(input()))
for i in range(n):
    find(w[i])
