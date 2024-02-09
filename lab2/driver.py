import main

my_list = [4, 4, 6, 6, 7, 9, 10, 11, 12, 13, 13, 13,
           14, 19, 26, 26, 27, 28, 33, 33, 33, 33,
           35, 38, 39, 41, 47, 49, 49, 50, 50, 50,
           53, 54, 55, 56, 57, 59, 60, 61, 61, 61,
           67, 68, 68, 72, 78, 78, 78, 78, 79, 80,
           82, 87, 89, 90, 92, 93, 93, 99]
list1 = [5, 19, 27, 45, 49, 58, 59, 63, 84, 100]
list3 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
list2 = [1, 100]
empty_list = []
none_list = None
singleton_list = [5]

lo = 19
hi = 84
range_list = main.extract(list1, lo, hi)
print(range_list)
lo = 2
hi = 4
range_list = main.extract(list3, lo, hi)
print("repeating list: ", range_list)
lo = 19
hi = 84
range_list = main.extract(list1, lo, hi)
print(range_list)
lo = 57
hi = 78
range_list = main.extract(list2, lo, hi)
print("two values in the list: ", range_list)
lo = 57
hi = 78
range_list = main.extract(my_list, lo, hi)
print("Both lo and hi found: ", range_list)
lo = 2
hi = 4
range_list = main.extract(singleton_list, lo, hi)
print("singleton list exclusive: ", range_list)
lo = 2
hi = 5
range_list = main.extract(singleton_list, lo, hi)
print("singleton list inclusive: ", range_list)
lo = 57
hi = 78
range_list = main.extract(none_list, lo, hi)
print("List is None: ", range_list)
lo = 58
hi = 78
range_list = main.extract(my_list, lo, hi)
print("low not found: ", range_list)
lo = 38
hi = 94
range_list = main.extract(my_list, lo, hi)
print("high not found: ", range_list)
lo = None
hi = 56
range_list = main.extract(my_list, lo, hi)
print("low is None: ", range_list)
lo = 38
hi = None
range_list = main.extract(my_list, lo, hi)
print("high is None: ", range_list)
lo = None
hi = None
range_list = main.extract(my_list, lo, hi)
print("High and low are both None: ", range_list)
lo = 57
hi = 38
range_list = main.extract(my_list, lo, hi)
print("low > high: ", range_list)
