def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  carry = False
  tmp = ListNode(0)
  tail = tmp

  while l1 or l2:
      s = carry
      if l1: 
          s += l1.val
          l1 = l1.next
      if l2:
          s += l2.val
          l2 = l2.next

      if s > 9:
          carry = True
      else:
          carry = False

      tail.next = ListNode(s % 10)
      tail = tail.next

  if carry:
      tail.next = ListNode(1)
      tail = tail.next

  return tmp.next
