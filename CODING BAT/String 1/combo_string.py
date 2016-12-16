def combo_string(a, b):
  counta = 0
  for letter in a:
    counta += 1
  countb = 0
  for letter in b:
    countb += 1
  if counta > countb:
    return b + a + b
  elif counta < countb:
    return a + b + a

print(combo_string('Hello', 'hi'))