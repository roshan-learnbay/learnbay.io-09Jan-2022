def maximumUniqueSubarray(nums):
    from collections import defaultdict
    left=sum=0
    maxSum=-1
    counter=defaultdict(int)
    for right,num in enumerate(nums):

        counter[num]+=1
        #print(right,num,counter,sum,maxSum)
        while counter[num]>1:
            counter[nums[left]]-=1
            sum-=nums[left]
            left+=1
            #print(right,num,counter,sum,maxSum,"inside")
        sum+=nums[right]
        maxSum=max(sum,maxSum)
    return maxSum

nums=[5,2,1,2,5,2,1,2,5]
print(maximumUniqueSubarray(nums))
