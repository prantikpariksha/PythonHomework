list1=[]

def Func1(i):
    
        if (i%3==0 and i%5==0):
            i="FizzBuzz"
            list1.append(i)
        elif (i%3==0):
            i="Fizz"
            list1.append(i)
        elif (i%5==0):
            i="Buzz"
            list1.append(i)
        else:
            list1.append(i)
            
for i in range(1,101):
    if(i>1):
        for j in range(2,i):
            if (i%j==0):
                Func1(i)
                break
        else:
            i="Prime"
            list1.append(i)
    else:
        list1.append(i)
        
print(list1)
        
        

