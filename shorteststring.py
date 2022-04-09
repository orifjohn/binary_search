class Solution:
	def solve(self, s):
		return abs(len(s) - 2 * s.count("1"))