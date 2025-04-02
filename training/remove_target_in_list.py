
nums = [1, 2, 3, 4, 4, 5, 4, 4, 7, 8, 6, 6, 6, 4, 3]

def ex1(nums, target):
    i, j = 0, 0
    while i < len(nums):
        if nums[i] != target:
            nums[j] = nums[i]
            j += 1
        i += 1
    del nums[j:]
    return nums
        
print(ex1(nums, 4))