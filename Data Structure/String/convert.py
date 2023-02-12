#print(ord("a")-ord("A"))
def convert(str_ptr):
    hm={1:'A',2:'B',3:'C',4:'D',5:'E',
        6:'F',7:'G',8:'H',9:'I'}
    res=""
    for i in range(len(str_ptr)):
        res=res+hm[ord(str_ptr[i])-ord('a')+1]
    return res

print(convert('abcd'))