import pyautogui
import time

# Coordinates of where to click (x, y) Last Three are play, assault, eula
click_coordinates = [(1908, 658), (2376, 967), (2572, 1398), (2503, 1257)] # Replace with your coordinates
org_coordinates = [(132, 331), (855, 968) ,(1051, 1398) ,(989, 1250)]
fk_coordinates = [(1717, 1323),(363, 193),(842,892),(235,1140),(1028,772),(855,965),(1051, 1398) ,(989, 1250)]
# Time delay between actions
delay = 1

# Start the script with a delay
time.sleep(2)
assault_delay = 6

# Main loop to click repeatedly
while True:
    index = 0
    for coord in fk_coordinates:
        # Wait for save black screen to leave
        if(index == 1):
            time.sleep(2.5)

        # Wait for units to load into battlefield before clicking assault
        if(index == 6):
            time.sleep(assault_delay)
        
        # Go to current coordinate and click, and wait delay set seconds
        pyautogui.moveTo(coord)
        pyautogui.click()
        time.sleep(delay)

        # If we're in the EURLA coordinate, we iterate throught all coordinates to start a new battle.
        if(index == 7):
            for coord in fk_coordinates:
                if(index == 2):
                    time.sleep(assault_delay)
                pyautogui.moveTo(coord)
                pyautogui.click()
                time.sleep(delay)
        
        index+= 1


    time.sleep(5)
