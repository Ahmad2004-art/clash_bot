import os
import pyautogui
import time
import win32api
import win32con

# Path to your Clash of Clans shortcut
shortcut_path = r"C:\Users\USER\Desktop\clash_bot\Clash of Clans.lnk"


# Open the shortcut
os.startfile(shortcut_path)

print("Clash of Clans is launching...")


print("Waiting for 55 seconds...")
time.sleep(10)
def scroll_down_with_ctrl(duration_sec=3, scroll_amount=-120, scroll_interval=0.2):
    pyautogui.keyDown('ctrl')  # Hold Ctrl
    start_time = time.time()
    
    while time.time() - start_time < duration_sec:
        # Scroll down with mouse wheel event
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, scroll_amount, 0)
        time.sleep(scroll_interval)
    
    pyautogui.keyUp('ctrl')    # Release Ctrl

print("Starting Ctrl + scroll down for 4 seconds...")
scroll_down_with_ctrl()
print("Done.")

x, y = pyautogui.position()

# Press and hold left mouse button
pyautogui.mouseDown(button='left')

# Move mouse left and up by ~3 cm (110 pixels) **while holding the button**
pyautogui.moveTo(x - 110, y - 110, duration=2.2)  # move over 2 seconds

# Release left mouse button after moving
pyautogui.mouseUp(button='left')

print("Held left mouse, moved left-up ~3 cm while holding, then released.")



import pyautogui
import time

kis = 0

for ext in range(1000):
    print(f"EXT loop {ext + 1}/100")

    for outer_loop in range(6):
        print(f"  Outer loop {outer_loop + 1}/10")

        for i in range(4):
            print(f"    Inner loop {i + 1}/5")

            # Press space
            pyautogui.press('space')
            time.sleep(2)

            # Press f
            pyautogui.press('f')
            time.sleep(6)

            # Hold w then c
            time.sleep(0.5)
            pyautogui.keyDown('w')
            time.sleep(2)
            pyautogui.keyUp('w')
            pyautogui.keyDown('c')
            time.sleep(1)
            pyautogui.keyUp('c')
            
        
            # Hold e for 5 seconds
            pyautogui.keyDown('e')
            time.sleep(5)
            pyautogui.keyUp('e')

            #hold R then e
            time.sleep(0.5)
            pyautogui.keyDown('r')
            time.sleep(1)
            pyautogui.keyUp('r')
            

            # Hold e for 5 seconds
            pyautogui.keyDown('e')
            time.sleep(5)
            pyautogui.keyUp('e')

            #hold t then e
            time.sleep(0.5)
            pyautogui.keyDown('t')
            time.sleep(1)
            pyautogui.keyUp('t')
            

            # Hold e for 5 seconds
            pyautogui.keyDown('e')
            time.sleep(1)
            pyautogui.keyUp('e')

            #hold u then e
            time.sleep(0.5)
            pyautogui.keyDown('u')
            time.sleep(1)
            pyautogui.keyUp('u')
            

            # Hold e for 5 seconds
            pyautogui.keyDown('e')
            time.sleep(1)
            pyautogui.keyUp('e')
            
             # Hold e for 5 seconds
            pyautogui.keyDown('o')
            time.sleep(1)
            pyautogui.keyUp('o')

            # Press sequence with timing
            for key in ['i', 'e', 'r', 'o', 't', 'o', 'z', 'o', 'u', 'o', 'p']:
                if key in ['w', 'r', 't', 'z', 'u', 'i', 'p']:
                    pyautogui.keyDown(key)
                    time.sleep(1)
                    pyautogui.keyUp(key)
                else:
                    pyautogui.press(key)
                    time.sleep(0.1)

            # Press a, s, d multiple times
            for _ in range(4):
                pyautogui.press('a')
                time.sleep(0.1)
            for _ in range(4):
                pyautogui.press('s')
                time.sleep(0.1)
            for _ in range(3):
                pyautogui.press('d')
                time.sleep(0.1)

            # Hold t, z, u, i each for 1 second
            for key in ['t', 'z', 'u', 'i']:
                pyautogui.keyDown(key)
                time.sleep(1)
                pyautogui.keyUp(key)

            print("    Waiting 2 minutes before pressing f...")
            time.sleep(70)

            # Press f and g, then hold h
            pyautogui.press('f')
            time.sleep(2)
            pyautogui.press('g')
            time.sleep(2)
            pyautogui.keyDown('h')
            time.sleep(1)
            pyautogui.keyUp('h')
            time.sleep(10)

        print("  Outer loop finished")

        # Alternate sequences
        sequence1 = ['f', 'j', 'k', 'l']
        sequence2 = ['f', 'j', 'y', 'l']
        sequence = sequence1 if kis % 2 == 0 else sequence2

        print(f"  Sequence loop {kis + 1} running sequence: {sequence}")
        for key in sequence:
            pyautogui.keyDown(key)
            time.sleep(1)
            pyautogui.keyUp(key)

        kis += 1

    time.sleep(5)
    time.sleep(5)
    def search_and_click(image_path):
        location = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)
        if location:
            pyautogui.click(location)
            return True
        return False

    def main():
        image_path = r"C:\Users\USER\Desktop\clash_bot\wall.png"
   
        for _ in range(8):
            found = search_and_click(image_path)
            time.sleep(3)
            if found:
                pyautogui.press('h')
                pyautogui.press('v')
                time.sleep(3)
            else:
                print("Image not found during b v x sequence")

   
        for _ in range(8):
            found = search_and_click(image_path)
            time.sleep(3)
            if found:
                pyautogui.press('n')
                pyautogui.press('v')
                time.sleep(3)
            else:
                print("Image not found during n v x sequence")


    if __name__ == "__main__":
        main()

