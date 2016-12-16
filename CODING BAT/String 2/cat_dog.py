def cat_dog(str):
  if str.count('cat') == str.count('dog'):
    return True
  else:
    return False

print(cat_dog('catdog'))