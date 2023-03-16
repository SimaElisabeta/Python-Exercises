####
# 1. Create a function in Python
def print_values(name, age):
    print(f'Name is: {name}')
    print(f'Age is: {age}')


print_values('Alex', 30)


####
# 2. Create a function with variable length of arguments
def func_variable(*args):
    print('Printing values:')
    for arg in args:
        print(arg)


func_variable(10, 50, 100)
func_variable(10, 100)


####
# 3. Return multiple values from a function
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


res = calculate(40, 10)
print(res)

add, sub = calculate(40, 10)
print(add, sub)


####
# 4. Create a function with a default argument

def show_employee(name='', salary=9000):
    print(f'Name: {name}, salary: {salary}')


show_employee('Ben', 12000)
show_employee('Jessa')


####
# 5. Create an inner function to calculate the addition in the following way

def calc_addition(a, b):
    def addition():
        return a + b

    return 5 + addition()


print(calc_addition(5, 10))


####
# 6. Create a recursive function
def recursive_addition(number):
    if number:
        return number + recursive_addition(number - 1)
    else:
        return 0


output = recursive_addition(10)
print(output)


####
# 7. Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)


display_student("Emma", 26)
show_student = display_student
show_student("Emma", 26)


####
# 8. Generate a Python list of all the even numbers between 4 to 30
def get_even_numbers(from_n, to_n):
    new_list = []
    for i in range(from_n, to_n):
        if i % 2 == 0:
            new_list.append(i)
    return new_list


print(get_even_numbers(4, 30))

print(20 * '-', 'EX 9', 20 * '-')
####
# 9. Find the largest item from a given list
# v1
x = [4, 6, 8, 24, 12, 2]
print(max(x))


# v2
def max_number(lst):
    maximum = lst[0]
    for i in lst:
        if i > maximum:
            maximum = i
    return maximum


print(max_number(x))
print('The end!')
