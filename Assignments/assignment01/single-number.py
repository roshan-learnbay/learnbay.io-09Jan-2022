def single_number(nums):
    result=0
    n=len(nums)
    for i in range(n):
        result^=nums[i]

    return result

#Driver

nums=[2,3,8,4,5,5,4,3,2]
print(single_number(nums))
