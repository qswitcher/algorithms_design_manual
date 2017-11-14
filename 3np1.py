import sys
import time


results = {}
def compute(n):
    n_start = n
    if results.get(n_start, 0) > 0:
        return results[n_start]
    cycle = []
    while n != 1:
        cycle.append(n)
        if n % 2 == 1:
            n = 3*n + 1
        else:
            n = n/2
    cycle.append(1)
    for i in range(len(cycle)):
        results[cycle[i]] = len(cycle) - i
    return len(cycle)

start = time.time()
for line in sys.stdin:
    pair = [int(x) for x in line.split()]
    left = min(pair[0], pair[1])
    right = max(pair[0], pair[1])
    max_cycle = 1
    for n in range(left, right+1):
        max_cycle = max(max_cycle, compute(n))
    print(pair[0], pair[1], max_cycle)
end = time.time()
elapsed_seconds = float("%.2f" % (end - start))
print('elapsed=', elapsed_seconds)
