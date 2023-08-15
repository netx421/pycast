import os
import time
import subprocess
from threading import Thread
from pyfiglet import Figlet
from moviepy.editor import *
import sys
import pyautogui

def display_banner():
    custom_fig = Figlet(font='slant')
    banner = custom_fig.renderText("PY-CAST x421")
    print(banner)

def record_screen_with_audio(duration=10):

    screen_width, screen_height = pyautogui.size()


    original_mouse_position = pyautogui.position()


    pyautogui.moveTo(0, 0)


    temp_file = "temp.mp4"


    def countdown_timer(duration):
        for i in range(duration, 0, -1):
            print(f"\rRecording ends in {i} seconds...   ", end="")
            time.sleep(1)
        print("\rRecording completed.                 ")


    ffmpeg_cmd = (
        f"ffmpeg -y -f x11grab -s {screen_width}x{screen_height} -i :0.0 "
        f"-f alsa -ac 2 -i default -t {duration} -c:v libx264 -c:a aac -strict experimental -r 30 {temp_file} 2>&1"
    )


    countdown_thread = Thread(target=countdown_timer, args=(duration,))
    countdown_thread.start()


    recording_process = subprocess.Popen(ffmpeg_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


    while recording_process.poll() is None:
        output = recording_process.stdout.readline().decode().strip()
        if output.startswith("frame="):
            sys.stdout.write(f"\r{output}")
            sys.stdout.flush()


    pyautogui.moveTo(original_mouse_position.x, original_mouse_position.y)


    video_clip = VideoFileClip(temp_file)
    output_filename = "captured_video.mp4"  # Set your fixed output filename here
    video_clip.write_videofile(output_filename, codec="libx264")


    video_clip.close()
    os.remove(temp_file)

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_banner()

        print("Screen Recording Application")
        print("---------------------------")
        print("1. Record Screen with Audio")
        print("2. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            display_banner()
            record_duration = int(input("Enter record duration (seconds): "))
            print("Recording started...")
            record_screen_with_audio(duration=record_duration)
            print("Press Enter to make a new recording.")
            input()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
## netx421@proton.me
## https://searchtec.tech


