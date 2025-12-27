# Create linked list from list helper function
def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Print linked list helper function
def print_linked_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

# Define ListNode
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution class as above
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

# Example usage:
l1 = create_linked_list([2,4,3])  # Represents 342
l2 = create_linked_list([5,6,4])  # Represents 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)  # Outputs: [7, 0, 8]

