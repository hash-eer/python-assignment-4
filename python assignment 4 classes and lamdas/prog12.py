# 2) Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# list.sort(reverse=True)
# print(list)

list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
list.sort(key=lambda a:a[1])
print(list)


