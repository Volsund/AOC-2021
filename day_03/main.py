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


