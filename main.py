import time
from PIL import ImageGrab
import pyautogui

# Setting a delay before running the program.
print("Welcome to Auto Roulette Bot thingy. Ctrl-C when you can to stop code from executing.")
time.sleep(5)

def startingPoint():
    # "ok" variable is used for iteration, number of attempts.
    ok = 0
    
    # 			IMPORTANT
    # This values of x and y coordinates are temporary set.
    # Same to red, green, blue values.
    # User should set individually in code for every value
    # where the pointer should click or where the color is on the screen.
    value_x = 0
    value_y = 0
    value_r = 0
    value_g = 0
    value_b = 0
    
    # We make sure nothing is on bet.
    pyautogui.click(x=value_x, y=value_y) 
    while True:

        # We're picking up the color of waiting delay.
        px = ImageGrab.grab().load()
        colorRollingDelay = px[value_x, value_y] 
        # DEBUG
        # print(colorRollingDelay)

        # Ensure the color is correct then bet.
        if colorRollingDelay == (value_r, value_g, value_b): 
            ok += 1
            print('"Ok" delaying {} time(s)'.format(ok))
            if ok >= 3:
                print('Clicking...')
                pyautogui.click(x=value_x, y=value_y) # set value of cash button
                pyautogui.click(x=value_x, y=value_y) # bet button
                ok = 0

                # Wait for next round.
                while True:
                    
                    px = ImageGrab.grab().load()
                    colorBetButton = px[value_x, value_y] # bet button color
                    # This can be optimized using more conditions 
                    # and capturing more colors from screen.

                    if colorBetButton == (value_r, value_g, value_b): # win
                        # We break and repeat the start process.
                        # ok += 1
                        print('Win color detected. Continue...')
                        pyautogui.click(x=value_x, y=value_y) # clear cash button
                        # if ok >= 2:
                        #     print("Win. Restarting...")
                        #     ok = 0
                        break
                
                    if colorBetButton == (value_r, value_g, value_b): # lose 
                        # We double the value.
                        ok += 1
                        print('"Lose color" delaying {} time(s)'.format(ok))
                        if ok >= 3:
                            print("Bet lost. Double the value.")
		            pyautogui.click(x=value_x, y=value_y) # double cash
		            time.sleep(3) # let it finish the round
		            pyautogui.click(x=value_x, y=value_y) # bet button
		            ok = 0
		            # Making sure not to double or bet repeatedly losing all.
                            time.sleep(7)
                time.sleep(0.1)
                # break
        time.sleep(0.3)
        # Not sure if I used to many sleeps. Sorry for that :')

startingPoint()
