####
# 1. Create a list by picking an odd-index items from the first list and even index items from the second
def odd_even_list_packing(list1, list2):
    new_list = []
    for i in range(1, len(list1), 2):  # odd
        new_list.append(list1[i])
    for j in range(0, len(list1), 2):  # even
        new_list.append(list2[j])
    return new_list


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
print(odd_even_list_packing(l1, l2))


####
# 2. Remove and add item in a list
def remove_add_item_in_list(your_list, item_index):
    the_item = your_list.pop(item_index)
    print(f'List After removing element at index 4: {your_list}')
    your_list.insert(2, the_item)
    print(f'List after Adding element at index 2: {your_list}')
    your_list.append(the_item)
    print(f'List after Adding element at last: {your_list}')


list1 = [34, 54, 67, 89, 11, 43, 94]
remove_add_item_in_list(list1, 4)


####
# 3. Slice list into 3 equal chunks and reverse each chunk
def slice_list_and_return_reverse(your_list):
    lst1 = your_list[0:3]
    print(f'Chunk 1:{lst1}')
    lst1.reverse()
    print(f'After reversing it: {lst1}')
    lst2 = your_list[3:6]
    print(f'Chunk 1:{lst2}')
    lst2.reverse()
    print(f'After reversing it: {lst2}')
    lst3 = your_list[6:]
    print(f'Chunk 1:{lst3}')
    lst3.reverse()
    print(f'After reversing it: {lst3}')


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
slice_list_and_return_reverse(sample_list)


####
# 4. Count the occurrence of each element from a list
def count_occurrence(your_list):
    output = {}
    for item in your_list:
        count = your_list.count(item)
        output.setdefault(item, count)
    return output


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print(count_occurrence(sample_list))


####
# 5. Create a Python set such that it shows the element from both lists in a pair
def get_list_pairs_as_set(list1, list2):
    return set(zip(list1, list2))


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print(get_list_pairs_as_set(first_list, second_list))
print('The end!')


####
# 6. Find the intersection (common) of two sets and remove those elements from the first set
def remove_common_n_from_first_set(set1, set2):
    intersection = set1.intersection(set2)
    for item in intersection:
        first_set.remove(item)
    return set1


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
print(remove_common_n_from_first_set(first_set, second_set))


####
# 7. Checks if one set is a subset or superset of another set. If found, delete all elements from that set
def check_sub_or_super_set_and_delete(set1, set2):
    print(f'First set is subset of second set - {set1.issubset(set2)}')
    print(f'Second set is subset of First set - {set2.issubset(set1)} \n')
    print(f'First set is Super set of second set - {set1.issuperset(set2)}')
    print(f'Second set is Super set of First set - {set2.issuperset(set1)} \n')
    if set1.issubset(set2) and set2.issuperset(set1):
        set1.clear()
        print(f'First Set: {set1}')
        print(f'Second Set: {set2}')
    else:
        set2.clear()
        print(f'First Set: {set1}')
        print(f'Second Set: {set2}')


first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

check_sub_or_super_set_and_delete(first_set, second_set)


####
# 8. Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# If not, delete it from the list
def get_all_values_in_dict(your_lst, your_dict):
    new_list = []
    for item in your_lst:
        if item in your_dict.values():
            new_list.append(item)

    return new_list


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print(get_all_values_in_dict(roll_number, sample_dict))


####
# 9. Get all values from the dictionary and add them to a list but don’t add duplicates
def get_all_unique_values_from_dict(your_dict):
    uniques = []
    for value in your_dict.values():
        if value not in uniques:
            uniques.append(value)
    return uniques


speed = {'jan': 47,
         'feb': 52,
         'march': 47,
         'April': 44,
         'May': 52,
         'June': 53,
         'july': 54,
         'Aug': 44,
         'Sept': 54}

print(get_all_unique_values_from_dict(speed))

print(20 * '-', 'EX 10', 20 * '-')


####
# 10. Remove duplicates from a list and create a tuple and find the minimum and maximum number
def remove_duplicates_print_tuple_max_min(your_list):
    uniques = list()
    for item in your_list:
        if item not in uniques:
            uniques.append(item)
    print(f'unique items: {uniques}')
    print(f'tuple : {tuple(uniques)}')
    print(f'min : {min(uniques)}')
    print(f'max : {max(uniques)}')


sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
remove_duplicates_print_tuple_max_min(sample_list)

print('The end!')
