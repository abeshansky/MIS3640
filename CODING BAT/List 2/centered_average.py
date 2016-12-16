def centered_average(nums):
  nums.remove(max(nums))
  nums.remove(min(nums))
  return sum(nums) / len(nums)

print(centered_average([1, 2, 3, 4, 100]))