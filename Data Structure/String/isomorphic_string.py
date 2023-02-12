def foo(s1,s2):
    if len(s1)!=len(s2):
        return False
    hm={}
    hm2={}
    for i in range(len(s1)):
        a=s1[i]
        b=s2[i]
        if a in hm or b in hm:
            continue
        elif a in hm.values() or b in hm.values():
            continue
        else:
            hm[s1[i]]=s2[i]
    new=""
    try:
        for i in range(len(s2)):
            new=new+hm[s1[i]]
        if new==s2:
            return True
        return False
    except:
        return False


print(foo("paper","title"))