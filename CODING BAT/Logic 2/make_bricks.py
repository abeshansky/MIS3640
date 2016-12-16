def make_bricks(small, big, goal):
  if goal > big*5 + small:
    return False
  if goal % 5 > small:
    return False
  else:
    return True

print(make_bricks(3, 1, 8))