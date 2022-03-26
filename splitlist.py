class Solution:
    def solve(self, x):
        l=len(x)
        p=[0 for i in range(l)]
        p[-1]=x[-1]
        for i in range(l-2,-1,-1):
            p[i]=min(p[i+1],x[i])
        ma=x[0]
        for i in range(1,l):
            if ma<p[i]:
                return True
            ma=max(ma,x[i])
        return False