dim = list(map(int,input().split()))

l=max(dim)
b=min(dim)

#7 3
count_x=0
count_y=0
if (b>=2):
    count_x=l
    count_y=b//2

rem=(b%2)*l//2

print(count_x*count_y+rem)