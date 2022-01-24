def sorted_square(nums):
    n=len(nums)
    j=n-1
    for i in range(n):
        nums[i]=nums[i]*nums[i]

    while(j>0):
        print(nums)
        if(nums[0]>nums[j]):
            tmp=nums[0]
            nums[0]=nums[j]
            nums[j]=tmp
        j-=1

    return nums


nums=[-4,-1,0,3,10]
print(sorted_square(nums))


=============================================================

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)

#         #Approach1
#         j=n-1
#         for i in range(n):
#             nums[i]=nums[i]*nums[i]
#         i=0
#         while(j>i):
#             print(nums)
#             if(nums[i]>nums[j]):
#                 nums[i],nums[j] = nums[j], nums[i]
#                 if nums[i]<=nums[j-1]:
#                     i+=1
#             j-=1

#         return nums

        #Approach2
        low=0
        high=n-1
        res=[None]*n
        idx=n-1
        while low<high:
            lowSq=nums[low]*nums[low]
            highSq=nums[high]*nums[high]
            if lowSq<highSq:
                print(idx)
                res[idx]=highSq
                high-=1
                idx-=1
            else:
                print(idx)
                res[idx]=lowSq
                low+=1
                idx-=1
        return res
