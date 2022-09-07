# #Write a Python class to reverse a string word by word.
# Input string : 'hello .py' Expected Output : '.py hello'
class py_solution:
    def reverse_words(self, s):
        l=s.split(" ")
        l=l[-1::-1]
        result=' '.join(l)
        return result
          
s=input("enter the strings")
print(py_solution().reverse_words(s))