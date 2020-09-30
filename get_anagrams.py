import itertools

words_file = open('words_alpha.txt', 'r')
words_list = [line.strip() for line in words_file.readlines()]

words_by_length = {}
for i in range(1,34):
    words_by_length[i] = {}

def word_to_dict(word):
    d = {char: 0 for char in word}
    for char in word:
        d[char] += 1
    return d

for w in words_list:
    #if len(w) < 10:
    words_by_length[len(w)].update({w : word_to_dict(w)})

def check_anagram(s):
    string_dict = word_to_dict(s)
    string_len = len(s)
    matches = []
    for w in words_by_length[string_len]:
        if string_dict == (words_by_length[string_len][w]):
            matches.append(w)
    return(matches)

def get_anagrams(jumble):
    for i in range(len(jumble)+1,4,-1):
        all_matches = []
        combinations = itertools.combinations(jumble,i)
        for c in combinations:
            all_matches += check_anagram(c)
        if all_matches != []:
            print(str(i)+" Letters")
            print(', '.join(set(all_matches)))
            print()