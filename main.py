"""
  Skype detects user activity by frequency of keypresses and move movement. The
  script manages to fool skype by randomly pressing keys every n second (default
  20 seconds).
"""

from pynput.keyboard import Key, Controller
import random
import time
import sys


# generate a random number in provided range
def generate_random(start, end):
	random_num = random.randint(start, end + 1)
	return random_num


# press array of provided keys, n times
def key_press(keyboard, keys, times=1):
	for _ in range(times):
		for key in keys:
			keyboard.press(key)

		for key in keys:
			keyboard.release(key)


# main functionality of program
def main():
  keyboard = Controller()
  delay = 20

  while True:
    tab_times = generate_random(10, 15)
    switch_tab_times = generate_random(2, 6)

    print(f"Sleeping {delay} seconds...")
    time.sleep(delay)

    print(f"Clicking {tab_times}th link")
    key_press(keyboard, [Key.tab], tab_times)
    key_press(keyboard, [Key.enter])

    if (tab_times % 2 == 0):
      print("Switching Tabs...")
      key_press(keyboard, [Key.ctrl, Key.tab], switch_tab_times)


# entry-point to the script
if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Gracefully shutting down script...")
    sys.exit(0)