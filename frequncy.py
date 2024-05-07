my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

# Sort the list
my_list.sort()

# Initialize variables
current_element = my_list[0]
count = 1

# Iterate over the sorted list to count occurrences
for i in range(1, len(my_list)):
    if my_list[i] == current_element:
        count += 1
    else:
        print(f"{current_element}: {count} times")
        current_element = my_list[i]
        count = 1

# Print the count for the last element
print(f"{current_element}: {count} times")
