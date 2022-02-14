def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)

    i=0
    while i<n and nums[i]!=0:
        i+=1
    j=i+1
    while j<n:
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return nums

nums=[1,0,2,0,13,14,0,8]
print(moveZeroes(nums))
