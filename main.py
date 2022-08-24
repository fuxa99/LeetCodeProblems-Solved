from easy import *

## two sum
print("===== two Sum =====")
nums = [2,3,5,7,11,15,16,20,30,32,40]
target = [9,47,41,26]
for i in range(len(target)):
  print(twoSum(nums, target[i]))

## power of 3
print("===== Power of 3 =====")
nums = [27, 3, 0, 9, 15]
for i in nums:
  print(isPowerOfThree(i))

print("===== Palindrom numbers =====")  
nums = [121, -121, 10]
for i in nums:
  print(isPalindrome(i))