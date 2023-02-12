# An array a
#  is good if for all pairs of adjacent elements, ai
#  and ai+1
#  (1≤i<n
# ) are of different parity. Note that an array of size 1
#  is trivially good.

# You are given an array of size n
# .

# In one operation you can select any pair of adjacent elements in which both elements are of the same parity, delete them, and insert their product in the same position.

# Find the minimum number of operations to form a good array.

def good_array(ls):
    if len(ls)==1:
        return 0
    i=0
    count=0
    while i<len(ls)-1:
        if ls[i]%2!=ls[i+1]%2:
            i=i+1
        else:
            ls[i+1]=ls[i]*ls[i+1]
            ls.pop(i)
            count+=1
    return count


n=int(input())
ls=[]
for i in range(n):
    x=int(input())
    ls.append(list(map(int, input().split())))

for i in range(n):
    print(good_array(ls[i]))
