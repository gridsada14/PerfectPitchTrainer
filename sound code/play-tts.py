import time
from pygame import mixer

mixer.init()
mixer.music.load('sound code\speech.mp3')
print('Ready')
mixer.music.play()
while mixer.music.get_busy():   # wait music finish playing beffore close.
    time.sleep(1)

