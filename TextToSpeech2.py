import os
from gtts import gTTS
import PyPDF2 
pdf = open(r'LOCATION\NAME.pdf', 'rb')
pr = PyPDF2.PdfFileReader(pdf) 
pageObj = pr.getPage(10)
x = pageObj.extractText()
speech_obj = gTTS(text = x,slow = False)
speech_obj.save("audio1.wav")
os.system("start audio1.wav") 