"""
Description:This section of code accepts user input from the console and based 
on the input it checks for equality between any two of them. If the comparison
betwen any one of the given value is successful it displays "TRUE" else it will
displays "False"

"""
#value1=5     # <-- Use if hardcoded input is required
#value2=6     # <-- Use if hardcoded input is required
#value3="7"   # <-- Use if hardcoded input is required

value1=input("Please type 1st digit or string in the console and hit enter:")
value2=input("Please type 2nd digit or string in the console and hit enter:")
value3=input("Please type 3rd digit or string in the console and hit enter:")



reslt1=True
reslt2=False


def Func1 (var1,var2,var3):
 
     var1=int(var1)  #string to Integer- when using hardcoded input
     var2=int(var2)  #string to Integer- when using hardcoded input
     var3=int(var3)  #string to Integer- when using hardcoded input
     
     if var1==var2 or var3==var2 or var3==var1:
        
         print("Result is:", reslt1)
              
     else:
         print("Result is:", reslt2)


var5=Func1(value1,value2,value3)



