class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
        	ans = ans^i
        return ans
A = Solution()
print A.singleNumber([2,2,9,3,3,7,7])