# TIME OUT
from typing import List
def maxProfit( prices: List[int]) -> int:
    profit_map = {}
    number_of_days = len(prices)
    for day in range(number_of_days):
        price_at_day = prices[day]
        for next_day in range(day+1, number_of_days):
            price_at_next_day = prices[next_day]
            curr_profit = price_at_next_day - price_at_day
            prev_profit = profit_map.get(day, 0)
            if curr_profit > prev_profit:
                profit_map[day] = curr_profit
    
    max_profit = 0

    for day in profit_map:
        profit = profit_map[day]
        if profit > max_profit:
            max_profit = profit
    
    return max_profit