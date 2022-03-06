class Solution:
    def solve(self, intervals, point):
        n = 0
        for i in range(len(intervals)):
            if intervals[i][0] <= point <= intervals[i][1]:
                n += 1
        return n
