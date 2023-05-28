from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, vfx
import pyttsx3 
import os
with open("text.txt") as t:
    lines = t.readlines()
text = ''
texts = []
voice = pyttsx3.init()
voice.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
for e in lines:
    if e == '\n':
        texts += [text]
        text = ''
    else:
        text += e
voice.save_to_file(texts[0],"audio1.mp3",'K')
voice.save_to_file(texts[1],"audio2.mp3")
voice.save_to_file(texts[2],"audio3.mp3")
voice.runAndWait()


audio1 = AudioFileClip('audio1.mp3')
audio2 = AudioFileClip('audio2.mp3')
audio3 = AudioFileClip('audio3.mp3')

image1 = ImageClip('Video.png')
image2 = ImageClip('Video-1.png')
image3 = ImageClip('Video-2.png')
clip3 = image3.set_duration(audio3.duration)
clip2 = image2.set_duration(audio2.duration+1)
clip1 = image1.set_duration(audio1.duration+1)
Video1= clip1.set_audio(audio1)
Video2= clip2.set_audio(audio2)
Video3= clip3.set_audio(audio3)
Video_final = concatenate_videoclips([Video1,Video2,Video3])
Video_final.write_videofile('video1.mp4',24)
