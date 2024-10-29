"""
Your program should:
1. Read in the data.
2. Categorize the songs by artist, like this:
1. Create one empty folder per artist.
2. Create one blank text file per song by that artist in the relevant folder.
The file name of the text
file should be the name of the song._summary_
"""

import os
import time
import csv

os.system("cls")

if not os.path.exists("songs"):
    os.mkdir("songs")
COUNT = 0
with open("100MostStreamedSongs.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rank = row["Rank"]
        streams = row["Streams"]
        artist = row["Artist(s)"]
        song = row["Song"]
        date = row["Date published"]
        artist_dir = os.path.join("songs", artist)
        if not os.path.exists(artist_dir):
            os.mkdir(artist_dir)
        with open(os.path.join(artist_dir, f"{song}_summary.txt"), "w", encoding="utf-8") as file:
            file.write(
                f"Artist: {artist}\n"
                f"Song: {song}\n"
                f"Ranking: {rank}\n"
                f"Streams: {streams}\n"
                f"Date Published: {date}"
            )
        print(f"{song} by {artist} has been saved")
        COUNT += 1
        print("Please wait")
        print("Saving"+"."* COUNT)
        time.sleep(0.3)
        os.system("cls")
os.system("cls")
print("All songs have been saved!".center(55,"*"))
time.sleep(2)
