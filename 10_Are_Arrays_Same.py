
def comp(array1, array2):

    if array1 != None and array2 != None and len(array1) == len(array2):
        list1 = ([abs(x) for x in array1])
        list1 = sorted(list1)
        list2 = sorted(array2)

        for count, num1 in enumerate(list1, 0):
            if num1 * num1 != list2[count]:
                return False
        return True
    else:
        return False

# * * * * * * * * * * * * *  * *
# Alternative Solution 1
# For the amount of times the value i*i is in array2. Remember i is an item not a counter
# Great use of try and except to deal with anything that isn't correct.
# Doesn't need abs command because gets squared first, then sorted and then compared
def comp2(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

# Alternative Solution 2
def comp3(a, b):
    try:
        return sorted(i*i for i in a) == sorted(b)
    except:
        return False

a1 = [-121, -144,19, -161, 19, -144, 19, -11,3,3]
a2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361,9,9]
# a1 = ''
# a2 = ''

print(comp(a1,a2));
print(comp2(a1,a2));
print(comp3(a1,a2));

