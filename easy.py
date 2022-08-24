def twoSum(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
  for i in range(len(nums)):
    if (target - nums[i]) in nums: 
      if i != nums.index(target - nums[i]):
        return [i, nums.index(target - nums[i])]

def isPowerOfThree(n: int) -> bool:
  """
  :type n: int
  :rtype: bool
  """
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