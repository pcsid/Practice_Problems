class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        store = []
        isGood = True
        for letter in magazine:
            store.append(letter)
        for letter in ransomNote:
            if letter in store:
                store.remove(letter)
            else:
                isGood = False
        return isGood

myObject = Solution()
ransomNote = "aa"
magazine = "ba"
print(myObject.canConstruct(ransomNote, magazine))