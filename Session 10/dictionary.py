names = ['Rose', 'Jerry', 'Alex']
scores = [95, 75, 85]

print(scores[names.index('Jerry')])

grades = {'Jerry': 75, 'Rose:': 95}
print(grades['Jerry'])

grades['Brian'] = 90
print(grades)

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else: d[c] += 1
    return d

h = histogram('Bookkeeper')
print(h)