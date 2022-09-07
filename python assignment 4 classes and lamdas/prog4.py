# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose
# sum equals a specific target number. Note: There will be one solution for each input and do not use the
# same element twice. Input: numbers= [10,20,10,40,50,60,70], target=50 Output: 3, 4

class validation:
    def pair_indices(self,arr,target):
        arr.sort()
        left=0
        right=len(arr)-1
        
        while(left<=right):
            if arr[left] + arr[right] >target:
                right=right-1
            elif arr[left] +arr[right] <target:
                left=left+1
            elif arr[left] +arr[right]== target:
                return print("pairs that matched indexes are ",left,right)
            
arr=[10,20,30,40,50,60,70]
target=50
validation().pair_indices(arr,target)
        
           
