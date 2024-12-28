from basic_linked_list import print_linked_list


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node_head = current.next_node
        current.next_node = prev
        prev = current
        current = next_node_head
    return prev


# None -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
# Create individual nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

# Link the nodes together
node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5
node5.next_node = node6

# node1 is the head of the ListNode: 1 -> 2 -> 3 -> 4 -> 5
head_node = node1

result = reverse_linked_list(head_node)
print("Reversed linked list")
print_linked_list(result)

