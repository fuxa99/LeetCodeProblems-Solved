from src.help_fun import *

def addTwoNumbers(l1, l2):
    list_nodes = [l1, l2]
    total_number = 0
	
    for i in list_nodes:
        list_node = i
        number = 0
        iteration = 0
        while(True):
            number += list_node.val * (10 ** iteration) 
            if not(list_node.next):
                break
            list_node = list_node.next
            iteration += 1
        total_number += number
    
    total_number = str(total_number)
    ans = ListNode(0)
    for i in range(len(total_number)):
        ans.val = int(total_number[i])
        pom = ans
        if i < len(total_number)-1:
            ans = ListNode(0, pom)
    return ans