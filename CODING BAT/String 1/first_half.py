def first_half(str):
  count = 0
  for a in str:
    count += 1
  return str[0:count/2]

print(first_half('HelloThere'))