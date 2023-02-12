n= int(input())

x=0
for i in range(n):
    op=list(input())
    op=sorted(op)
    if ['+','+'] == op[:-1]:
        x+=1
    else:
        x-=1
print(x)