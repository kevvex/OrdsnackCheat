import sys
from itertools import permutations
from treeGen import TreeGenerator

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
    filename = sys.argv[1]
    file = open(filename, 'r', encoding='UTF-8')
    word = sys.argv[2]
    wordSet = findWordList(word, file)
    sortedList = sorted(list(wordSet), key=len, reverse=True)

    if sortedList == set():
        print('No result found')

    tree_gen = TreeGenerator(word, sortedList)

    if sys.argv[3] == '-g':
        tree_gen.generate_graphviz()
    elif sys.argv[3] == '-d':
        tree_gen.generate()

    file.close()

main() # Remove this temporarily when running tests