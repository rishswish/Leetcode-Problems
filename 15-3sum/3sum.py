class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i=0
        nums.sort()
        result=[]
        if len(nums)==3:
            if sum(nums)==0:
                result.append(nums)
        while i<len(nums)-3:
            l=i+1
            r=len(nums)-1
            res=[]
            while l<r:
                summ=nums[l]+nums[r]
                target=nums[i]*-1
                if summ>target:
                    r-=1
                if summ<target:
                    l+=1
                if summ==target:
                    res=[nums[i],nums[l],nums[r]]
                    result.append(res)
                    temp_l=l+1
                    while nums[l]==nums[temp_l] and temp_l<len(nums)-1:
                        temp_l+=1
                    l=temp_l
                    temp_r=r-1
                    while nums[r]==nums[temp_r] and temp_r>i:
                        temp_r-=1
                    r=temp_r

            t=i+1
            while nums[i]==nums[t] and t<len(nums)-1:
                t+=1
            print(nums[i],nums[t])
            i=t

        return result





        