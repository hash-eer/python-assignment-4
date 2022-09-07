# Write a Python class named Circle constructed by a radius and two methods which will compute the
# area and the perimeter of a circle.

class validation:
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return self.r**2*3.15
    
    def perimeter(self):
        return 2*3.14*self.r

n=int(input("enter the radius to perform area and perimeter of the circle:"))
    
obj=validation(n)
print("area of the circle is :",obj.area())
print("perimeter of the circle is :",obj.perimeter())