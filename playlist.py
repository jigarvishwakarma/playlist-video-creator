#It works
from moviepy.editor import *
import random
import pafy
import datetime
from pytube import Playlist
import os, glob
 
SAVE_PATH = os.getcwd()
video_path = str(SAVE_PATH+'/out.png')
#audio_path = str(SAVE_PATH+'/cache/*)

try:
    os.remove(video_path)
    filelist = glob.glob(os.path.join(SAVE_PATH, "*"))
    for f in filelist:
        print(f)
except:
    print("nothing to reset")

# input

list_of_names = []
def pafyd(link,name):
	v = pafy.new(link)
	list_of_names.append(v.title)
	bestaudio = v.getbestaudio()
	bestaudio.download(filepath=str("cache\\"+str(name)+'.m4a'))
	return name

def take_yt_link(value):
    listoflinks = []
    link=""
    while(link==""):
        link=input("Enter YouTube link for "+value+" : ")
        if link=="":
            break
        listoflinks.append(link)
        print("total",len(listoflinks),"songs added")
    return link

link=input("Enter YouTube Playlist link for : ")
playlist = Playlist(link)
listofaudio_clip=[]
for i in range(0,len(playlist)):
    title = pafyd(playlist[i],i)
    audio_clip = AudioFileClip(SAVE_PATH+"\cache\\"+str(title)+".m4a")
    listofaudio_clip.append(audio_clip)

print(list_of_names) 

new_audioclip = concatenate_audioclips(listofaudio_clip)
print(new_audioclip.duration)
new_audioclip.write_audiofile("c1_amv.mp3", fps=44100)

cliptext = TextClip("~\t"+"\n\n~\t".join(list_of_names), font ="Lane", fontsize = 20, color ="white").set_position("center") #.set_duration(new_audioclip.duration).set_fps(10)
video = ImageClip("image.jpg")
image = CompositeVideoClip([video,cliptext])

image.save_frame("out.png")

final_video = ImageClip("out.png").set_audio(new_audioclip).set_duration(new_audioclip.duration).set_fps(10)
 
final_video.write_videofile("play.mp4", codec='libx264', audio_codec="aac")

