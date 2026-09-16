#!/usr/bin/env python3

import random

def get_achievements() -> tuple[str, ...]:
    achievements = ("Strategist", "Speed Runner", "World Savior", 
    "Crafting Genius", "Master Explorer", "Collector Supreme", "Untouchable", 
    "Boss Slayer", "Unstoppable", "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder")
    return achievements

def gen_random_set(achievements: tuple[str, ...]) -> set:
    random_set = set(random.sample(achievements, random.randint(1, 14)))
    return random_set

def distinct(alice: set, bob: set, charlie: set, dylan: set) -> None:
    print(f"All distinct achievements: {set.union(alice, bob, charlie, dylan)}"
          "\n")

def common(alice: set, bob: set, charlie: set, dylan: set) -> None:
    print(f"Common achievements: {set.intersection(alice, bob, charlie,
    dylan)}\n")

def uniqueness(alice: set, bob: set, charlie: set, dylan: set) -> None:
    a = alice.difference(bob, charlie, dylan)
    b = bob.difference(alice, charlie, dylan)
    c = charlie.difference(alice, bob, dylan)
    d = dylan.difference(alice, bob, charlie)
    print(f"Only Alice has: {a}")
    print(f"Only Bob has: {b}")
    print(f"Only Charlie has: {c}")
    print(f"Only Dylan has: {d}\n")

def needs(achievements: tuple[str, ...], alice: set, bob: set, charlie: set, 
          dylan: set) -> None:
    all = set(achievements)
    a = all.difference(alice)
    b = all.difference(bob)
    c = all.difference(charlie)
    d = all.difference(dylan)
    print(f"Alice is missing: {a}")
    print(f"Bob is missing: {b}")
    print(f"Charlie is missing: {c}")
    print(f"Dylan is missing: {d}")

def gen_player_achievements() -> None:
    achievements = get_achievements()
    alice = gen_random_set(achievements)
    bob = gen_random_set(achievements)
    charlie = gen_random_set(achievements)
    dylan = gen_random_set(achievements)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")

    distinct(alice, bob, charlie, dylan)
    common(alice, bob, charlie, dylan)
    uniqueness(alice, bob, charlie, dylan)
    needs(achievements, alice, bob, charlie, dylan)

if __name__ == "__main__":
    print("=== Achievement Tracker SYstem ===\n")
    gen_player_achievements()
