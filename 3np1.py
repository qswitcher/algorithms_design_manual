import sys
import time


results = {}
def collatz(n):
    n_start = n
    if results.get(n_start, 0) > 0:
        return results[n_start]
    
    answer = 1
    if n == 1:
        answer = 1
    elif n % 2 == 1:
        answer = collatz(3*n + 1) + 1
    else:
        answer = collatz(n/2) + 1
    results[n_start] = answer
    return answer

start = time.time()
for line in sys.stdin:
    pair = [int(x) for x in line.split()]
    left = min(pair[0], pair[1])
    right = max(pair[0], pair[1])
    max_cycle = 1
    for n in range(left, right+1):
        max_cycle = max(max_cycle, collatz(n))
    print(pair[0], pair[1], max_cycle)
end = time.time()
elapsed_seconds = float("%.2f" % (end - start))
print('elapsed=', elapsed_seconds)
