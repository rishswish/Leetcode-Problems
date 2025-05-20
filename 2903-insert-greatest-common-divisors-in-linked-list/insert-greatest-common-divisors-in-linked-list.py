# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while(b):
                a, b = b, a % b
            return a
        
        curr=head
        while curr and curr.next:
            gc=math.gcd(curr.val,curr.next.val)
            node=ListNode(gc)
            node.next=curr.next
            curr.next=node
            curr=curr.next.next

        return head
        