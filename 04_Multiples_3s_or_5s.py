
# My Solution
def solution(number):
    countnum = 1;
    numbers = [];
    while (countnum < number):
        if (countnum % 3) == 0 or (countnum % 5) == 0:  # % is mod ie the remainder value after division
            numbers.append (countnum);
        countnum += 1;
    return sum(numbers);


# Alternative Solution
def solution2(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


num = 20;
print (solution(num));
print (solution2(num));