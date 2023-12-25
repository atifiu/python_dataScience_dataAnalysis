'''
Using %timeit: your turn!
You'd like to create a list of integers from 0 to 50 using the range() function. However, you are unsure whether using list comprehension or unpacking the range object into a list is faster. Let's use %timeit to find the best implementation.

For your convenience, a reference table of time orders of magnitude is provided below (faster at the top).

symbol	name	unit (s)
ns	nanosecond	10-9
µs (us)	microsecond	10-6
ms	millisecond	10-3
s	second	100
'''
# Create a list of integers (0-50) using list comprehension
nums_list_comp = [num for num in range(51)]
print(nums_list_comp)

# Create a list of integers (0-50) by unpacking range
nums_unpack = [*range(51)]
print(nums_unpack)

'''
Using %timeit: specifying number of runs and loops
A list of 480 superheroes has been loaded into your session (called heroes). You'd like to analyze the runtime for converting this heroes list into a set. Instead of relying on the default settings for %timeit, you'd like to only use 5 runs and 25 loops per each run.

What is the correct syntax when using %timeit and only using 5 runs with 25 loops per each run?

%timeit -r5 -n25 set(heroes)
'''