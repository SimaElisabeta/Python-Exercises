####
# 1. Print First 10 natural numbers using while loop
# v1
for i in range(1, 11):
    print(i)

# v2
i = 1
while i <= 10:
    print(i)
    i += 1

####
# 2. Print the following pattern
for i in range(5):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

####
# 3. Calculate the sum of all numbers from 1 to a given number
user_input = 10
the_sum = 0

for i in range(user_input):
    the_sum += i + 1

print(the_sum)


####
# 4. Write a program to print multiplication table of a given number
def multiplications_of(number):
    for n in range(10):
        print((n + 1) * number)


multiplications_of(2)


####
# 5. Display numbers from a list using loop
def display_numbers(lst):
    for nr in lst:
        if nr > 500:
            break
        elif nr % 5 == 0:
            if nr > 150:
                continue
            else:
                print(nr)


numbers = [12, 75, 150, 180, 145, 525, 50]
display_numbers(numbers)


####
# 6. Count the total number of digits in a number
def count_total_digits(numers):
    counter = 0
    while numers != 0:
        numers //= 10
        counter += 1
    print(counter)


count_total_digits(75869)

####
# 7. Print the following pattern
# v1
row = 5
col = row

for i in range(row):
    for j in range(col, 0, -1):
        print(j, end=" ")
    col -= 1
    print()

print()
# v2
row = 5
col = 5
for i in range(0, row + 1):
    for j in range(col - i, 0, -1):
        print(j, end=' ')
    print()


####
# 8. Print list in reverse order using a loop
# v1
def reverse_list_print(lst):
    for item in range(len(lst) - 1, -1, -1):
        print(lst[item])


# v2
def reverse_list_print_2(lst):
    lst.reverse()
    for item in lst:
        print(item)


lst = [10, 20, 30, 40, 50]

reverse_list_print(lst)
print()
reverse_list_print_2(lst)

####
# 9. Display numbers from -10 to -1 using for loop

for i in range(-10, 0, 1):
    print(i)

####
# 10. Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print('Done!')


####
# 11. Write a program to display all prime numbers within a range
def prime_numbers(start, end):
    print(f'Prime numbers between {start} and {end} are:')
    for nr in range(start, end + 1):
        if nr >= 1:
            for i in range(2, nr):
                if (nr % i) == 0:
                    break
            else:
                print(nr)


start = 25
end = 50

prime_numbers(start, end)

####
# 12. Display Fibonacci series up to 10 terms
num1 = 0
num2 = 1

for i in range(10):
    print(num1, end=' ')
    calc = num1 + num2
    num1 = num2
    num2 = calc

print()


####
# 13. Find the factorial of a given number
def factorial_number(number):
    if number < 0:
        return 'Factorial does not exist for negative numbers'
    elif number == 0:
        return 0
    result = 1
    for i in range(number, 0, -1):
        result *= i
    return result


print(factorial_number(4))

####
# 14. Reverse a given integer number
num = 76542
reverse_number = 0
print("Given Number:", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Reverse Number:", reverse_number)


####
# 15. Use a loop to display elements from a given list present at odd index positions
# v1
def display_numbers_at_odd_index(lst):
    for i in range(1, len(lst) + 1, 2):
        print(lst[i], end=' ')


# v2
def display_numbers_at_odd_index_v2(lst):
    for i in lst[1::2]:
        print(i, end=' ')


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
display_numbers_at_odd_index(my_list)
print()
display_numbers_at_odd_index_v2(my_list)

####
# 16. Calculate the cube of all numbers from 1 to a given number
input_number = 6

for i in range(1, input_number + 1):
    print(f'Current Number is : {i}  and the cube is {i ** 3}')

####
# 17. Find the sum of the series upto n terms
n = 5
start = 2
total = 0

for i in range(0, n):
    total += start
    start = start * 10 + 2

print(total)

print(20 * '-', 'EX 18', 20 * '-')
####
# 18. Print the following pattern
first_row = 5
second_row = 4

for i in range(first_row):
    for j in range(i + 1):
        print('*', end=' ')
    print()
for i in range(second_row, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

print('The end!')
