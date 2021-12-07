with open('data.txt') as f:
    data = [int(num) for num in f.readline().split(',')]

# ---------------- Part 1 -------------------------
results = {}
for position in range(min(data), max(data) + 1):
    cost = 0
    for num in data:
        if num > position:
            cost += num - position
        else:
            cost += position - num
    results[position] = cost
    print(f'Total cost position {position} = {cost}')
    cost = 0

print(f'Lowest cost: {min(results.values())}')

results = {}
for position in range(min(data), max(data) + 1):
    cost = 0
    for num in data:
        if num > position:
            difference = num - position
            total = 0
            counter = 0
            for i in range(difference):
                total = total + counter + 1
                counter += 1
            cost += total
        else:
            difference = position - num
            total = 0
            counter = 0
            for i in range(difference):
                total = total + counter + 1
                counter += 1
            cost += total
    results[position] = cost
    print(f'Total cost position {position} = {cost}')
    cost = 0

print(f'Lowest cost: {min(results.values())}')

