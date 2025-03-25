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

        mid = (right+left) // 2

        while left < right and mid>left and mid<right:
            if isBadVersion(mid) == True:
                right = mid
                mid=(right+left) // 2
                print(f"if: left: {left}, right: {right}, mid: {mid}")

            # GOOD version
            else:
                left = mid
                mid = (right+left) // 2


                print(f"else: left: {left}, right: {right}, mid: {mid}")
        
        if isBadVersion(left) == True:
            return left
        if isBadVersion(left+1) == True:
            return left+1

if __name__ == "__main__":
    n_ = 3
    bad = 1
    sol = Solution()
    print(sol.firstBadVersion(n=n_))