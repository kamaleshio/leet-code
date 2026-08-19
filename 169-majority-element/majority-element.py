class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=None
        count=0

        for i in nums:
            if count==0:
                n=i

            if i == n:
                count+=1
            else:
                count-=1
        return n
        