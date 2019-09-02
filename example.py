nrows = 3
ncols = 2
value = None

# for loop
# Fill the list with items so that [] accesses a valid index
the_list = [None] * nrows
for i in range(nrows):
    the_list[i] = [value] * ncols
the_list[0][0] = 42

# Alternatively, populate an empty list using a slice
# I wouldn't do this - it's too tricky.
the_list = [] * nrows
for i in range(nrows):
    # Slices append the individual items in an iterable
    # To append an iterable, wrap it in... an iterable...
    the_list[i:] = [[value] * ncols]
the_list[0][0] = 42

# Nested list comprehension
the_list = [[value for _ in range(ncols)] for _ in range(nrows)]
the_list[0][0] = 42

# Multiplication in comprehension
the_list = [[value] * ncols for _ in range(nrows)]
the_list[0][0] = 42

# Do *not* use nested multiplication!
the_list = [[value] * ncols] * nrows
the_list[0][0] = 42
the_list[0][0] = 43
