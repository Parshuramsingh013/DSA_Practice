def find_combinations(index, current_list, current_sum, target_sum, max_length, nums, results):
    # if the sum matches and size is within limits, save the result
    if current_sum == target_sum and len(current_list) <= max_length:
        results.append(current_list[:])
        return
    
    # stop recursion if index is out of bounds or max size is exceeded
    if index >= len(nums) or len(current_list) > max_length:
        return
    
    # include the current number
    current_list.append(nums[index])
    find_combinations(index + 1, current_list, current_sum + nums[index], target_sum, max_length, nums, results)
    # backtrack and exclude the current number
    current_list.pop()
    find_combinations(index + 1, current_list, current_sum, target_sum, max_length, nums, results)


# input values
nums = [17, 9, 8, 6, 5, 3, 2, 1]
target_sum = 17
max_length = 4
results = []


# find combinations
find_combinations(0, [], 0, target_sum, max_length, nums, results)
print(results)
