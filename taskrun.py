class Solution:
    def solve(self, tasks, k):
        last_times = {}
        cur_time = 0
        for j, task in enumerate(tasks):
            if task in last_times and cur_time - last_times[task] <= k:
                wait_time = k - (cur_time - last_times[task]) + 1
                cur_time += wait_time
            last_times[task] = cur_time
            cur_time += 1
        return cur_time
