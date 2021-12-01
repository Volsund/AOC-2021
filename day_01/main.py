with open('nums.txt') as f:
    data = f.read()
    
nums = data.split()

x = 1
times_larger = 0
for i in range(len(nums)-1):
    if int(nums[x]) > int(nums[x-1]):
        times_larger+=1
    x+=1

print(f'Larger than previous: {times_larger}')