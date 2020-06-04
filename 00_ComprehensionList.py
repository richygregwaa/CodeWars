# Google "Python List"
# Select "5. Data Structures — Python 3.8.3 documentation"
# Select "5.1.3 List Comprehensions

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# squares
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


squares = [x**2 for x in range(10)]
print(squares)


squares = list(map(lambda x: x**2, range(10)))
print(squares)

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it. For example,
# this listcomp combines the elements of two lists if they are not equal:

# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
comp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(comp)

# and it’s equivalent to:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(comp)


# Other useful stuff on the page (see link at top)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.



# An example that uses most of the list methods:
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print (fruits)
print( fruits.count('apple') )
# 2

print( fruits.count('tangerine') )
# 0

print( fruits.index('banana') )
# 3

print( fruits.index('banana', 4) ) # Find next banana starting a position 4
# 6

fruits.reverse()
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print(fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

print(fruits.pop())

# 'pear'

# You might have noticed that methods like insert, remove or sort that only modify the list have
# no return value printed – they return the default None. 1 This is a design principle for all
# mutable data structures in Python


# Here are all of the methods of list objects:
#
# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x].
#
# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
#
# list.insert(i, x)
# Insert an item at a given position. The first argument is the index of the element before which
# to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x)
# is equivalent to a.append(x).
#
# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there
# is no such item.
#
# list.pop([i])
# Remove the item at the given position in the list, and return it. If no index is specified,
# a.pop() removes and returns the last item in the list. (The square brackets around the i
# in the method signature denote that the parameter is optional, not that you should type square
# brackets at that position. You will see this notation frequently in the Python Library Reference.)
#
# list.clear()
# Remove all items from the list. Equivalent to del a[:].
#
# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x.
# Raises a ValueError if there is no such item.
#
# The optional arguments start and end are interpreted as in the slice notation and are used to
# limit the search to a particular subsequence of the list. The returned index is computed
# relative to the beginning of the full sequence rather than the start argument.
#
# list.count(x)
# Return the number of times x appears in the list.
#
# list.sort(key=None, reverse=False)
# Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).
#
# list.reverse()
# Reverse the elements of the list in place.
#
# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].