class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        letter_dict = {}
        
        for each_letter in magazine:
            if each_letter not in letter_dict:
                letter_dict.update({each_letter:1})
            else:
                print(letter_dict[each_letter])
                letter_dict[each_letter] = letter_dict[each_letter] + 1

if __name__ == "__main__":
    ransomNote = 'ab'
    magazine = 'aab'

    s = Solution()
    print(s.canConstruct(ransomNote, magazine))