####
# 1. Calculate the multiplication and sum of two numbers.
def calc_multiplication_sum(n1, n2):
    multiplication = n1 * n2
    if multiplication <= 1000:
        return multiplication
    return n1 + n2


print(f"The result is {calc_multiplication_sum(20, 30)}")
print(f"The result is {calc_multiplication_sum(40, 30)}")

####
# 2. Print the sum of the current number and the previous number.
# v1
for nr in range(10):
    print(f"Current Number {nr}, Previous Number {0 if nr == 0 else nr - 1}, Sum: {0 if nr == 0 else nr + nr - 1}")

# v2
for nr in range(10):
    previous_nr = 0 if nr == 0 else nr - 1
    print(f"Current Number {nr}, Previous Number {previous_nr}  Sum: {nr + previous_nr}")

####
# 3. Print characters from a string that are present at an even index number
user_input = 'pynativex'  # input('Enter your word here: ')
print(f'Original String is {user_input}')
print('Printing only even index chars')

# v1
for i in range(0, len(user_input), 2):
    print(f'current index even nr: {i} = {user_input[i]}')

# v2
for i in range(len(user_input)):
    if i % 2 == 0:
        print(f'current index even nr: {i} = {user_input[i]}')


####
# 4. Remove first n characters from a string
def remove_chars(your_string, chars_nr):
    output = your_string[chars_nr:]
    return output


print(remove_chars('pynative', 4))
print(remove_chars('pynative', 2))


####
# 5. Check if the first and last number of a list is the same
def check_first_last_equality(my_list):
    return my_list[0] == my_list[-1]


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(check_first_last_equality(numbers_y))


####
# 6. Display numbers divisible by 5 from a list
# v1
def get_nr_divisible_by_5(my_list):
    output = []
    for nr in my_list:
        if nr % 5 == 0:
            output.append(nr)
    return output


given_list = [10, 20, 33, 46, 55]
print(get_nr_divisible_by_5(given_list))

# v2
for nr in given_list:
    if nr % 5 == 0:
        print(nr)

####
# 7. Return the count of a given substring from a string
str_x = "Emma is good developer. Emma is a writer"
print(f'Emma appeard {str_x.count("Emma")} times')

####
# 8. Print the following pattern
# v1
for nr in range(1, 6):
    for j in range(nr):
        print(nr, end=' ')
    print()

# v2
print()
for nr in range(1, 6):
    print(f"{nr} " * nr)


####
# 9. Check Palindrome Number
def check_palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


check_palindrome(121)
check_palindrome(125)


####
# 10. Create a new list from a two list using the following condition
def get_marge_odd_even(list1, list2):
    output = []
    for number in list1:
        if (number % 2) != 0:  # odd
            output.append(number)

    for number in list2:
        if (number % 2) == 0:  # even
            output.append(number)

    return output


l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]
print(get_marge_odd_even(l1, l2))


####
# 11. Write a Program to extract each digit from an integer in the reverse order.
def reverse_digit(number):
    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end=' ')


reverse_digit(7536)
print()


####
# 12. Calculate income tax for the given income by adhering to the below rules
def get_taxable_income(income):
    if income <= 10000:
        total_tax = 0
    elif income <= 20000:
        x = income - 10000
        total_tax = (x * 0.1)
    else:
        first_i = 10000
        next_i = 10000
        remaining_i = income - first_i - next_i
        total_tax = (first_i * 0) + (next_i * 0.1) + (remaining_i * 0.2)
    return total_tax


print(f'${get_taxable_income(45000)}')


####
# 13. Print multiplication table form 1 to 10
def get_multiplication_table():
    for i in range(10):
        for j in range(10):
            output = (i + 1) * (j + 1)
            print(f"{output:<3}", end=' ')
        print()


get_multiplication_table()

####
# 14. Print downward Half-Pyramid Pattern with Star

row = 5
col = row

for r in range(row):
    for c in range(col):
        print('*', end=' ')
    print()
    col -= 1


####
# 15. Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# v1
def exponent(base, exp):
    return base ** exp


# v2
def exponent_v2(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num -= 1
    return result


print(20 * '-', 'EX 15', 20 * '-')
print(exponent(2, 5))
print(exponent(5, 4))

print(exponent_v2(2, 5))
print(exponent_v2(5, 4))

print('The end!')
