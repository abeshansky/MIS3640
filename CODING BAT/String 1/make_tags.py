def make_tags(tag, word):
  c = "<" + tag + ">"
  d = "<" + "/" + tag + ">"
  return c + word + d

print(make_tags('i', 'Yay'))