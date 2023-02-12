
def count(num):
    count=0
    pi = "314159265358979323846264338327"
    for i in range(len(str(num))):
        ele = str(num)[i]
        if pi[i]==ele:
            count+=1
        else:
            break
    return count


ls=[]
n=int(input())

for _ in range(n):
    ls.append(input())

for ele in ls:
    print(count(ele))