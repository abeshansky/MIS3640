def near_ten(num):
  if num % 10 == 8 or num % 10 == 9 or num % 10 == 0 or num % 10 == 1 or num % 10 == 2: 
    return True
  else:
    return False

print(near_ten(12))