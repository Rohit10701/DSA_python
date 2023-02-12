# Taisia has n
#  six-sided dice. Each face of the die is marked with a number from 1
#  to 6
# , each number from 1
#  to 6
#  is used once.

# Taisia rolls all n
#  dice at the same time and gets a sequence of values a1,a2,…,an
#  (1≤ai≤6
# ), where ai
#  is the value on the upper face of the i
# -th dice. The sum of this sequence is equal to s
# .

# Suddenly, Taisia's pet cat steals exactly one dice with maximum value ai
#  and calculates the sum of the values on the remaining n−1
#  dice, which is equal to r
# .

# You only know the number of dice n
#  and the values of s
# , r
# . Restore a possible sequence a
#  that fulfills the constraints.

# Input
# The first line contains the integer t
#  (1≤t≤1000
# ) — the number of testcases.

# Each testcase is given on a separate line and contains three integers n
# , s
# , r
#  (2≤n≤50
# , 1≤r<s≤300
# ).

# It is guaranteed that a solution exists.

# Output
# For each testcase, print: n
#  integers a1,a2,…,an
#  in any order. It is guaranteed that such sequence exists.

# If there are multiple solutions, print any.

# 7
# 2 2 1
# 2 4 2
# 4 9 5
# 5 17 11
# 3 15 10
# 4 4 3
# 5 20 15

# 1 1
# 2 2 
# 1 2 2 4
# 6 4 2 3 2
# 5 5 5
# 1 1 1 1
# 1 4 5 5 5

def dice(n,s,r):
    missing_num = s-r
    rest_sum = r
    ls=[]
    rem_num=n-1
    i=0
    while i<n:
        if rem_num == 0:
            break
        rem = r//rem_num
        ls.append(rem)
        r = r-rem
        rem_num-=1
        i+=1
    
    ls.append(missing_num)
    return ls

n=int(input())
ls=[]
for i in range(n):
    ls.append(list(map(int, input().split())))

for ele in ls:
    map=dice(ele[0],ele[1],ele[2])
    print(*map)