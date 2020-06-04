# My Solution
def tickets(notes):

    till=[];
#    print(notes)
    for note in notes:

        if note == 25:
            till.append(note)

        if note == 50:
            if till.count(25) > 0:
                till.remove(25)
                till.append(note)
            else:
                return "NO"

        if note ==100:
            if till.count(25) >= 1 and till.count(50) >= 1:
                till.remove(50)
                till.remove(25)
                till.append(100)
            elif till.count(25) >= 3:
                till.remove(25)
                till.remove(25)
                till.remove(25)
                till.append(100)
            else:
                return "NO"
    return "YES"


# Alternative Solutions 1
def tickets1(people):
    till = {100.0: 0, 50.0: 0, 25.0: 0}

    for paid in people:
        till[paid] += 1
        change = paid - 25.0

        for bill in (50, 25):
            while (bill <= change and till[bill] > 0):
                till[bill] -= 1
                change -= bill

        if change != 0:
            return 'NO'

    return 'YES'



# a = [25, 25, 50]  # => YES
a = [25,25,25,25,25,25,25,50,50,100,25,25,100,100]
b = [25, 100] # => NO.
c = [25, 25, 50, 50, 100] # => NO

print(tickets(a));
print(tickets(b))
print(tickets(c));
print("\n")
print(tickets1(a));
print(tickets1(b))
print(tickets1(c));
print("\n")
