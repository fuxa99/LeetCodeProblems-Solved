from src.help_fun import *
from src.easy import *
from src.medium import *

print("===== Add Two Numbers - Linked list =====") 
node1 = ListNode(0)
node2 = ListNode(0)
node3 = ListNode(0)
node4 = ListNode(0)
l1 = ListNode(0)
l2 = ListNode(0)
node1.val = 3
node2.val = 4
node2.next = node1
l1.val = 2
l1.next = node2
node3.val = 4
node4.val = 6
node4.next = node3
l2.val = 5
l2.next = node4
ans = addTwoNumbers(l1,l2)
#Data is reserved
print(f"For l1: => " + str(l1.next.next.val)+ str(l1.next.val) + str(l1.val))
print(f"For l2: => " + str(l2.next.next.val)+ str(l2.next.val) + str(l2.val))
print(f"For 342+465: => " + str(ans.next.next.val)+ str(ans.next.val) + str(ans.val))

print("===== Two sum =====")
input = [2,3,5,7,11,15,16,20,30,32,40]
target = [9,47,41,26]
for i in range(len(target)):
  print(f"For target: {target[i]} => " + str(twoSum(input, target[i])))

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

print("===== Longest Common Prefix =====") 
input = ["heaaaa","heh","hey","hello"]
print(f"For input: => " + str(longestCommonPrefix(input)))

