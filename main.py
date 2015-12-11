# check mp3 bitrate
from check import eval_bitrate

# references
from references import *

# utils
import os
from utils import log_read_files


# go to library
os.chdir(LIBRARY_LOCATION)

# loop through library files
for artist in os.listdir('.'):
    os.chdir(artist)
    log_read_files('artist', artist)
    for album in os.listdir('.'):
        os.chdir(album)
        log_read_files('album', album)
        for file in os.listdir('.'):
            for FILE_TYPE in MUSIC_FILE_TYPES:
                if file.endswith(FILE_TYPE):
                    log_read_files('track', file)
                    eval_bitrate(artist, album, file)
                    break
        os.chdir('..')
    os.chdir('..')
    log_read_files('padding', '')
