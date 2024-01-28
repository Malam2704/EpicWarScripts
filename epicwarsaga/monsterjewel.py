import pyautogui
import time

SCREEN_ADDER = 0

def perform_actions():
    # Coordinates for the clicks
    first_click_x, first_click_y = 1056, 1278
    second_click_x, second_click_y = 828, 1510
    third_click_x, third_click_y = 986, 1354

    # Keys to press
    first_key = 'u'
    second_key = '1'

    # Perform the first click
    pyautogui.click(first_click_x + SCREEN_ADDER, first_click_y)
    time.sleep(0.2)  # Wait for 1/5th of a second

    # Perform the second click
    pyautogui.click(second_click_x+ SCREEN_ADDER, second_click_y)
    time.sleep(0.2)  # Wait for 1/5th of a second

    # Press the two keys
    pyautogui.press(first_key)
    time.sleep(0.2)  # Wait for 1/5th of a second
    pyautogui.press(second_key)
    time.sleep(0.2)  # Wait for 1/5th of a second

    # Perform the third click
    pyautogui.click(third_click_x+ SCREEN_ADDER, third_click_y)
    time.sleep(0.2)  # Wait for 1/5th of a second

# Loop the actions indefinitely
while True:
    perform_actions()
    time.sleep(4)  # Delay of 1 second before repeating the loop
