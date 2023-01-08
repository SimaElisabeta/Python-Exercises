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

print(20 * '-', 'EX 5', 20 * '-')


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
