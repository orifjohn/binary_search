class Solution:
    def solve(self, typed, target):
        def get_run_length_encoded(s):
            ans = []
            for a, b in groupby(s):
                ans.append((a, len(list(b))))
            return ans

        z1 = get_run_length_encoded(typed)
        z2 = get_run_length_encoded(target)

        if len(z1) != len(z2):
            return False

        return all(a == b and l1 >= l2 for (a, l1), (b, l2) in zip(z1, z2))

