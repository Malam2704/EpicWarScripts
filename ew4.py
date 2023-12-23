import pyautogui
import time

# Coordinates of where to click (x, y)
click_coordinates = [(1908, 658), (2376, 967), (2572, 1398), (2503, 1257)] # Replace with your coordinates
org_coordinates = [(1257, 1038), (855, 968) ,(1051, 1398) ,(989, 1250)]
# Time delay between actions
delay = 1

# Start the script with a delay
time.sleep(2)
assault_delay = 7.5

# Main loop to click repeatedly
while True:
    index = 0
    for coord in org_coordinates:
        if(index == 2):
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
        index+= 1


    time.sleep(5)
