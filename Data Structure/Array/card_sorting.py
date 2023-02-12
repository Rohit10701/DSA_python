ls=[1,1,2,3,4]
def count(str):
    count=0
    for ch in str:
        if ch=='1':
            count+=1
    return count

def card(ls):
    con={}
    for ele in ls:
        con[ele]=count(bin(ele)[2:])
    print(sorted(con.items(), key=lambda kv:(kv[1], kv[0])))
    
print(card(ls))