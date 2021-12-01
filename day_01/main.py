with open('nums.txt') as f:
    data = f.read()
    
nums = [int(num) for num in data.split()]

x = 1
times_larger = 0
for i in range(len(nums)-1):
    if int(nums[x]) > int(nums[x-1]):
        times_larger+=1
    x+=1

print(f'Measurement larger than previous: {times_larger}')

finished = False
counter = 0
sum_larger = 0
while not finished:
    if counter + 3 < len(nums):
        first_sum = nums[counter] + nums[counter+1] + nums[counter+2]
        second_sum = nums[counter + 1] + nums[counter+ 2] + nums[counter+3]
        if second_sum > first_sum:
            sum_larger+=1
        counter+=1
    else:
        finished = True

print(f'Sum of measurements in sliding window increases {sum_larger} times.')

