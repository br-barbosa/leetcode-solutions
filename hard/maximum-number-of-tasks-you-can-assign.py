"""
Problem: Maximum Number of Tasks You Can Assign
Link: https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign

Approach:
Binary search over the possible number of tasks k that can be completed. For each step, we determine if the best k workers can complete the easiest k tasks, with the assistance of the pills. For the hardest task at hand, preference is given to the best worker, without pill. If not possible, we proceed to a linear search for the weakest worker that can complete the task with a pill.

Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""

from collections import deque

class Solution:
    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        def can_assign(k):
            dq = deque(workers[-k:])
            pills_left = pills
            for i in range(k - 1, -1, -1):
                if dq[-1] >= tasks[i]:
                    dq.pop()
                elif pills_left > 0:
                    for j in range(len(dq)):
                        if dq[j] + strength >= tasks[i]:
                            del dq[j]
                            pills_left -= 1
                            break
                    else:
                        return False
                else:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
