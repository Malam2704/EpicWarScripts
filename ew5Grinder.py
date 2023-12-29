import pyautogui
import time
import keyboard  # You need to install this library using 'pip install keyboard'

# Coordinates of where to click (x, y)
click_coordinates = [(1688,908), #The bottom right flag
                     (1135,217), #The Stage clicking
                     (837,1053), #Yes to Battle
                     (1957,1332),(1145,940),(1142,553),
                     (1642,1145),# The Assault Button
                     (2070,693),(250,1290),(837,1081)]  # Replace with your coordinates

# Time delay between actions
delay = 1
delay_later = 5

# Start the script with a delay
time.sleep(2)

# Variable to control the main loop
running = False

while True:
    if keyboard.is_pressed('h'):  # Start loop when 'H' is pressed
        running = True
        start_time = time.time()  # Start timer
        sped_up = False

    while running:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > 45:  # Check if 50 seconds have passed
            pyautogui.moveTo((1375, 1347))
            pyautogui.click()
            # Reset the timer
            start_time = time.time()
            sped_up = False

        index = 0
        for coord in click_coordinates:           
            if(index >= 3 and index <= 5):
                # print("starting sped up")
                if(sped_up != True):
                    pyautogui.moveTo(coord)
                    pyautogui.click()
                    if(index == 5):
                        sped_up = True
            else:
                pyautogui.moveTo(coord)
                pyautogui.click()
            
            if index > 6:
                time.sleep((delay_later))
            else:
                time.sleep(delay)
            
            index += 1

        time.sleep(5)

        

    time.sleep(0.1)  # To prevent high CPU usage
