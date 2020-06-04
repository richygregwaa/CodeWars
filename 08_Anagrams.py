
# My first solution
def anagrams(word, words):
    anagramlist = []
    for c, value in enumerate(words, 1):
        word2, value2 = list(word), list(value)
        word2.sort()
        value2.sort()
        if word2 == value2:
            anagramlist.append(value)
    return anagramlist


# My second solution
def anagrams2(word, words):
    anagramlist=[]
    a = [anagramlist for i, val in enumerate(words) if sorted(word) == sorted(val) and anagramlist.append(val) or i == 0]
    return a[0]

# My second solution - updates based on Alternative solution 1.
# Lesson here is that left-most variable next to return is at ITEM level and not at the
# list level which I originally had as anagramlist. Need to build up list was removed
def anagrams2_1(word, words):
    return [val for val in words if sorted(word) == sorted(val)]

# Alternative solution 1
def anagrams3(word, words): return [item for item in words if sorted(item)==sorted(word)]


# Alternative solution 2
def anagrams4(word, words):
    match = sorted(word)
    return [w for w in words if match == sorted(w)]

# Alternative solution 3
def anagrams5(word, words):
    return [w for w in words if sorted(word)==sorted(w)]


test_word1 = 'abba';
test_words1 = ['aabb', 'abcd', 'bbaa', 'dada', 'abab'];
test_word2 = 'racer';
test_words2 = ['crazer', 'carer', 'racar', 'caers', 'racer'];
test_word3 = 'laser';
test_words3 = ['lazing', 'lazy', 'lacar'];

print(anagrams2_1(test_word1,test_words1))
print(anagrams2_1(test_word2,test_words2))
print(anagrams2_1(test_word3,test_words3))


# nagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) = > ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) = > ['carer', 'racer']    #
# anagrams('laser', ['lazing', 'lazy', 'lacer']) = > []