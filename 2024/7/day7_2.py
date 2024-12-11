def valid_calculation(target, nums):
    if len(nums) == 1: return nums[0] == target
    if valid_calculation(target, [nums[0] + nums[1]] + nums[2:]): return True
    if valid_calculation(target, [nums[0] * nums[1]] + nums[2:]): return True
    if valid_calculation(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:]): return True
    return False

input = open("large.in").read().split("\n")
result = 0
for line in input:
    target, nums = line.split(":")
    target = int(target)
    nums = list(map(int, nums.split()))
    valid = valid_calculation(target, nums)

    if valid:
        result += target

print(result)