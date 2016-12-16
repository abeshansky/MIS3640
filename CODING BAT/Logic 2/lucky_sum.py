def lucky_sum(a, b, c):
  if a == 13:
    return 0
  if b == 13:
    return a
  if c == 13:
    return a + b
  else:
    return a + b + c

print(lucky_sum(1, 2 , 3))