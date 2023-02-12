def boat(people,limit):
        people.sort()
        people = people[::-1]
        
        l,r=0,len(people)-1
        count=0
        print(people)
        while l<=r:
            if (people[l]+people[r])<=limit and l!=r:
                count+=1
                l+=1
                r-=1
                
            else:
                count+=1
                l+=1
        return count

print(boat([3,5,3,4],5))