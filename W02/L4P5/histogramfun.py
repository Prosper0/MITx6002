import pylab

# You may have to change this path
WORDLIST_FILENAME = r"F:\Dev\Python\MITx6002\W02\L4P5\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowelsList = []
    for word in wordList:
        cntVowels = 0
        for letter in word.lower():
            if letter in 'aeiou':
                cntVowels = cntVowels + 1
        vowelsList.append(cntVowels/float(len(word)))
    pylab.figure()
    pylab.title("Vowel Proportion Histogram")
    pylab.xlabel('Proportion of Vowels')
    pylab.ylabel('Number of Vowels')

    pylab.hist(vowelsList, numBins)
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
