#!/usr/bin/env python3

import random

def create_list() -> list:
    names = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
    "kevin", "Liam"]
    return names

def capitalize_list(names: list) -> list:
    capitalized = [name.capitalize() for name in names]
    return capitalized

def only_capitals(names: list) -> list:
    capitals = [name for name in names if name[0].isupper()]
    return capitals

def make_dictionary(names: list) -> dict[str, int]:
    dictionary = {name: random.randrange(0, 1000) for name in names}
    return dictionary

def score_average(scores: dict[str, int]) -> float:
    total = sum(scores[score] for score in scores)
    return round(total / len(scores), 2)

def highest_scores(scores: dict[str, int], average: float) -> dict[str, int]:
    #deze klopt nog niet
    highest_scores = {name: score for score in scores for scores[score] > average}
    return highest_scores

if __name__ == "__main__":
    print("=== Game Data Alchemist ===")
    names = create_list()
    print(f"Initial list of players: {names}")
    capitalized_list = capitalize_list(names)
    print(f"New list with all names capitalized: {capitalized_list}")
    print(f"New list of capitalized names only: {only_capitals(names)}")
    score_dict = make_dictionary(capitalized_list)
    print(f"Score dict: {score_dict}")
    average = score_average(score_dict)
    print(f"Score average is: {average}")
    print(highest_scores(score_dict, average))
