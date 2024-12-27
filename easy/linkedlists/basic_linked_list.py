class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next_node else "\n")
        node = node.next_node


def linked_list_to_list(node):
    list_ = []
    while node:
        list_.append(node.val)
        node = node.next_node
    return list_


def direct_linked_list():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    # print(node1.val)
    # print(node2.val)
    # print(node3.val)

    node1.next_node = node2
    node2.next_node = node3

    # current = node1
    # while current:
    #     print(current.val)
    #     current = current.next_node
    print_linked_list(node1)
    print(linked_list_to_list(node1))


def list_to_linked_list(list_):
    head = ListNode(list_[0])
    current = head
    for num in list_[1:]:
        current.next_node = ListNode(num)
        current = current.next_node

    return head


direct_linked_list()
print()
list_to_convert = [1, 3, 5, 7, 9]
converted_list = list_to_linked_list(list_to_convert)
# head_ = converted_list
# while head_:
#     print(head_.val, end=" -> " if head_.next_node else "\n")
#     head_ = head_.next_node
print_linked_list(converted_list)
