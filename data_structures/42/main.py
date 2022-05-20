nums = [1, 3, -1, 2, -1, 2]


def maxSubArraySum(nums):
    output = []
    maxSum, runningMax = nums[0], 0
    for num in nums:
        runningMax = max(runningMax + num, num)
        maxSum = max(maxSum, runningMax)
        output += maxSum,

    print(output)

    return output


left_sum = maxSubArraySum(nums)
right_sum = (maxSubArraySum(nums[::-1])[-2::-1])

print(left_sum)
print(right_sum)

for a, b in zip(left_sum, right_sum):
    print(a, b)