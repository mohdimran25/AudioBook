"""
gtts module is used for conversion of text into audio
NOTE: It can only read text files (not supported PDF files)
usecase:
from gtts import gTTS
 tts = gTTS('hello')
 tts.save('hello.mp3')

"""


from gtts import gTTS
import os 
with open("sample.txt","r") as file:
    sample = file.read()
    language = 'en'
    audio = gTTS(text=sample,lang=language,slow=False)
    audio.save('sample.mp3')

os.system('sample.mp3') 