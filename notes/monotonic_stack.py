def NGE(self, A):
  stack = []
  res = []

  while A:
    a = A.pop()
            
    while stack and a > stack[-1]:
      stack.pop()

    res.append(-1 if not stack else stack[-1])
    stack.append(a)

  return res[::-1]
