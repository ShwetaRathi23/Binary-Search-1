#Time Complexity :O(log n)
#Space Complexity :O(1)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=int(low+(high-low)/2)
            if nums[mid]==target:
                return mid
            elif nums[low]<=nums[mid]:
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[mid]<=nums[high]:
                if nums[mid]<target and target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        #==> while(low<high)
        #if nums[high]==target:
        #    return high
        return -1