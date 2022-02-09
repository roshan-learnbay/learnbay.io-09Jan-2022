def numSubarrayProductLessThanK(nums, k):
    n=len(nums)
    if k<=1:
        return 0
    product=1
    start=end=0
    res=0
    while end<n:
        product*=nums[end]
        while product>=k:
            #print(start,product)
            product //=nums[start]
            start+=1
        res+=end-start+1
        end+=1
    return res

print(numSubarrayProductLessThanK([1,1,1],1))
