from pynput.keyboard import Key, Controller
import random
import time


def generate_random(start, end):
	random_num = random.randint(start, end + 1)
	return random_num


def key_press(keyboard, keys, times=1):
	for i in range(times):
		for key in keys:
			keyboard.press(key)

		for key in keys:
			keyboard.release(key)


if __name__ == "__main__":
	keyboard = Controller()
	delay = 10

	while True:
		tab_times = generate_random(15, 30)
		switch_tab_times = generate_random(2, 6)

		print(f"Sleeping {delay} seconds...")
		time.sleep(delay)

		key_press(keyboard, [Key.tab], tab_times)
		print(f"Pressing Tab {tab_times} times")

		key_press(keyboard, [Key.enter])

		if (tab_times % 2 == 0):
			print("Switching Tabs...")
			key_press(keyboard, [Key.ctrl, Key.tab], switch_tab_times)
