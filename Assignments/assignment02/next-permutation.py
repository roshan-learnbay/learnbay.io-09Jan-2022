def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n=len(nums)
    lastInc=-1
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            lastInc=i

    if lastInc==-1:
        for i in range(n//2):
            nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
        return

    index=lastInc
    for i in range(index+1,n):
        if nums[i]>nums[lastInc-1] and nums[i]<nums[index]:
            index=i
    nums[lastInc-1],nums[index]=nums[index],nums[lastInc-1]
    nums[lastInc:n]=sorted(nums[lastInc:n])
    return nums


nums=[1,2,3,5,4,2]
print(nextPermutation(nums))
