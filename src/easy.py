def twoSum(nums, target):
  for i in range(len(nums)):
    if (target - nums[i]) in nums: 
      if i != nums.index(target - nums[i]):
        return [i, nums.index(target - nums[i])]

def isPowerOfThree(n: int) -> bool:
  if n <= 0:
    return False
  num = n
  while (num % 3) == 0:
    num = num / 3
  if int(num) == 1:
    return True
  else:
    return False

def isPalindrome( x: int) -> bool: 
  return str(x) == str(x)[::-1]

def romanToInt(s: str) -> int:
  symbols = ["I", 1,"V", 5,"X", 10,"L", 50,"C", 100,"D", 500,"M", 1000]
  paired = ["IV", 4, "IX", 9,"XL", 40,"XC", 90,"CD", 400,"CM", 900]
  value = 0
  check_paired_index = 0
  for i in range(len(s)):
    if check_paired_index <= i:
      if i+1 < len(s):
        if s[i]+s[i+1] in paired:
          value += paired[paired.index(s[i]+s[i+1]) + 1]
          check_paired_index = i + 2
        else:
          value += symbols[symbols.index(s[i]) + 1]
      else:
        value += symbols[symbols.index(s[i]) + 1]
  return(value)

def longestCommonPrefix(strs: list) -> str:
  if strs[0] == "":
    return ""
  if len(strs) < 2:
    return strs[0]
  run = True
  pref_len = 0
  result = min(strs, key=len)
  for i in range(len(result)):
    for j in range(len(strs)-1):
      if strs[0][i] != strs[j+1][i]:
        run = False
    if run:
      pref_len += 1
  return strs[0][:pref_len]