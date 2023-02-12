ls=[1,2,3,4,5]
res=[]
def find(ls):
    for i in range(len(ls)):
        for j in range(i,len(ls)):
            if int((i**2+j**2)**(0.5)) in ls:
                res.append(i)
                res.append(j)
                res.append(int((i**2+j**2)**(0.5)))
                break
    return res

print(find(ls))
