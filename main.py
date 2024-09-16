from random import randint

import art
from game_data import data
import random

print(art.logo)
print("Welcome to Higher or Lower! Let's get Started")

current_score = 0
game_over = False
a = ""

option_1 = randint(0, len(data))
option_1_followers = data[option_1]["follower_count"]

while game_over == False:
    option_2 = randint(0, len(data))
    option_2_followers = data[option_2]["follower_count"]

    a = print(
        f"A: a(n) {data[option_1]['description']} from "
        f"{data[option_1]['country']} called {data[option_1]['name']}")
    print(art.vs)
    b = print(
        f"B: a(n) {data[option_2]['description']} from "
        f"{data[option_2]['country']} called {data[option_2]['name']}")
    highest_count = max(option_1_followers, option_2_followers)
    a_or_b = {"a": option_1_followers, "b": option_2_followers}
    answer = input("Please select an answer, 'A' or 'B' ").lower()
    answer_followers = a_or_b[answer]

    if answer_followers == highest_count:
        current_score += 1
        print(f"Your current score is {current_score}")
        print("That's right!")
        if highest_count == a_or_b["a"]:
            continue
        else:
            option_1 = option_2
            still_continue = False
    else:
        print(current_score)
        print("That's wrong! Game over")
        break






