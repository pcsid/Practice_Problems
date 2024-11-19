class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        returnList = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            #print(sortedWord)
            if sortedWord not in myDict:
                myDict[sortedWord] = [word]
            else:
                myDict[sortedWord].append(word)
                #print(myDict[sortedWord])
        for key in myDict:
            returnList.append(myDict[key])
        return returnList