from gtts import gTTS
from playsound import playsound

mess = input("Enter your message: ")
t1 = gTTS(mess)
t1.save("mess.mp3")
playsound("mess.mp3")
