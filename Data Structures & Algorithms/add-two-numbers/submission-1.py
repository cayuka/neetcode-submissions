# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# linked list []
# [1,2,3], l2 = [4,5,6]

# iteration 1: 
# 1 + 4 = 5
# carry = 0
# result = [5]

# iteration 2: 
# 2 + 5 = 7
# carry = 0
# result = [5, 7]

# iteration 3: 
# 6 + 3 = 9
# carry = 0
# result = [5, 7, 9]
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        curr = result
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0 

            v3 = v1 + v2 + carry
            carry = v3 // 10
            v3 = v3 % 10
            curr.next = ListNode(v3)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next