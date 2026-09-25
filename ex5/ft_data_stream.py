#!/usr/bin/env python3

import typing
import random

def gen_event() -> typing.Generator[tuple[str, str]]:
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["eat", "sleep", "run", "grab", "move", "climb", "swim",
               "release", "use"]
    while True: # stops when next() in loop done. bc new next() call starts from yield
        yield random.choice(names), random.choice(actions)

def consume_event(event_list: list) -> typing.Generator[tuple[str, str]]:
    while len(event_list):
        yield event_list.pop(random.randrange(len(event_list)))

if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")
    print("Build list of 10 events:")
    event_list = [] #[tuple[str, str]]
    for i in range(10):
        event_list.append(next(events))
    print(event_list)
    event = consume_event(event_list)
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
