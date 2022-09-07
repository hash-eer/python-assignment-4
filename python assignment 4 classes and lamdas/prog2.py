# Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets
# must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are
# invalid.
class Answer:
    
    def checkparam(self,str):
        check={')':'(','}':'{',"]":"["}
        list=[]
        
        for i in str:
            if i in check.values():
                list.append(i)
            elif list and check[i]==list[-1]:
                list.pop()
            else:
                return False
        return list==[]
    

            
str=input("enter the brackets:")
result=Answer().checkparam(str)
if result==True:
    print("it is valid")
else:
    print("Invalid")