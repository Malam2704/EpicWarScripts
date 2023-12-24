import pyautogui
import time
import keyboard  # You need to install this library using 'pip install keyboard'

# Coordinates of where to click (x, y)
click_coordinates = [(1908, 658), (2376, 967), (2572, 1398), (2503, 1257)]  # Replace with your coordinates
org_coordinates = [(132, 331), (855, 968), (1051, 1398), (989, 1250)]

# Time delay between actions
delay = 1
assault_delay = 6

# Start the script with a delay
time.sleep(2)

# Variable to control the main loop
running = False

while True:
    if keyboard.is_pressed('h'):  # Start loop when 'H' is pressed
        running = True
        start_time = time.time()  # Start timer

    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > 50:  # Check if 50 seconds have passed
            # Place your action here
            pyautogui.moveTo((812, 152))
            pyautogui.click()
            pyautogui.moveTo((1893,766))
            pyautogui.click()
            print("50 seconds have passed!")
            # Reset the timer
            start_time = time.time()

        index = 0
        for coord in org_coordinates:
            if(index == 2):
                pyautogui.moveTo((1887, 378))
                time.sleep(assault_delay)
            pyautogui.moveTo(coord)
            pyautogui.click()
            time.sleep(delay)

            if(index == 3):
                for coord in org_coordinates:
                    if(index == 2):
                        time.sleep(assault_delay)
                    pyautogui.moveTo(coord)
                    pyautogui.click()
                    time.sleep(delay)
            index += 1

        time.sleep(5)

        if keyboard.is_pressed('j'):  # Stop loop when 'J' is pressed
            running = False

    time.sleep(0.1)  # To prevent high CPU usage
