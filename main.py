from gtts import gTTS
import os


file_handleer = open("input.text", "r")
myText = file_handleer.read().replace("\n", " ")

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")
file_handleer.close()
os.system("start output.mp3")