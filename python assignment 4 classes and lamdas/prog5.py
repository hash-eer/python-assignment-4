# Write a Python class to find the three elements that sum to zero from a set of n real numbers. Input
# array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]

class validation:
    def three_numbers(self,arr):
        n=len(arr)
        list=[]
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        list.append([arr[i],arr[j],arr[k]])
        print(list)
                        
                        
arr=[-25, -10, -7, -3, 2, 4, 8, 10]                  
validation().three_numbers(arr)