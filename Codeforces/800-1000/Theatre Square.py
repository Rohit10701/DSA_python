import math
w = list(map(int,input().split()))

n=w[0]
m=w[1]
a=w[2]


count_x = math.ceil(n/a)
count_y = math.ceil(m/a)

print(count_x*count_y)