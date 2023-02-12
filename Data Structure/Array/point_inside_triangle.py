def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
 

def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
    A = area (x1, y1, x2, y2, x3, y3)
 
    A1 = area (x, y, x2, y2, x3, y3)

    A2 = area (x1, y1, x, y, x3, y3)

    A3 = area (x1, y1, x2, y2, x, y)

    if(A == A1 + A2 + A3):
        return True
    else:
        return False
 
def check(x1,y1,x2,y2,x3,y3,xp,yp,xq,yq):
    if isInside(x1,y1,x2,y2,x3,y3,xp,yp):
        return 1
    if isInside(x1,y1,x2,y2,x3,y3,xq,yq):
        return 2
    if isInside(x1,y1,x2,y2,x3,y3,xp,yp) and isInside(x1,y1,x2,y2,x3,y3,xq,yq):
        return 3
    if not isInside(x1,y1,x2,y2,x3,y3,xp,yp) and not isInside(x1,y1,x2,y2,x3,y3,xq,yq):
        return 4
    else:
        return 0
# A(0, 0), B(20, 0) and C(10, 30)
print(check(2,2,7,2,5,4,4,3,7,4))