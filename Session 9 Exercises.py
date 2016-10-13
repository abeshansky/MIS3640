#Exercise 1
#2
# def has_no_e(word):
#     for letter in word:
#         if 'e' in word:
#             return False
#         return True

# print(has_no_e('fish'))
# print(has_no_e('white'))
# print(has_no_e('novel'))

# def has_no_e(word):
#     for letter in word:
#         if 'e' in word:
#             return False
#         return True

# def has_no_e(word):
#     count = 0
#     for letter in word:
#         if 'e' in word:
#             count =+ 1
#     percentage = count / count(word)
# print(has_no_e('fish'))
# print(has_no_e('white'))
# print(has_no_e('novel'))

# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         if c < previous:
#             return False
#         previous = c
#     return True
# print(is_abecedarian('abcde'))
# print(is_abecedarian('peanut'))

# def three_consec_doubles():
#     for letter in word:
#         i = 0
#         pairCount = 0
#         while i < len(word) - 1:
#             if letter[i] == letter[i + 1]:
#                 pairCount += 1
#                 if pairCount == 3:
#                     print word
#                 i += 2
#             else:
#                 pairCount = 0
#                 i += 1