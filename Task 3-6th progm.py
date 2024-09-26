
# Sample lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [6, 7, 8, 9, 10, 4]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find duplicates in all three lists using intersection
duplicates = set1.intersection(set2).intersection(set3)

# Convert to a list and print the result
duplicates_list = list(duplicates)
print("Duplicates in all three lists:", duplicates_list)