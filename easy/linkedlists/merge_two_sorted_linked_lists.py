"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

from basic_linked_list import list_to_linked_list


class LinkedList:

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def merge_two_linked_lists(list1: LinkedList, list2: LinkedList):
    dummy = LinkedList(-1)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next_node = list1
            list1 = list1.next_node
        else:
            current.next_node = list2
            list2 = list2.next_node
        current = current.next_node

    if list1:
        current.next_node = list1
    elif list2:
        current.next_node = list2

    return dummy.next_node


node1 = LinkedList(1)
node2 = LinkedList(3)
node3 = LinkedList(5)
node4 = LinkedList(7)
node5 = LinkedList(9)

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5

llist1 = node1
# while llist1:
#     print(llist1.val)
#     llist1 = llist1.next_node

print()

node6 = LinkedList(2)
node7 = LinkedList(4)
node8 = LinkedList(6)
node9 = LinkedList(8)

node6.next_node = node7
node7.next_node = node8
node8.next_node = node9

llist2 = node6
# while llist2:
#     print(llist2.val)
#     llist2 = llist2.next_node

print()
# merged_node = merge_two_linked_lists(llist1, llist2)
# while merged_node:
#     print(merged_node.val, end=" -> " if merged_node.next_node else "\n")
#     merged_node = merged_node.next_node

"""input from list"""
list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 6, 8]
merged_node = merge_two_linked_lists(list_to_linked_list(list_1), list_to_linked_list(list_2))
print("Merged linked list")
while merged_node:
    print(merged_node.val, end=" -> " if merged_node.next_node else "\n")
    merged_node = merged_node.next_node
