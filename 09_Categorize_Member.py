
# My Solution
def openOrSenior(data):
    categoryOut=[]
    for member in data:
        if member[0] >= 55 and member[1] > 7:
            categoryOut.append("Senior")
        else:
            categoryOut.append("Open")
    return categoryOut


# * * * * * * * * * * * *
# Alternative solution1 - I came close to this but couldn't get syntax correct to allow an else
# This is awesome solution. Should come in really handy
def openOrSenior2(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data]
# * * * * * * * * * * * *


# Alternative solution1
def openOrSenior3(members):
    return ["Senior" if m[0]>54 and m[1]>7 else "Open" for m in members]



input = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]] # Age, Handicap
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
print (openOrSenior(input))
print (openOrSenior2(input))
print (openOrSenior3(input))