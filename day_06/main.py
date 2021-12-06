with open('example_data.txt') as f:
    raw_data = f.readline().split(',')

data = [int(fish) for fish in raw_data]
print(f'Initial state: {data}')

days = 256
for i in range(1, days + 1):
    new_data = []
    for fish in data:
        if fish == 0:
            new_data.append(6)
            new_data.append(8)
        if fish != 0:
            new_data.append(fish-1)
    data = new_data
    print(f'Day - {i}')
fish_counter = 0
for fish in new_data:
    fish_counter += 1

print(f'There are {fish_counter} after {days} days!')
