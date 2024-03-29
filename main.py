import curses
from curses import wrapper
import time
import random

# Function to display the start screen
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

# Function to display the target text and the user's input
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)  # Green for correct characters
        if char != correct_char:
            color = curses.color_pair(2)  # Red for incorrect characters

        stdscr.addstr(0, i, char, color)

# Function to load a random line of text from a file
def load_text():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# Function for the speed typing test
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)  # Set non-blocking input

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)  # Revert to blocking input when the text is completed
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:  # Check for the Esc key to exit the test
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            # Handle backspace: remove the last character from the user's input
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            # Add the pressed key to the user's input if there is room
            current_text.append(key)

# Main function
def main(stdscr):
    # Initialize color pairs
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:  # Check for the Esc key to exit the program
            break

# Run the program using curses.wrapper
wrapper(main)
