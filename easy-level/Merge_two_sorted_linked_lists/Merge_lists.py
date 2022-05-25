sys.setrecursionlimit(10000)

def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    if head1.data <= head2.data:
        head1.next = mergeLists(head1.next, head2)
        return head1
    head2.next = mergeLists(head1, head2.next)
    return head2


if __name__ == '__main__':
    #number of tests
    tests = int(input())

    for tests_itr in range(tests):
        
        list_count = int(input())
        list1 = SinglyLinkedList()

        for i in range(list_count):
            list1_item = int(input())
            list1.insert_node(list1_item)

        list2_count = int(input()) 

        for j in range(list2_count):
            list2_item = int(input())
            list2.insert_node(list2_item)

        list3 = mergeLists(list1.head, list2.head)

    print(list3)


