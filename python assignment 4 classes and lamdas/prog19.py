# 9) Write a Python program to find the elements of a given list of strings that contain specific substring
# using lambda.
# Original list: ['red', 'black', 'white', 'green', 'orange']
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to
# search: abc Elements of the said list that contain specific substring: []

list1= ['red', 'black', 'white', 'green', 'orange']

def find_substring(list1, sub_x):
    result=list(filter(lambda x : sub_x in x , list1 ))
    return result

print("this is a current list")
print(list1)
sub_x=input("enter the substring:")
print(find_substring(list1,sub_x))
