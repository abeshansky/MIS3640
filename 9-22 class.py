result = 0
for i in range(1, 11, 2):
    print('current i:', i)
    result += i
print(result)

result = 0
for i in range(11):
    if i%2 ==1:
        print('current i:', i)
        result += i
print(result)

iteration = 0
count = 0
while iteration < 5:
        for letter in "hello, world":
            count += 1
        print("Iteration "+ str(iteration) + "; count is:" + str(count))
        iteration += 1

# while True:
#     line = input('> ')
#     if life == 'done':
#         break
#     print(line)
# print ('Done!')

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Interation " + str(iteration) + "; count is: " + str(count))
    iteration += 1

result = 0
i = 1
while i <= 10:
    if i%2 == 0:
        result = result + i
    i = i + 1
print(result)