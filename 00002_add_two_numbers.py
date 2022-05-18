# My solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        # List out digits from ListNode
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
            
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # Cast list to string        
        string1 = ''.join([str(i) for i in list1])  # l1: 243
        string2 = ''.join([str(i) for i in list2])  # l2: 564
        
        # Reverse the string and cast to num
        num1 = int(string1[::-1])  # 342
        num2 = int(string2[::-1])  # 465
        
        # Add two numbers and cast to int digits reversed
        result_list = [int(i) for i in str(num1 + num2)[::-1]]  # 708
        
        # Result node is Keep popping the result_list from right
        result_node = None
        while True:
            if len(result_list) == 0:
                break
            val = result_list.pop()
            result_node = ListNode(val, result_node)

        return result_node

  
# Leetcode solution
# Algorithm
# Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1l1 and l2l2. Since each digit is in the range of 0 \ldots 90…9, summing two digits may "overflow". For example 5 + 7 = 125+7=12. In this case, we set the current digit to 22 and bring over the carry = 1carry=1 to the next iteration. carrycarry must be either 00 or 11 because the largest possible sum of two digits (including the carry) is 9 + 9 + 1 = 199+9+1=19.
#
# public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
#     ListNode dummyHead = new ListNode(0);
#     ListNode p = l1, q = l2, curr = dummyHead;
#     int carry = 0;
#     while (p != null || q != null) {
#         int x = (p != null) ? p.val : 0;
#         int y = (q != null) ? q.val : 0;
#         int sum = carry + x + y;
#         carry = sum / 10;
#         curr.next = new ListNode(sum % 10);
#         curr = curr.next;
#         if (p != null) p = p.next;
#         if (q != null) q = q.next;
#     }
#     if (carry > 0) {
#         curr.next = new ListNode(carry);
#     }
#     return dummyHead.next;
# }



# 2. Add Two Numbers
# Medium

# 18299

# 3752

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.