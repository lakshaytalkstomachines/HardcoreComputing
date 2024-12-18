"""
This file will contain code that will be used to test the code in the other files.

This will use test tables to test the code. and python dataclass to create test cases.
"""

from probablity.step_rule import total_outfits
from probablity.sum_rule import run_simulations

from dataclasses import dataclass

# For step rule
# Create a test case class to store the test cases                      
@dataclass
class Test:
    shirts: int
    pants: int
    shoes: int
    expected: int           

# Create a test table to store the test cases                      
test_table = [
    Test(shirts=3, pants=2, shoes=4, expected=24),
    Test(shirts=2, pants=3, shoes=2, expected=12),
    Test(shirts=1, pants=1, shoes=1, expected=1),
]

# Create a function to run the tests and print appropriate messages with the results with emojis and expectations.                        
def run_tests(test_table):
    for test in test_table:  
        # this shoudl print the test case in a readable format                   
        print(f"Running test: Shirts: {test.shirts}, Pants: {test.pants}, Shoes: {test.shoes} Expected: {test.expected}")
        result = total_outfits(test.shirts, test.pants, test.shoes)
        if result == test.expected:
            print("✅ Test passed")
        else:
            print("❌ Test failed") 
    print("All tests passed")              

# Run the tests                      
run_tests(test_table)

# for sum rule
@dataclass
class EvenSumTest:
    num_simulations: int
    num_dice: int
    num_runs: int
    expected: float

test_table = [
    EvenSumTest(num_simulations=1000000, num_dice=2, num_runs=10, expected=0.5),
    EvenSumTest(num_simulations=1000000, num_dice=3, num_runs=10, expected=0.5),
    EvenSumTest(num_simulations=1000000, num_dice=4, num_runs=10, expected=0.5),
]

def run_tests(test_table):
    for test in test_table:
        print(f"Running test: Num Simulations: {test.num_simulations} Num Dice: {test.num_dice} Num Runs: {test.num_runs} Expected: {test.expected}")
        result = run_simulations(test.num_simulations, test.num_dice, test.num_runs)
        if result == test.expected:
            print("✅ Test passed")
        else:
            print(f"❌ Test failed Actual: {result} Expected: {test.expected}")
    print("All tests passed")

run_tests(test_table)       