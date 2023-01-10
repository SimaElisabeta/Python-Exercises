import string

####
# 1a. Create a string made of the first, middle and last character
str1 = "James"
middle_char = len(str1) // 2
print(str1[0] + str1[middle_char] + str1[-1])


# 1b. Create a string made of the middle three characters
def middle_3_char(my_string):
    middle = len(my_string) // 2
    print(my_string[middle - 1:middle + 2])


str1 = "JhonDipPeta"
str2 = "JaSonAy"
middle_3_char(str1)
middle_3_char(str2)

####
# 2. Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
s1_middle = len(s1) // 2
s3 = s1[:s1_middle] + s2 + s1[s1_middle:]
print(s3)

####
# 3. Create a new string made of the first, middle, and last characters of each input string
# s1 and s2’s first, middle, and last characters.
s1 = "America"
s2 = "Japan"
s1_m = len(s1) // 2
s2_m = len(s2) // 2

s3 = s1[0] + s2[0] + s1[s1_m] + s2[s2_m:]
print(s3)

####
# 4. Arrange string characters such that lowercase letters should come first
str1 = 'PYnAtivE'
lower_char = ''
upper_char = ''
for char in str1:
    if char == char.lower():
        lower_char += char
    else:
        upper_char += char

print(lower_char + upper_char)


####
# 5. Count all letters, digits, and special symbols from a given string
def count_chars_digits_symbols(my_string):
    chars_count = 0
    digits_count = 0
    symbols_count = 0
    for char in my_string:
        if char.isalpha():
            chars_count += 1
        elif char.isdigit():
            digits_count += 1
        else:
            symbols_count += 1

    print(f'Chars = {chars_count} ')
    print(f'Digits = {digits_count} ')
    print(f'Symbol = {symbols_count} ')


str1 = "P@#yn26at^&i5ve"
count_chars_digits_symbols(str1)

####
# 6. Create a mixed String using the following rules
# v1
s1 = "Abc"
s2 = "Xyz"

first_last = s1[0] + s2[-1]
middle = s1[1:-1] + s2[1:-1]
last_first = s1[-1] + s2[0]

s3 = first_last + middle + last_first
print(s3)
print()

# v2
s1 = "Ab@c"
s2 = "Xy#z"

s1_length = len(s1)
s2_length = len(s2)

length = s1_length if s1_length > s2_length else s2_length
result = ""

s2 = s2[::-1]

for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)


####
# 7. String characters balance Test
def is_subset(str_a, str_b):
    result = True
    for char in str_a:
        if char in str_b:
            continue
        else:
            result = False
    return result


s1 = "Yn"
s2 = "PYnative"
print(is_subset(s1, s2))


####
# 8. Find all occurrences of a substring in a given string by ignoring the case
def count_occurrences(your_str, your_chars):
    new_str = your_str.lower()
    new_chars = your_chars.lower()
    return new_str.count(new_chars)


str1 = "Welcome to USA. usa awesome, isn't it?"
print(count_occurrences(str1, 'Usa'))


####
# 9. Calculate the sum and average of the digits present in a string
def calc_sum_average_of_digits_in_str(your_str):
    the_sum = 0
    digit_count = 0
    for char in your_str:
        if char.isdigit():
            the_sum += int(char)
            digit_count += 1
    return f'Sum is: {the_sum} \nAverage is: {the_sum / digit_count}'


str1 = "PYnative29@#8496"
print(calc_sum_average_of_digits_in_str(str1))


####
# 10. Write a program to count occurrences of all characters within a string
def get_chars_count(your_srt):
    char_dict = dict()
    for char in your_srt:
        count = your_srt.count(char)
        char_dict[char] = count

    return char_dict


str1 = "Appels"
print(get_chars_count(str1))
print()

####
# 11. Reverse a given string

# v1
str1 = "PYnative"
str1 = str1[::-1]
print(str1)

# v2
str1 = "PYnative"
str1 = ''.join(reversed(str1))
print(str1)

####
# 12. Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
find_index = str1.rfind('Emma')
print(find_index)

####
# 13. Split a string on hyphens

str1 = 'Emma-is-a-data-scientist'
str_split = str1.split('-')
for item in str_split:
    print(item)


####
# 14. Remove empty strings from a list of strings
# v1
def remove_empty_in_list(your_list):
    new_list = []
    for item in your_list:
        if item:
            new_list.append(item)
    return new_list


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
print(remove_empty_in_list(str_list))

# v2
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str_list = list(filter(None, str_list))
print(new_str_list)

####
# 15. Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print(new_str)


####
# 16. Removal all characters from a string except integers
def get_only_integer(your_str):
    output = ''
    for char in your_str:
        if char.isdigit():
            output += char
    return output


str1 = 'I am 25 years and 10 months old'
print(get_only_integer(str1))


####
# 17. Find words with both alphabets and numbers
def get_alph_num(your_str):
    output = []
    string_split = your_str.split()
    for item in string_split:
        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            output.append(item)
    for i in output:
        print(i)


str1 = "Emma25 is Data scientist50 and AI Expert"
get_alph_num(str1)

print(20 * '-', 'EX 18', 20 * '-')


####
# 18. Replace each special symbol with # in the following string
def replace_symbols_in_str(your_str, new_symbol):
    for char in your_str:
        if char.isdigit() or char.isalpha():
            pass
        elif char == ' ':
            pass
        else:
            your_str = your_str.replace(char, new_symbol)
    return your_str


str1 = '/*Jon is @developer & musician!!'
print(str1)
print(replace_symbols_in_str(str1, '#'))

print('The end!')
