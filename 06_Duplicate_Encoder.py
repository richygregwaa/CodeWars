
# My Solution
def duplicate_encode(word):
    string = word.lower();
    string2 ='';

    for letter in string:
        if string.count(letter) == 1:
            string2 += "(";
        else:
            string2 += ")";
    return string2


# Alternative Solution
def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


print(duplicate_encode('@boB@"'))
print(duplicate_encode2('@boB@"'))

# Simple example of Join with Tuple
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Simple example of Join with Dictionary
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

