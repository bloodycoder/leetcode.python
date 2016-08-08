class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4 != 0)
        
#win  1 2 3 5 6 7 9 10 11 13 14 15

#lose 4 8 12 16