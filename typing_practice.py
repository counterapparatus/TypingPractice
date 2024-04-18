# This is a simple program for me to practice my python and create something that will help me learn to type characters that I need to practice

import random
import curses

## initialize curses
stdscr = curses.initscr()


opening_prompt = (
    "Welcome to typing practice. This is a simple game to help you practice typing."
)
opening_prompt += "\nWe all know how to type, but if you are like me, there are some characters that are more difficult"
opening_prompt += "\nYou win when you enter all your characters correctly."
opening_prompt += "\nYou lose when you run out of lives (you have 3)."
opening_prompt += "\nPlease enter all the characters you need to practice: "

stdscr.addstr(opening_prompt)
stdscr.refresh()
characters = list(stdscr.getstr().decode())

# I want the characters to be in a dictionary so I can keep track of how many times each was type
correct_chars = {x: 0 for x in characters}
lives = 3
score = 0
while lives != 0:
    # Choose a random character, unless the player has already won (i.e dictionary is empty)
    if correct_chars:
        random_char = random.choice(list(correct_chars.keys()))
    else:
        break

    # Display message asking to enter the character
    stdscr.clear()
    stdscr.addstr(f"""
          \n\n\n\n--> {random_char} <--
          \n\n\nEnter the character that appears between the arrows:""")
    stdscr.refresh()

    # Get the key press and updating either number of lives or number of correct presses
    answer = stdscr.getkey()
    if answer == random_char:
        score += 1
        correct_chars[random_char] += 1
        if correct_chars[random_char] == 3:
            correct_chars.pop(random_char)
    else:
        lives -= 1
        stdscr.addstr("Oops")
        stdscr.refresh()


if lives == 0:
    stdscr.addstr(f"""
          \nGame Over
          \nYour final score was {score}
          \nYour Score for each character is:
          """)
    for char, correct in correct_chars.items():
        stdscr.addstr(f"{char} | {correct}")
else:
    stdscr.addstr(f"You won! Good typing! Your final score is {score}")
stdscr.refresh()
