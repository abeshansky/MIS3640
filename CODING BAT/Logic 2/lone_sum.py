def lone_sum(a, b, c):
  if a != b and a != c and b != c:
    return a + b + c
  if a != b and a != c and b == c:
    return a
  if a != b and a == c and b != c:
    return b
  if a == b and a != c and b != c:
    return c
  if a == b and a == c and b == c:
    return 0

print(lone_sum(1, 2, 3))