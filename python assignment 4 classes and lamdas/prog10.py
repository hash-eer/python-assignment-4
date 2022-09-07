#Write a Python program to get the class name of an instance in Python.

class car:
    def parts():
        pass
 
c = car()
 

#print(c.__class__)
 
# this prints the name of the class
classes = c.__class__
# prints the name of the class
print(classes.__name__)