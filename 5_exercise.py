# Exercise 5: Check if the first and last number of a list is the same

# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# 3 types of arrays

# tuple - immutable, not to be changed after creation
ovoce = ("Apple", "Banana")
ovoce[1] = "Pear"
ovoce

ovoce = ("Apple", "Pear")
ovoce

# list
ovoce = ["Apple", "Banana"]
ovoce[1] = "Pear"
ovoce

# dictionary
znamky_studentu = {"Wilson": 1, "Winona": 3, "Wigfrid": 2}
znamky_studentu["Winona"]
znamky_studentu["Wigfrid"] = 1
znamky_studentu

# task
lst_1 = [10, 20, 30, 40, 10]
lst_2 = [13, 47, 26, 345, 12, 324, 234, 23]

lst_1[0]
lst_1[-1]

lst_1[0] == lst_1[-1]

def Check_first_last(lst):

    print(f"Your list: {lst}")
    print(f"Result is: {lst[0] == lst[-1]}")

Check_first_last([1,2,3,4,5,1])
Check_first_last(lst_1)
Check_first_last(lst_2)

