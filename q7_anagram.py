class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the strings
        s = sorted(s)
        t = sorted(t)

        # compare the sorted strings
        if s == t:
            return True
        else:
            return False
    
if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("rat", "car"))