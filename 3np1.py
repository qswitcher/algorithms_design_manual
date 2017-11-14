import sys

results = {}
for line in sys.stdin:
    pair = [int(x) for x in line.split()]
    max_cycle = 1
    for n in range(pair[0], pair[1]+1):
        n_start = n
        if results.get(n_start, 0) > 0:
            max_cycle = max(max_cycle, results[n_start])
            continue
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
        max_cycle = max(max_cycle, len(cycle))
    print(pair[0], pair[1], max_cycle)
            