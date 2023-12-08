#!/usr/bin/python3
# written by: atholcomb
# count_missing_nums.py
# Create a function that takes a list of "mostly" numbers, counts the 
# amount of missing numbers and returns their sum. Watch out for strings!

def count_missing_nums(nums_list):
    count = 0
    
    for num in '123456789':
        if num not in nums_list:
            count += 1

    return count


print(count_missing_nums(["1", "3", "5", "7", "9"])) # 4
print(count_missing_nums(["7", "3", "1", "9", "5"])) # 4
print(count_missing_nums(["1", "5", "B", "9", "z"])) # 6
