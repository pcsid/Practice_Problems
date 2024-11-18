class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:  # Handle empty input
            return []
        
        output = []
        phoneDict = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def recursive(currString, nextDigits):
            if not nextDigits:  
                output.append(currString)
            else:
                for letter in phoneDict[nextDigits[0]]:  # Access letters for the current digit
                    recursive(currString + letter, nextDigits[1:])  # Move to the next digit

        recursive("", digits)
        return output
