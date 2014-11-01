import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

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
    Write code to plot a histogram of the proportion of vowels in each word
    of a given wordList. Vowels are 'A', 'E', 'I', 'O', 'U'.
    """
    data = []
    for w in wordList:
        vowel_count = len([ x for x in w if x in ['a','e','i','o','u'] ])
        prop = vowel_count/float(len(w))
        print prop
        data.append(prop)
    pylab.hist(data, numBins)
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList, 5)
