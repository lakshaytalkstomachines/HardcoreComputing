"""
Write a function that takes a word as input and generates all possible unique permutations of its letters. Without using any libraries.
"""
import argparse
from rich.console import Console


def unique_permutations(word):
    if len(word) == 1:
        return [word]
    else:
        permutations = []
        for i in range(len(word)):
            for p in unique_permutations(word[:i] + word[i+1:]):
                permutations.append(word[i] + p)
        return permutations

def character_color_rich(character):
    """
    maps the entire english alphabet to a each unique color. according rich library.
    """
    map = {
        "a": "bright_red",
        "b": "green",
        "c": "blue",
        "d": "yellow",
        "e": "magenta",
        "f": "bright_yellow",
        "g": "bright_magenta",
        "h": "red",
        "i": "cyan",
        "j": "bright_blue",
        "k": "bright_green",
        "l": "purple",
        "m": "orange1",
        "n": "deep_sky_blue1",
        "o": "spring_green1",
        "p": "hot_pink",
        "q": "dark_orange",
        "r": "gold1",
        "s": "turquoise2",
        "t": "steel_blue",
        "u": "violet",
        "v": "orchid",
        "w": "khaki1",
        "x": "deep_pink2",
        "y": "light_goldenrod1",
        "z": "bright_white",
    }
    return map.get(character, "white")

    

def print_permutations(word, console):
    """
    This function will print the permutations of the word in a readable format ( sorted ).
     Use different colors for each word in a permutation. using rich library.
    
     For example:
     Permutations of abc:
     a b c
     a c b
     b a c
     b c a
     c a b
     c b a

     a is green
     b is red
     c is blue
    """
    console.print(f"Permutations of {word}:")
    for p in unique_permutations(word):
        for i in range(len(p)):
            color = character_color_rich(p[i])
            console.print(f"[{color}]{p[i]}[/]", end="")
        console.print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    console = Console()
    parser.add_argument("-w", "--word", type=str, help="The word to generate permutations for", required=True)
    args = parser.parse_args()
    print_permutations(args.word, console)