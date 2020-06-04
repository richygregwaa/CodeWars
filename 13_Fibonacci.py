from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 1,1,2,3,5,8,13,21,34,55,89,144
# 1,2,3,4,5,6,07,08,09,10,11,012

print (fibonacci(400))

# test.assert_equals(fibonacci(70), 190392490709135)
# test.assert_equals(fibonacci(60), 1548008755920)
# test.assert_equals(fibonacci(50), 12586269025)