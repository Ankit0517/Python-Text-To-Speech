import os
from gtts import gTTS 
x = input("Enter the text   ")
lang = 'hi'
speech_obj = gTTS(text = x, lang = lang, slow = False)
speech_obj.save("audio.wav")
os.system("start audio.wav") 
 

