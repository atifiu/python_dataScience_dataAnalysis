"""
Numpy arrays are homogenous i.e. must contain elements of one type only
numpy array index works numpy[0, 1] will return first elemnt
boolean indexing i.e. numpy[numpy > 0]
"""
import numpy as np

nums = np.array([[ 1 , 2 , 3 , 4 , 5],
 [ 6 ,7 , 8 , 9 ,10]])
print(nums)

# Print second row of nums
print(nums[1,:])

# Print all elements of nums that are greater than six
print(nums[nums > 6])

# Double every element of nums
nums_dbl = nums * 2
print(nums_dbl)

# Replace the third column of nums
nums[:,2] = nums[:,2] + 1
print(nums)




"""
Bringing it all together: Festivus!
In this exercise, you will be throwing a party—a Festivus if you will!

You have a list of guests (the names list). Each guest, for whatever reason, has decided to show up to the party in 10-minute increments. For example, Jerry shows up to Festivus 10 minutes into the party's start time, Kramer shows up 20 minutes into the party, and so on and so forth.

We want to write a few simple lines of code, using the built-ins we have covered, to welcome each of your guests and let them know how many minutes late they are to your party. Note that numpy has been imported into your session as np and the names list has been loaded as well.

Let's welcome your guests!
"""
# Create a list of arrival times
arrival_times = [*range(10,60,10)]
print(arrival_times)

# Create a list of arrival times


# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)
names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
def welcome_guest(guest_arrivals):
    return "Welcome to Festivus " + str(guest_arrivals[0])+ "... You're " + str(guest_arrivals[1]) + " min late."

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[index],time) for index,time in enumerate(new_times)]
print(guest_arrivals)

# Map the welcome_guest function to each (guest,time) pair
welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]
print(guest_welcomes)
print(*guest_welcomes, sep='\n')
