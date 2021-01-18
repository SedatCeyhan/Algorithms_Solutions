import collections

# https://leetcode.com/discuss/interview-question/393226/akuna-capital-oa-2019-quant
def hashedPorts(n, T, packet_id):
    ans, t = [], 1
    avail = [0] * n
    queue = collections.deque()
    for pid in packet_id:
        # pop from queue if the port is available
        while queue and avail[queue[0]] <= t:
            queue.popleft()
        # if no ports available, wait until there is one available
        if len(queue) == n:
            t = avail[queue.popleft()]
        # try port until find one available
        port = pid % n
        while avail[port] > t:
            port = (port + 1) % n
        # send packet, update available time for the port
        avail[port] = t + T
        queue.append(port)
        ans.append(port)
        t += 1
    return ans


print('Q1')
n = 5
T = 10
packid = [1, 2, 3, 4, 5, 6]
print(hashedPorts(n, T, packid))

n = 5
T = 2
packid = [5, 1, 6, 2, 7, 3]
print(hashedPorts(n, T, packid))

n = 5
T = 10
packid = [1, 1, 1, 6, 2, 2]
print(hashedPorts(n, T, packid))
print(' ')



from heapq import heappush, heappop


def turnstile(times, direction):
    n = len(times)
    if n == 0: return []
    pq, ans = [], [-1] * n
    for t, d, i in zip(times, direction, range(n)):
        heappush(pq, (t, d, i))
    T, state = 0, None
    while pq:
        # get next person
        t, d, i = heappop(pq)
        # if not used in previous second, state is None
        if t - 1 > T: state = None
        # update current time
        T = max(T, t)
        # if there are multiple people waiting
        # split them by direction and store
        cand = [[], []]
        cand[d].append((t, d, i))
        while pq and pq[0][0] <= T:
            tt, dd, ii = heappop(pq)
            cand[dd].append((tt, dd, ii))
        # judge direction
        if not cand[0]:
            D = 1
        elif not cand[1]:
            D = 0
        else:
            D = int(state in [None, 1])
        # deal with the group that goes first
        for tt, dd, ii in cand[D]:
            ans[ii], T, state = T, T + 1, D
        # push the group that goes after back
        for tt, dd, ii in cand[1 - D]:
            heappush(pq, (tt, dd, ii))
    return ans


print('Q3')

times = [0, 0, 1, 5]
direction = [0, 1, 1, 0]
print(turnstile(times, direction))


times = [0, 0, 0, 0, 1, 1, 3]
direction = [0, 0, 1, 1, 1, 0, 1]
print(turnstile(times, direction))


times = [0, 0, 0, 0, 1, 1, 4]
direction = [0, 0, 1, 1, 1, 0, 1]
print(turnstile(times, direction))