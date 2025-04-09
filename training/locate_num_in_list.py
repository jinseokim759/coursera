nums = [1, 2, 3, 4, 5, 6, 8, 9, 10]

def locate_num(nums, num):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == num:
            return nums[mid]
        elif nums[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(locate_num(nums, 4))  #case1: num is in the nums
print(locate_num(nums, 12)) #case2: num is bigger than numbers in nums
print(locate_num(nums, 7))  #case3: num is smaller than the biggest number in nums, but is not in the nums