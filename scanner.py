def getCyphertext(filename):
    with open(filename, "r") as cypherfile:
        cyphertext = cypherfile.read()
    return cyphertext

def basicStats(cyphertext):
    print("Length of cyphertext: %d" % len(cyphertext))
    return

def gatherStats(cyphertext):
    charMap = {}
    for c in cyphertext:
        if c in charMap:
            charMap[c]+= 1
        else:
            charMap[c] = 1;
    return charMap

def printStats():
    return

def buildFracCyphers(num):
    return 

def buildPercentageTable(cyphertext, keyLength = 1):
    clen = len(cyphertext)
    charMap = gatherStats(cyphertext)
    pcgMap = {}
    for c in charMap:
        pctg = (charMap[c]/clen)*100
        pcgMap[c] = pctg
    
    
def removeKey(dict, key):
    newDict = dict(d)
    del newDict(key)
    return newDict

cyphertext = getCyphertext("theText1.txt").upper()
basicStats(cyphertext)
print(gatherStats(cyphertext))
