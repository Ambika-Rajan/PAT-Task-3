def find_triplet_with_sum(nums, target):
    n = len(nums)
    found_triplets = []

    # Sort the list for easier handling
    nums.sort()

    # Iterate through each element and use a two-pointer approach
    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                found_triplets.append((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return found_triplets


# Given list and target value
my_list = [10, 20, 30, 9]
target_value = 59

# Find triplets
triplets = find_triplet_with_sum(my_list, target_value)

# Output result
if triplets:
    print("Triplets found:", triplets)
else:
    print("No triplets found that sum to", target_value)
