# Author: Mohammad Reza Arani

def skyline(*args):
    return max(args) if args else 0

nums = input()

nums = [int(n) for n in nums.split()]

print(skyline(*nums))
