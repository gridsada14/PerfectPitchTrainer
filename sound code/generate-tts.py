from IPython.display import Audio
import gtts
from gtts import gTTS

# language code : ja = japan, th = thai, en = english
tts = gTTS('สวัสดีครับ', lang='th') 
tts.save('speech.mp3')