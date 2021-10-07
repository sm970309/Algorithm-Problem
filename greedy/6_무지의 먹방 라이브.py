from collections import deque
def solution(food_times, k):
    queue = deque(zip(food_times, range(1, len(food_times) + 1)))
    if sum(food_times) <= k:
        return -1
    while k:
        try:
            q = queue.popleft()
            if q[0] - 1 != 0:
                queue.append((q[0] - 1, q[1]))
            k -= 1
        except:
            return -1

    return queue[0][1]