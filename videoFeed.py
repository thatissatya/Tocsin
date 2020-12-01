# Show video feed
import cv2, time, sys
from pynput.keyboard import Key, Controller
import pygame  # For playing sound

keyboard = Controller()
# Finally when video capture is over, release the video capture and destroyAllWindows
def dest(master):
    keyboard.press('q')
    try:
        if cv2.VideoCapture.isOpened():
            try:
                pygame.mixer.music.stop()
            except :
                time.sleep(5)
                master.destroy()
    except :
        try:
            pygame.mixer.music.stop()
            master.destroy()
        except :
            master.destroy()


def destt():
    keyboard.press('q')
    keyboard.release('q')
