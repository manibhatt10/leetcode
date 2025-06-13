class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        
        """
        if n<1:
            return False
        x=0
        while pow(2,x)<=n:
            if n==pow(2,x):
                return True
            x=x+1
        return False
        

