# TIME OUT
from typing import List

def maxProfit( prices: List[int]) -> int:
    buy_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < buy_price:
            buy_price = price
            continue
        
        profit = price - buy_price
        if profit > max_profit:
            max_profit = profit

    return max_profit