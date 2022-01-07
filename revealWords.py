import sys
from itertools import permutations

def fullPermList(word):
    word_len = len(word)
    long_list = []
    for cur_word_len in range(word_len, 0, -1):
        listWords = findWordPermutations(word, cur_word_len)
        long_list += listWords.copy()
    return long_list

def findWordPermutations(word, wordLen):
    return [''.join(p) for p in permutations(word, wordLen)]

def findWordList(word, file):
    perms = fullPermList(word)
    newList = [e.strip() for e in file.readlines()]
    matchList = []
    for perm in perms:
        for word in newList:
            if perm == word:
                matchList.append(word)
            #print(f'{perm} == {word} -> {foundWord}')

    return set(matchList)

def main():
    file = open('svenska-ord.txt', 'r', encoding='UTF-8')
    word = sys.argv[1]
    wordList = findWordList(word, file)

    if wordList == set():
        print('No result found')

    for word in wordList:
        print(word)

    file.close()

main() # Remove this temporarily when running tests