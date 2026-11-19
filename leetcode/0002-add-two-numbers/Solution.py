class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1 = self.listToNum(l1)
        num2 = self.listToNum(l2)
        total = num1 + num2
        return self.numToList(total)

    def listToNum(self, node: ListNode | None) -> int:
        num = 0
        multiplier = 1
        
        while node:
            num += node.val * multiplier
            multiplier *= 10
            node = node.next
            
        return num

    def numToList(self, num: int) -> ListNode | None:
        if num == 0:
            return ListNode(0)

        temp = ListNode(0)
        current = temp

        while num > 0:
            current.next = ListNode(num % 10)
            current = current.next
            num //= 10

        return temp.next
