# references
from references import *

def log_read_files(output_item, value):
    if LOG_READ_FILES:
        if output_item == 'artist':
            print '= = = = = = = = ='
            print value
            print '= = = = = = = = ='
        elif output_item == 'album':
            print '# # # # # # # # #'
            print value
            print '# # # # # # # # #'
        elif output_item in ['padding', 'track']:
            print value

def output_track(album, artist, file):
    pass
