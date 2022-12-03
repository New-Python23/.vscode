def twoSum(nums, target):
    i = 0
    j = 0
    
    while True:
        if nums[i] + nums[j] == target:
            break
        else:
            if j > len(nums):
                j = 0
                i += 1
            else:
                j += 1
    print(f"{nums[i]} + {nums[j]} = {target}")

twoSum([1,2,3], 4)
