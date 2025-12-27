

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0)
        current = temp
        carry = 0

        while l1 or l2 or carry:
            # Get values from nodes (or 0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values with carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for next step
            new_node = ListNode(total % 10)
            current.next = new_node
            current = current.next

            # Move to next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return temp.next


l1=[2,4,3]
l2=[5,6,4]

s=Solution()
print(s.addTwoNumbers(l1,l2))
