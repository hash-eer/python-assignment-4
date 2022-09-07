# Write a Python program to find if a given string starts with a given character using Lambda.

check_char = lambda a,x : True if a.startswith(x) else False

a=input("enter the string:")
x=input("enter the character to check the first letter is True or Not:")
print(check_char(a,x))