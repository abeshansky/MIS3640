def caught_speeding(speed, is_birthday):
  bday = 0
  if is_birthday == True:
    bday = 5
  if speed <= 60 + bday:
    return 0
  if speed >= 60+bday and speed <= 80+bday:
    return 1
  if speed >= 81+bday:
    return 2

print(caught_speeding(60, False))