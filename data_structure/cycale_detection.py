

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    flag=0
    s=set()
    tmp=head.next
    while tmp: 
        if tmp in s:
            flag=1
            break
        else:
            s.add(tmp)
            tmp=tmp.next
    return flag
