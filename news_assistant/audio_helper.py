from gtts import gTTS
import pygame


def text_to_mp3(text):
    audio = gTTS(text=text, lang="en", slow=False)
    audio.save("text.mp3")


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue


if __name__ == "__main__":
    file = "story"
    story = open(file + ".txt")
    text_to_mp3(story.read())
    story.close()
    play_audio("text.mp3")

