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
