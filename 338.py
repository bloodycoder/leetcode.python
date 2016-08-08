class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
    	ans = [0]
    	for i in range(1,num+1):
    		value = ans[i>>1]+(i&1)
    		ans.append(value)
    	return ans
