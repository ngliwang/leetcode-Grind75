from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        balance = amount
        coins_array = [0] * len(coins)
        coins_sum = 0

        for index, coin in enumerate(coins[::-1]):
            
            original_index = len(coins) - 1 - index
            print(f"Original index: {original_index}, Coin: {coin}")

            num_coins = math.floor(balance / coin)
            balance = balance - num_coins * coin
            coins_array[original_index] = num_coins

        
        if balance > 0:
            print("negative")
            return -1
        else:
            for each in coins_array:
                coins_sum += each

        print("balance", balance)
        print("coins array", coins_array)
        print("coins sum", coins_sum)
        return coins_sum

        # # print(coins)
        # counter = 0
        # balance = amount
        # biggest_deno = coins[-1]
        # coins_pointer = len(coins)
        # print("pointer", coins_pointer)

        # while(balance>0 and (balance / coins[coins_pointer] >=1)):
            

        # number_biggest_coins = math.floor(amount / biggest_deno)
        # # print(number_biggest_coins)

        # balance = balance - number_biggest_coins * biggest_deno

        # print(balance)


        


if __name__ == "__main__":
    s = Solution()
    s.coinChange([186,419,83,408], 6249)