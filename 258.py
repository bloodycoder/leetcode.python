class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num%9==0):
        	ans = 9
        else:
        	ans = num%9
        return ans
A = Solution()
for i in range(10,100):
    print i,A.addDigits(i)
