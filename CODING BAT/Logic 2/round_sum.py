def round_sum(a, b, c):
  def round10(num):
    if num >= 5:
      if num % 10 < 5:
        return num - num % 10
      elif num % 10 >= 5:
        return num + ( 10 - (num % 10))
    else:
      return 0
  return round10(a) + round10(b) + round10(c)

print(round_sum(16, 17, 18))