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


cyphertext = getCyphertext("theText1.txt").upper()
basicStats(cyphertext)
print(gatherStats(cyphertext))
