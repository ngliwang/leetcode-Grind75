class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                # if nothing else to pop, or if the last element is not the corresponding opening bracket
                if stack == [] or d[c] != stack.pop():
                    return False
            else:
                return False

        # true - nothing else left in stack to compare
        # false - something left in stack to compare, but no more right bracket
        return len(stack) == 0

solution = Solution()
value = solution.isValid("(")
print(value)