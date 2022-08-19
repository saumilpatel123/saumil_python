#magic method : in magic method never required for manual called
# class Point:
#     def __init__(self) :
#       print("init called")
# p1=Point()
# class A:
#     def __init__(self,num1,num2):
#          print("num1=",num1)
#          print("num2=",num2)
# obj=A(12,54)
class Point:
     def __init__(self,x,y) :
       print("init called")
       self.x=x
       self.y=y
       print("X:",self.x,"Y:",self.y)
       # magic str method always done with return value
     def __str__(self):
       print("str called")
       return "({0},{1})".format(self.x,self.y)
       #magic add method always return object
     def __add__(self,obj):
        print("add called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)
p1=Point(10,20)
p2=Point(30,40)
print(p1)
print(p2)
print("Addition:",p1+p2)