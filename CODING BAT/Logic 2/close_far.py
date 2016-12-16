def close_far(a, b, c):
  if abs(b-a) <= 1:
    close = b
  if abs(c-a) <= 1:
    close = c
  if close == b and abs(c-a) >= 2 and abs(c-b) >= 2:
    return True
  if close == c and abs(b-a) >= 2 and abs(c-b) >= 2:
    return True
  else:
    return False

print(close_far(1, 2, 10))