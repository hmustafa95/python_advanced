from collections import deque

words = ['rose', 'tulip', 'lotus', 'daffodil']
vowels = deque(map(str, input().split()))
consonants = list(map(str, input().split()))
word_found = 0
dict_words = {}
name_of_word_found = ''

while consonants and vowels and word_found == 0:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for word in words:
        for char in word:
            if vowel == char:
                if word not in dict_words:
                    dict_words[word] = ''
                dict_words[word] += vowel
            if consonant == char:
                if word not in dict_words:
                    dict_words[word] = ''
                dict_words[word] += consonant
        if word in dict_words:
            if set(dict_words[word]) == set(word):
                name_of_word_found = word
                word_found += 1
                break

if word_found == 1:
    print(f"Word found: {name_of_word_found}")
else:
    print('Cannot find any word!')

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")