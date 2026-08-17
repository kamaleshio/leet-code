class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        else:
            r=x//2
            l=1
            while l<=r:
                mid=l+(r-l)//2
                if  mid*mid==x:
                    return mid
                elif mid*mid>x:
                    r=mid-1
                else:
                    l=mid+1
            return r
                        