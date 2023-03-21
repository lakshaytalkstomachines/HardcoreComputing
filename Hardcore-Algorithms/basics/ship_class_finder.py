"""
    Given a map of letter classes and its corresponding Ship Classes, find for the given input which class of ship it is.

    'B' or 'b' -> 'BattleShip'
    'C' or 'c' -> 'Cruiser'
    'D' or 'd' -> 'Destroyer'
    'F' or 'f' -> 'Frigate'
"""
ship_classes = {
    'b' : "BattleShip",
    'c' : 'Cruiser',
    'd' : 'Destroyer',
    'f' : 'Frigate'
}

num_of_test_cases = int(input())

for _ in range(num_of_test_cases):
    letter_id = input().lower()
    ship_class = ship_classes.get(letter_id, "")
    print(ship_class)
