def Func1(i):
        if (i%3==0 and i%5==0):
            print("FizzBuzz")
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("Buzz")
        else:
            print(i)
            
for i in range(1,101):
    if(i>1):
        for j in range(2,i):
            if (i%j==0):
                Func1(i)
                break
        else:
            print(i,"-This is a primenumber:")
    else:
        print(i)  

