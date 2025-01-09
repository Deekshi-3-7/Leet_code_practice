"""
83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the
linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""


from basic_linked_list import print_linked_list


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def remove_duplicate(head):
    current = head
    while current and current.next_node:
        if current.val == current.next_node.val:
            current.next_node = current.next_node.next_node
        else:
            current = current.next_node
    return head


node6 = ListNode(5)
node5 = ListNode(3, node6)
node4 = ListNode(2, node5)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print("\nLinked lists after removing duplicates")
result = remove_duplicate(node1)
print_linked_list(result)
