# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
##
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        digit = 0
        phead = None
        pend = None
        while l1 is not None or l2 is not None:
            a, b = 0, 0
            if l1 is not None: 
                a = l1.val
                l1 = l1.next
            if l2 is not None: 
                b = l2.val
                l2 = l2.next
            tsum = a+b + carry
            carry, digit = tsum // 10, tsum % 10
            tmp = ListNode(digit) 
            if pend is None:
               phead =  pend = ListNode(digit)
            else:
                pend.next = ListNode(digit)
                pend = pend.next
            
        if carry != 0:
            pend.next = ListNode(carry)
            pend = tmp
        if phead is None:
            phead = ListNode(0)
        return phead
##
