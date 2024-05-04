# Let's construct a function that takes an indefinite number of keywords with assigned values
# and returns a dictionary whose keys ara the keywords and values are the values.

# For example:

# >>> my_function( dog = "Scooby", cat = "James")
# would output {'dog': 'Scooby, 'cat': 'James'}

def my_function(**kwargs):
    my_dict = {}

    for x, y in kwargs.items():
        my_dict[x] = y

    return my_dict

print(my_function(dog = "Scooby", cat = "James"))
