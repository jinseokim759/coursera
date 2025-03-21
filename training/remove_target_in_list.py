nums = [1, 2, 3, 4, 5]

def ex1(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            del nums[i]
            return nums

def ex2(nums, target):
    nums.remove(target)
    return nums

        
print(ex1(nums, 2))
#print(ex2(nums, 2))  