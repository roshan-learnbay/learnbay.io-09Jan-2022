def fourSum(nums, target):
    n=len(nums)
    ans=[]
    nums.sort()
    for i in range(0,n-3):
        for j in range(i+1,n-2):
            left=j+1
            right=n-1

            while(left<right):
                quadSum=nums[i]+nums[j]+nums[left]+nums[right]

                if quadSum>target:
                    right-=1
                elif quadSum==target:
                    #print("found : ", nums[i],nums[j],nums[left],nums[right])
                    #print("index : ",i,j,left,right, quadSum)
                    ans.append((nums[i],nums[j],nums[left],nums[right]))
                    left+=1
                else:
                    left+=1
                #print("while loop completes")

    return set(ans)


nums=[1,0,-1,0,-2,2]
print(fourSum(nums,0))
