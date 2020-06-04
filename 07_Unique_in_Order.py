
# My solution
def unique_in_order(iterable):

    iterablelist = list(iterable)
    it_count = 0
    it_len = len(iterablelist) - 1

    while it_count < it_len:
        if iterablelist[it_count] == iterablelist[it_count+1]:
            del iterablelist[it_count:it_count+1]
            it_count -= 1
            it_len -= 1

        it_count += 1
    return iterablelist


# Alternative Solution 1
def unique_in_order1(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r
#RG so either x is True for matching last item in list 'r' OR if not append x to the list


# Alternative Solution 2
from itertools import groupby
def unique_in_order2(iterable):
    return [x for (x, _) in groupby(iterable)]


# Alternative Solution 3
def unique_in_order3(iterable):
    return [ ch for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]

# RG I change the above. Change 'ch' at the beginning to 'i' and it worked but returned i instead of 'ch'
def unique_in_order4(iterable):
    return [ i for i, ch in enumerate(iterable) if i == 0 or ch != iterable[i - 1] ]
# RG. Clever because gets round problem of looping beyond index by comparing previous item
# and not the next item. This then allows standard built in utility to be used.


string = 'AAAABBBCCDAABBB'
string2 = 'ABBCcAD'
listnum = [1,2,2,3,3]
#listnum = []

# print (unique_in_order(string));
# print (unique_in_order(string2));
# print (unique_in_order(listnum));
print (unique_in_order3(string));
print (unique_in_order4(string));


# Alternative Solution 4 - Look into this
unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
# Not really a trua answer as this isn't part of the Def and it doesn't accept 'iterable'


# # Random Examples
# for i in range (10):
#     print (i)
#     i = 5
# # i = 5 will simply get overwritten by the for loop


# The enumerate object yields pairs containing a count (from start, which defaults to zero)
# and a value yielded by the iterable argument. enumerate is useful for obtaining an indexed list:
# (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
some_list = 'AABBBCCDAA'
for counter, value in enumerate(some_list):
    print(counter, value)

# '1' is where the count starts from ie '1 apple'
# '2' will start from 2. '2 apple'
# if the ', 1' is removed then count starts from 0. '0 apple'
# Notice how 'c' at the beginning takes value '1' from the edge. Inner assignment (value) then outer (c)

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
