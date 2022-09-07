# Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6]
# Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
class validation:
    def subset(self,nums):
        result=[[]]
        
        for num in nums:
            result+=[i + [num] for i in result]
        return result
       
    
nums=[4,5,6]
print(validation().subset(nums))