# Task 1: Given the two lists

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

combine_list = submitted + attended

item_count = combine_list.count("Alice")
print(item_count)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

print(submitted is attended)


# Using list methods, remove any student from the attended list who did not submit their assignment.

attended.remove("Eve")
attended.remove("Frank")
print(attended)