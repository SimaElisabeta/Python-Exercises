####
# 1. Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
list1 = list1[::-1]
print(list1)
list1.reverse()
print(list1)

####
# 2.Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

####
# 3. Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers_square = []
for nr in numbers:
    calc = nr * nr
    numbers_square.append(calc)

print(numbers_square)

####
# 4. Concatenate two lists in the following order
# v1
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i + j)

print(list3)

# v2
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3 = [x + y for x in list1 for y in list2]
print(list3)

####
# 5. Iterate both lists simultaneously
# v1
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

for i in range(len(list1)):
    print(f'{list1[i]} {list2[i]}')

# v2
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2.reverse()

print()
for x, y in zip(list1, list2):
    print(x, y)


####
# 6. Remove empty strings from the list of strings
def remove_empty_str_form_lst(your_list):
    return list(filter(None, your_list))


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(remove_empty_str_form_lst(list1))

####
# 7. Add new item to list after a specified item
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for item in list1[2][2]:
    if item == 6000:
        list1[2][2].append(7000)

print(list1)

####
# 8. Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)


####
# 9. Replace list’s item with new value if found
def replace_item_from_lst(your_list, item_to_replace, item_to_insert):
    if item_to_replace in your_list:
        index = your_list.index(item_to_replace)
        your_list[index] = item_to_insert
    return your_list


list1 = [5, 10, 15, 20, 25, 50, 20]
print(replace_item_from_lst(list1, 20, 200))

print(20 * '-', 'EX 10', 20 * '-')


####
# 10. Remove all occurrences of a specific item from a list.
def remove_number(your_list, number):
    for item in your_list:
        if item == number:
            your_list.remove(number)


list1 = [5, 20, 15, 20, 25, 50, 20]
print(f'List before: {list1}')
remove_number(list1, 20)
print(f'List after: {list1}')

print('The end!')
