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
