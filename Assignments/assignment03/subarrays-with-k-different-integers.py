def subarraysWithKDistinct(nums, k):
    def getKMost(k):
        from collections import defaultdict
        left=res=0
        counter=defaultdict(int)
        for right,num in enumerate(nums):
            counter[num]+=1

            while len(counter)>k:
                counter[nums[left]]-=1

                if counter[nums[left]]==0:
                    del counter[nums[left]]
                left+=1
            #print(counter)
            res+=right-left+1
        return res
    return getKMost(k)-getKMost(k-1)

nums=[1,2,1,2,3]
print(subarraysWithKDistinct(nums, 2))
