from easy import *

## two sum
print("===== two Sum =====")
input = [2,3,5,7,11,15,16,20,30,32,40]
target = [9,47,41,26]
for i in range(len(target)):
  print(f"For target: {target[i]} => " + str(twoSum(input, target[i])))

## power of 3
print("===== Power of 3 =====")
input = [27, 3, 0, 9, 15]
for i in input:
  print(f"For number: {i} => " + str(isPowerOfThree(i)))

print("===== Palindrom numbers =====")  
input = [121, -121, 10]
for i in input:
  print(f"For number: {i} => " + str(isPalindrome(i)))

print("===== Roman to Integer v1 =====") 
input = ["III","IV","IX","MCMXCIV"]
for i in input:  
  print(f"For number: {i} => " + str(romanToInt(i)))