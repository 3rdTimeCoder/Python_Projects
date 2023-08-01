from gtts import gTTS
import os

story = open('story.txt')
audio = gTTS(text=story.read(), lang="en", slow=False)
story.close()

audio.save("story.mp3")
os.system("start story.mp3")
print("Done")