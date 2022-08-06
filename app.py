from pytube import YouTube
from pytube import Playlist
from sys import argv
import moviepy.editor as mp

link = argv[2]
path = argv[3]
flag = 0
if '-n' in argv[1]:
    flag = 0
if '-p' in argv[1]:
    flag = 1

# single video
if flag == 0:
    yt = YouTube(link)
    yt_download = yt.streams.get_highest_resolution()
    yt_download.download(path)


# playlist video
if flag == 1:
    p = Playlist(link)
    for vid in p.videos:
        temp = vid.streams.get_highest_resolution()
        temp.download(path)
