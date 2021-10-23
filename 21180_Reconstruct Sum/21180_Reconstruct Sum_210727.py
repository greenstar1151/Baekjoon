import sys


n = int(input())
nums = []
for _ in range(n):
    stdin_str = sys.stdin.readline()
    nums.append(int(stdin_str))


target = sum(nums) / 2 
if target in nums: # In Python, 1.0 == 1
    print(target)
else:
    print('BAD')

# for i in range(n):
#     if nums[i] == sum(nums[:i]) + sum(nums[i+1:]):
#         print(nums[i])
#         break
# else:
#     print('BAD')
