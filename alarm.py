import time
import webbrowser
from datetime import datetime

# YouTube link
youtube_url = "https://youtu.be/6R4S_-vgUEw?si=Fnm1t6PyDUq823QW"

# Flag to ensure the video plays only once at 1:00 AM
video_played = False

print("Alarm is set for 1:00 AM. Waiting...")

while True:
    # Get current time
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    # Check for 01:00 AM and only play once
    if current_time == "01:00" and not video_played:
        print("It's 1:00 AM! Opening YouTube...")
        webbrowser.open(youtube_url)
        video_played = True

    # Reset the flag after 1:01 AM so it can work again the next day
    if current_time == "01:01":
        video_played = False

    # Sleep to avoid checking every millisecond (saves CPU)
    time.sleep(30)
