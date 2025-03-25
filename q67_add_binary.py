class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        if a == '0' and b == '0':
            pass
        if len(a) > len(b):
            b = '00' + b
            a = '0' + a
        elif len(b) > len(a):
            a = '00' + b
            b = '0' + a
        else:
            a = '0' + a
            b = '0' + b

        print('cleaned char', a, b)

        max_len = max(len(a), len(b))
        print('MAX_len', max_len)
        # output = '0' * max_len
        output = ''
        print('output', output)
        remain = 0
        pointer = 1


        # max_len = max(len(a), len(b))
        print('MAX_len', max_len)

        increment = 0

        for x in range(max_len):
            print('ptr', pointer)
            print(f'a,b {a[-pointer]}, {b[-pointer]}')
            sum = int(a[-pointer]) + int(b[-pointer]) + increment

            if sum == 3:
                increment = 1
                remain = 1

            if sum == 2:
                increment = 1
                remain = 0

            if sum == 1:
                increment = 0
                remain = 1

            if x+1 == max_len:
                if increment == 1:
                    remain = 1

            # output[-x] = remain
            output = str(remain) + output
            pointer += 1
            # increment = 0

        print('output', output)
        return output

            # print("carry", carry)


if __name__ == "__main__":
    runner = Solution()
    runner.addBinary('0', '0')
