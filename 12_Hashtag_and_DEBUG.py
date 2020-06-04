import logging, sys

# Comment the below line in and out to get all the other debug messages
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Using logging.basicConfig to toggle the logging level to stderr
# and the simple log methods, debug, info, warning, error and critical



# My Solution
# What I learned in the 'while and' statements was to check 'i' before the 'and' then interrogate 's[i]'
# after the 'and'. I had it the other way round and caused me all sorts of confusion
def generate_hashtag(s):
    hash_word = "#"
    i = 0

    if len(s) == 0:
        return False

    while i < len(s)-1:
        while i < len(s) and s[i] == " ":
            i += 1;

        if i < len(s):
            hash_word = hash_word + s[i].upper()
            i += 1;

        while i < len(s) and s[i] != " ":
            hash_word = hash_word + s[i].lower()
            i += 1

    logging.info('We processed %d records', len(s))

    if len(hash_word) <= 140:
        return hash_word
    else:
        return False


logging.debug('A debug message!')



# Alternative Solutions 1
# Good way to read this is to imagine the word 'only' before the if statement
# Notice the double condition for just the one 'if' without 'and'!
def generate_hashtag1(s): return '#' +s.strip().title().replace(' ','') if 0<len(s)<=140 else False


# Alternative Solutions 2
# What I've taken from this solution is there must be a list of python commands somewhere to look at in
# the same way that I look at keywords for robotframework. So much is already done for you as shown below
# https://docs.python.org/3/library/ <-- googled 'python commands' and found this

def generate_hashtag2(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


# Alternative Solutions 3
# Notice how the return deals with the additional conditions.
# 'return' line not as clear as solution2 but condense - no 'if' used!
def generate_hashtag3(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False




Hash1 = " Hello there thanks for trying my Kata"
Hash2 = "    Hello     World   "
Hash3 = ""
Hash4 = "codewars"
Hash5 = "codeWars"
Hash6 = "c i n"


print(generate_hashtag(Hash1))
print(generate_hashtag(Hash2))
# print(generate_hashtag1(Hash3))
# print(generate_hashtag1(Hash4))
# print(generate_hashtag1(Hash5))


# =>  false
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false