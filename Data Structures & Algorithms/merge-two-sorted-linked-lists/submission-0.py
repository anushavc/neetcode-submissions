# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating the dummy node first
        dummy=ListNode()
        tail=dummy
        while list1 and list2:
            #compare list 1 val with list 2 val
            if list1.val<list2.val:
                #tail.next (basically dummy node tail points to the list 1 node)
                tail.next=list1
                #we move the list 1 node to the next one
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        #rest of the nodes
        tail.next=list1 or list2
        return dummy.next