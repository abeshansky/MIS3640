def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n == 13 or n == 14 or n >= 17 and n <= 19:
      return 0
    else:
      return n
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))