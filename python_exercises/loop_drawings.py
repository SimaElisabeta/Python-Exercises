col = 4
count = 0

# Right arrow
while count < 1:
    for i in range(col):
        for j in range(i + 1):
            print('*', end=" ")
        print()
        count += 1
else:
    for i in range(col - 1, 0, -1):
        for j in range(i):
            print('*', end=" ")
        print()
print('The end!')

# Left arrow
count = 0
while count < 1:
    for i in range(col):
        for j in range(col - i - 1):
            print(' ', end=' ')
        for k in range(i + 1):
            print('*', end=' ')
        print()
        count += 1
else:
    for i in range(col - 1, 0, -1):
        for j in range(col - i):
            print(' ', end=' ')
            outer_j = j
        for k in range(i):
            print('*', end=' ')
        print()
print('The end!')

nr_el = 11
magic_number = (nr_el // 2)
x_del = 0

for i in range(magic_number + 1):
    for k in range(magic_number - i, 0, -1):
        print(' ', end=' ')
    for j in range(1 + (2 * i)):
        print('*', end=' ')
    print()
for i in range(magic_number - 1, -1, -1):
    for k in range(magic_number - i, 0, -1):
        print(' ', end=' ')
    for j in range(1 + (2 * i)):
        print('*', end=' ')
    print()
print('The end!')
