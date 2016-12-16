def make_chocolate(small, big, goal):
    big = big * 5
    if big + small < goal or small < goal % 5:
        return -1
    small = goal - big
    if small < 0:
      return small % 5
    else:
      return small 

print(make_chocolate(4, 1, 9))