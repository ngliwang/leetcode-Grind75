# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:



def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    else:
        return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n



        while left < right:
            mid = (left+right) // 2 
            if isBadVersion(mid) == True:
                right = mid
            else:
                left = mid + 1
        
        return left

if __name__ == "__main__":
    n_ = 5
    bad = 4
    sol = Solution()
    print(sol.firstBadVersion(n=n_))