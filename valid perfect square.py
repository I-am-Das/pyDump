class Solution(object):
    def isPerfectSquare(self, num):
        if num < 1:
            return False
        if num == 1:
            return True
        l,r= 1, num
        while l<=r:
            m=l+(r-l)//2
            s=m*m
            if s==num:
                return True
            elif s< num:
                l=m+1
            else:
                r=m-1
        return False
