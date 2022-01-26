def threeSumClosest(nums, target):
    n=len(nums)
    nums.sort()
    minDiff=float(100000)
    for i in range(0,n-2):
        left=i+1
        right=n-1
        while left<right:

            triSum=nums[i]+nums[left]+nums[right]
            diff=abs(triSum-target)
            #print(nums[i],nums[left],nums[right],"triSum : ",triSum,"diff : ",diff)
            if diff<minDiff:
                minDiff=diff
                closestSum=triSum

            if triSum>target:
                right-=1
            else:
                left+=1
            #print("closestSum - ", closestSum)
    return closestSum

nums=[-1,2,1,-4]
print(threeSumClosest(nums,1))
