'''
n!
r!(n-r)!
'''

N, M = map(int, input().split())

nums = [0] * (N + 1)

nums[1], nums[2] = 1, 2

for i in range(3, N+1):
    nums[i] = nums[i-1] * i

print(nums[N]//(nums[M]*nums[N-M]))