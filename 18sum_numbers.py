# Author: Mohammad Reza Arani

def sum_numbers(*args):
    return sum(args) if args else 0

nums = input()

nums = [int(n) for n in nums.split()]

print(sum_numbers(*nums))
