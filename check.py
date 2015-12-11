# mp3 metadata library
from eyed3 import mp3

# references
from references import *

# utils
import os
from utils import output_track


def eval_bitrate(artist, album, file):
    if not file.endswith('.mp3'):
        print 'not mp3:', file
    else:
        try:
            track_path = os.path.abspath(file)
            readable_file = open(track_path)
            vbr, bitrate = mp3.Mp3AudioInfo(readable_file, 0, None).bit_rate
            if bitrate < 320:
                print file, bitrate
            readable_file.close()
        except any as e:
            print e, file
