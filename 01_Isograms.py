
# My Solution
def is_isogram2(string):
    for letter in string:
        l_count = string.count(letter);
        if l_count > 1:
            return False
    return True



# Alternative Solution
# This works because of the set command (ie using a set), will basically return a de-duplicated list and
# if the lengths are different then there must have been a duplicate
def is_isogram(string):
    return len(string) == len(set(string.lower()))



# Call and Test the functions
my_string1 = "sdfhkj";
print(is_isogram(my_string1));      # Execute my solution
print(is_isogram2(my_string1));     # Execute alternative solution

my_string2 = "ssdfhkj";
print(is_isogram(my_string2));      # Execute my solution
print(is_isogram2(my_string2));     # Execute alternative solution
