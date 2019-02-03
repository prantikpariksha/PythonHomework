"""This section of code is having a function defined that allows you to add things to that 
list. Anything that's passed to this function should get added to myUniqueList, unless its
value already exists in myUniqueList. If the value doesn't exist already, it should be added
and the function should return True. If the value does exist, it should not be added, and
the function should return False"""

myUniqueList=[] 
RejectedItem=[]

def Func1(num):
       if num in myUniqueList:           #check whether the item is already in the list or not
           RejectedItem.append(num)      #if already present put it in the rejected list
           return (False,RejectedItem)
 
       else:
           myUniqueList.append(num)      #if not present put the actual list
           return (True,myUniqueList)
    
Test1=Func1(8)
Test2=Func1(3)
Test3=Func1(8)
Test4=Func1(11)
Test5=Func1(2)
Test6=Func1(2)
Test7=Func1(11)
Test8=Func1("hello")
Test9=Func1("World")
Test10=Func1("hello")

myLeftovers=RejectedItem
print (myUniqueList)
print (myLeftovers)