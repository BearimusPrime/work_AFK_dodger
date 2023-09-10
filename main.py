import pyautogui
import time

def move_mouse_in_square(square_size):
    # Get the screen resolution
    screen_width, screen_height = pyautogui.size()

    # Calculate the starting position of the square
    start_x = (screen_width - square_size) // 2
    start_y = (screen_height - square_size) // 2

    # Move the mouse to the starting position
    pyautogui.moveTo(start_x, start_y, duration=0.5)

    # Move the mouse in a square
    pyautogui.dragRel(square_size, 0, duration=0.5)  # Move right
    pyautogui.dragRel(0, square_size, duration=0.5)  # Move down
    pyautogui.dragRel(-square_size, 0, duration=0.5)  # Move left
    pyautogui.dragRel(0, -square_size, duration=0.5)  # Move up

    # Optional: Return the mouse to the starting position
    pyautogui.moveTo(start_x, start_y, duration=0.5)

    # Pause for a while before exiting
    time.sleep(2)

def main():
    # Call the function with desired square size
    square_size = 400
    move_mouse_in_square(square_size)

if __name__ == '__main__':
    while True:
        main()
