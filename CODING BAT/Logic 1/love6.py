def love6(a, b):
  if a == 6:
    return True
  if b == 6:
    return True
  if a + b == 6: 
    return True
  if abs(a - b) == 6:
    return True
  else:
    return False

print(love6(6, 4))