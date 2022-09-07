# Write a python class which has 2 methods get_string and print_string. get_string takes a string from
# the user and print_string prints the string in reverse order
class validation:
    
    def __init__(self):
        self.s=""
        
    def get_string(self):
        self.s=input("enetr the string")
        
        
    def print_string(self):
         s1=self.s
         l=[]
         l=s1.split(" ")
         l=l[-1::-1]
         result=' '.join(l)
         print( result)
        

obj=validation()
obj.get_string()
obj.print_string()
