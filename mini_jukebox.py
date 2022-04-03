import os
import pygame

def rebuild_library(music):
    path = os.getcwd() + "\\audio\\"
    files = os.listdir(path)
    music = {}
    i = 100
    for x in files:
        fullpath = path + x
        fullpath = fullpath.replace(os.sep, '/')
        music.update({i:fullpath})
        i += 1
    return music

def show_library(music):
    print()
    for key,value in music.items():
        print(str(key)+": "+value.split("/")[-1][:-4])

def main():
    pygame.init()
    music = {}
    music = rebuild_library(music)
    choice = 1000
    while(choice != -1):
        print("0: Stop track")
        print("555: Show library")
        print("999: refresh library")
        print("Enter number:")
        try:
            choice = int(input())
        except:
            print("Invalid input detected...\n")
            continue
        if choice == -1:
            continue
        elif choice == 0:
            pygame.mixer.stop()
        elif choice == 555:
            show_library(music)
        elif choice == 999:
            music = rebuild_library(music)
        else:
            try:
                music_player = pygame.mixer.Sound(music[choice])
                pygame.mixer.stop()
                music_player.play()
            except:
                print("Invalid music choice...\n")
                continue
        print()

if __name__ == "__main__":
    main()