""" 
Write a function that simulates rolling two dice and determines if the sum is even or odd. Run the simulation many times and calculate the percentage of even sums.

Output should be like this: After 10,000 simulations, 49.8% of the dice rolls resulted in an even sum.
"""  

import random
import argparse

def dice_roll():
    return random.randint(1, 6)

def even_sum(dice_sum):
    return dice_sum % 2 == 0

def multi_dice_rolls(num_simulations, num_dice):
    """
    Simulate rolling multiple dice and determine if the sum is even or odd.
    """
    even_count = 0
    for _ in range(num_simulations):
        dice_sum = sum(dice_roll() for _ in range(num_dice))
        if even_sum(dice_sum):
            even_count += 1
    return even_count / num_simulations

# function to run num_simulations of num_dice , num_runs times and average the results, use the average to calculate the percentage of even sums
def run_simulations(num_simulations, num_dice, num_runs):   
    return sum(multi_dice_rolls(num_simulations, num_dice) for _ in range(num_runs)) / num_runs    

if __name__ == "__main__":  
    parser = argparse.ArgumentParser()  
    parser.add_argument("--num_simulations", type=int, default=1000000)
    parser.add_argument("--num_dice", type=int, default=2)
    parser.add_argument("--num_runs", type=int, default=10)
    args = parser.parse_args()

    num_simulations = args.num_simulations
    num_dice = args.num_dice
    num_runs = args.num_runs
    percentage = run_simulations(num_simulations, num_dice, num_runs)
    print(f"After {num_simulations} simulations, {percentage * 100}% of the dice rolls resulted in an even sum for {num_dice} dice for {num_runs} runs.")

