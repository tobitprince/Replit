"""
This module plays a sound
"""
import os
import time
import sys
import pygame

pygame.mixer.pre_init()
# pygame.init() is not necessary, so you can remove this line
pygame.mixer.init()
sound = pygame.mixer.Sound("audio.wav")
sound.play()
pygame.mixer.pause()


def pause():
    """_summary_
    """
    pygame.mixer.pause()


pause()


def play():
    """_summary_

    Returns:
        _type_: _description_
    """
    # Play the sound
    pygame.mixer.unpause()
    while True:
        stop_playback = int(
            input("Press 2 anytime to pause playback and go back to the menu: ")
        )
        if stop_playback == 2:
            pause()
            return  # let's go back from this play() subroutine
        continue


while True:
    os.system("cls")
    print("🎵 MyPOD Music Player ")
    time.sleep(1)
    print("Press 1 to Play")
    print("Press 2 to Exit")
    print("Press anything else to see the menu again")
    userInput = int(input())
    if userInput == 1:
        print("Playing some proper tunes!")
        play()
    if userInput == 2:
        sys.exit()
    continue
