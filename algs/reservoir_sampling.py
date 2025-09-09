class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        i = 2
        node = self.head.next

        while node:
            if random.random() < (1 / i):
                res = node.val
            node = node.next
            i += 1

        return res
