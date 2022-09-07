# #Write a Python program to check whether a given string contains a capital letter, a lower case letter, a
# number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid
# string

def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) ,
    lambda str1: any(x.islower() for x in str1) ,
    lambda str1: any(x.isdigit() for x in str1) ,
    lambda str1: len(str1) < 11                ,]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
print(check_string(s))
    