#Write a Python class to implement pow(x, n)
class validation:
    def pow(self,x,n):
        if n==0:
            return 1
        elif n<0:
            return self.pow(1/x,-n)
        elif n%2==0:
            temp=self.pow(x,n/2)
            return temp*temp
        else:
            return x*self.pow(x,n-1)
        
        
x=int(input("enter the base number to perform operation:"))
n=int(input("enter the power to perform operation:"))
print("result of the operation is",validation().pow(x,n))