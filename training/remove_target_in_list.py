nums = [1, 2, 3, 4, 5]

def ex1(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            del nums[i]
            return nums
        
print(ex1(nums, 2))