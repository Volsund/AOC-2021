with open('data.txt') as f:
    data = f.read()

data_arr = data.split('\n')

# --------------------- First Part --------------------
gamma = ''
epsilon = ''

for x in range(len(data_arr[0])):
    zeros = 0
    ones = 0
    for i in range(len(data_arr)):
        if data_arr[i][x] == '0':
            zeros += 1
        elif data_arr[i][x] == '1':
            ones += 1

    if zeros > ones:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

gamma_dec = int(gamma,2)
epsilon_dec = int(epsilon,2)

print(f'Power consumption is {gamma_dec * epsilon_dec}')


# ----------------------- Second Part -----------------

oxygen_arr = data_arr
for x in range(len(data_arr[0])):
    zeros = 0
    ones = 0
    zero_arr = []
    one_arr = []
    for i in range(len(oxygen_arr)):
        if oxygen_arr[i][x] == '0':
            zeros += 1
            zero_arr.append(oxygen_arr[i])
        elif oxygen_arr[i][x] == '1':
            ones += 1
            one_arr.append(oxygen_arr[i])
    if zeros > ones:
        oxygen_arr = zero_arr
    else:
        oxygen_arr = one_arr
    if len(oxygen_arr) == 1:
        break

oxygen_rating = int(oxygen_arr[0], 2)

scrub_arr = data_arr
for x in range(len(data_arr[0])):
    zeros = 0
    ones = 0
    zero_arr = []
    one_arr = []
    for i in range(len(scrub_arr)):
        if scrub_arr[i][x] == '0':
            zeros += 1
            zero_arr.append(scrub_arr[i])
        elif scrub_arr[i][x] == '1':
            ones += 1
            one_arr.append(scrub_arr[i])
    if ones < zeros:
        scrub_arr = one_arr
    else:
        scrub_arr = zero_arr
    if len(scrub_arr) == 1:
        break

scrub_rating = int(scrub_arr[0], 2)
print(f'Life support rating is {oxygen_rating*scrub_rating}')
