# -*- coding: cp1252 -*-
import string


def getCyphertext(filename):
    with open(filename, "r") as cypherfile:
        cyphertext = cypherfile.read()
    return cyphertext

def gatherStats(cyphertext):
    charMap = {}
    for c in cyphertext:
        if c in charMap:
            charMap[c]+= 1
        else:
            charMap[c] = 1
    return charMap

def sumAllInMap(mapa):
    total = 0
    for c in mapa:
        total += mapa[c]
    return total

def buildFracBox(num):
    fracBox = []
    for i in range(0, num):
        fracBox.append({})
    return fracBox;

def buildFracTables(cyphertext, num, includeTable):
    fracBox = buildFracBox(num)
    i = 0;
    #Pour un chiffrement de cesar, choisir longueur de la clé égal à 1
    #fracBox contiendra qu'un seul charMap
    for c in cyphertext:
        if c in includeTable:
            if c in fracBox[i % num]:
                fracBox[i % num][c] += 1
            else:
                fracBox[i % num][c] = 1
            i += 1
        #print("i = %d" % i)
    #Turn occurences into percentages

    for z in range(0, len(fracBox)):
        pcgMap = {}
        mapa = fracBox[z]
        total = sumAllInMap(mapa);
        #print("sum in all = %d" % total)
        for c in mapa:
            pctg = (mapa[c]*100.0)/total
            pcgMap[c] = pctg
        fracBox[z] = pcgMap    
    return fracBox

#Only consider chars that are also in the includeTable
def getMaxPercent(mapa, includeTable):
    currMax = 0
    char = "a"
    for c in mapa:
        if((mapa[c] > currMax) & (c in includeTable)):
            currMax = mapa[c]
            char = c
    #print(char, currMax)
    return (char, currMax)

#Get max of each table
#Get the max only if it is in the include table
def gmet(mapatable, includeTable):
    allMaxes = []
    for z in range(0, len(mapatable)):
        maxP = getMaxPercent(mapatable[z], includeTable)
        allMaxes.append(maxP)
        z += 1
    return allMaxes

#Makes a statistical analysis for multiple key lengths
#Assumes cesar in the case of abscence of parameters
def mpkt_fracs(cyphertext, includeTable, keyLength = 1):
    resultSet = []
    for i in range(1, keyLength+1):
        mapatable = buildFracTables(cyphertext, i, alphabet)
        maxEach = gmet(mapatable, includeTable)
        resultSet.append(maxEach)
        i += 1
    return resultSet

#get highest percentage for subset
def ghpfss(fracs):
    currMaxInTable = ("aplaceholder", 0)
    for tup in fracs:
        if(tup[1] > currMaxInTable[1]):
            currMaxInTable = tup
    return currMaxInTable

#print most frequent letters per key length
def pmfl_kl(mpktFracs):
    resultSet = []
    for z in range(0, len(mpktFracs)):
        print("%d: " % (z+1))
        print(ghpfss(mpktFracs[z]))
        print("\n")
        z +=1
    return



#Après analyse, le texte semble seulement encoder des caractères alphabetiques (pas de nombres, d'espaces newlines ...)
alphabet = string.ascii_uppercase

cyphertext = getCyphertext("theText1.txt").upper()
pmfl_kl(mpkt_fracs(cyphertext, alphabet, 3500))

