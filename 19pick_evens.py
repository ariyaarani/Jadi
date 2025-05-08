# Author: Mohammad Reza Arani

def pick_evens(*args):
    return [n for n in args if n % 2 == 0]

nums = input()

nums = [int(n) for n in nums.split()]

print(pick_evens(*nums))
