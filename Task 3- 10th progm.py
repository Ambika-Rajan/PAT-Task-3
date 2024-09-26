def has_zero_sum_sublist(nums):
    # Initialize an empty set to store cumulative sums
    cumulative_sum_set = set()
    cumulative_sum = 0

    for num in nums:
        # Update the cumulative sum
        cumulative_sum += num

        # Check if the cumulative sum is zero or already exists in the set
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True  # A sub-list with sum zero exists

        # Add the cumulative sum to the set
        cumulative_sum_set.add(cumulative_sum)

    return False  # No sub-list with sum zero found

# Given list
my_list = [4, 2, -3, 1, 6]

# Check for zero sum sub-list
if has_zero_sum_sublist(my_list):
    print("There is a sub-list with sum equal to zero.")
else:
    print("No sub-list with sum equal to zero found.")
