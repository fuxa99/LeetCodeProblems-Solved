from find_sum_of_two_numbers import twoSum

nums = [2,3,5,7,11,15,16,20,30,32,40]
target = [9,47,41,26]
for i in range(len(target)):
  print(twoSum(nums, target[i]))