#clean up later
def isValid(self, s: str) -> bool:
  stack = []

  if s.count('(') != s.count(')'): return False
  if s.count('[') != s.count(']'): return False
  if s.count('{') != s.count('}'): return False

  for c in s:
    if c == '(' or c == '{' or c == "[":
      stack.append(c)
    else:
      if not stack: return False
        if c == ')' and stack[-1] != "(":
          return False
        if c == ']' and stack[-1] != "[":
          return False
        if c == '}' and stack[-1] != "{":
          return False
        stack.pop()

  return True
