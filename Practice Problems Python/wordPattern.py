class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        # If the length of the pattern doesn't match the number of words, return False
        if len(pattern) != len(words):
            return False
        
        # Create two dictionaries to establish a bijection between pattern and words
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            if char not in char_to_word:
                if word in word_to_char:
                    return False
                char_to_word[char] = word
                word_to_char[word] = char
            elif char_to_word[char] != word:
                return False
        
        return True



myObject = Solution()
pattern = "abba"
string = "dog cat cat dog"
print(myObject.wordPattern(pattern, string))