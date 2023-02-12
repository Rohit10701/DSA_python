def trap(ls):
    
        res=0
        l=0
        r=len(ls)-1
        loc_mxl=0
        loc_mxr=0
        while l<r:
            if(ls[l]<=ls[r]):
                if(ls[l]<=ls[l+1]):
                    if(loc_mxl<ls[l]):
                        loc_mxl=ls[l]
                    if(loc_mxl-ls[l+1]>0):
                        res=res+loc_mxl-ls[l+1]
                    l+=1
                else:
                    if(loc_mxl<ls[l]):
                        loc_mxl=ls[l]
                    res=res+loc_mxl-ls[l+1]
                    l+=1
            else:
                if(ls[r]<=ls[r-1]):
                    if(loc_mxr<ls[r]):
                        loc_mxr=ls[r]
                    if(loc_mxr-ls[r-1]>0):
                        res=res+loc_mxr-ls[r-1]
                    r-=1
                else:
                    if(loc_mxr<ls[r]):
                        loc_mxr=ls[r]
                    res=res+loc_mxr-ls[r-1]
                    r-=1
        return res
height = [9,2,9,3,2,2,1,4,8]

print(trap(height))