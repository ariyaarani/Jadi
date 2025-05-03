def largest(nums):
    largest_number = nums[0]
    for n in nums:
        if largest_number < n:
            largest_number = n
    return largest_number    

my_nums = [1, 2, 5, 6, 87, 97, 107]
largest_number = largest(my_nums)
print(largest_number)