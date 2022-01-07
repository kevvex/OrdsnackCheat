import sys
from itertools import permutations

def findWordPermutations(word):
    return [''.join(p) for p in permutations(word)]

def findWordList(lettersInWord, file):
    perms = findWordPermutations(lettersInWord)
    newList = [e.strip() for e in file.readlines()]
    matchList = []
    for perm in perms:
        for word in newList:
            if perm == word:
                matchList.append(word)
            #print(f'{perm} == {word}')

    return set(matchList)

def printWords(wordList):
    for word in wordList:
        print(word)

    if wordList == set():
        print('No result found')

def main():
    file = open('sven.txt', 'r', encoding='UTF-8')
    word = sys.argv[1]
    wordList = findWordList(word, file)
    printWords(wordList)
    
    file.close()

main()