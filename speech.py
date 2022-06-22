
from tkinter import *
import speech_recognition as sr
from googletrans import Translator
root=Tk()
root.geometry("600x600")
root.title("Speech Recognizer")
label1=Label(root,text="Language Translater", font=("Bahnschrift Light",15,"bold"))
label1.place(relx=0.5, rely=0.1,anchor=CENTER)
label2=Label(root,text="Enter Text", font=("Bahnschrift Light",10,"bold"))
label2.place(relx=0.2, rely=0.3,anchor=CENTER)
textbox=Text(root, width="30", height="10")
textbox.place(relx=0.2, rely=0.5,anchor=W)
def r_audio():    
    spr=sr.Recognizer()
    with sr.Microphone() as source:
        audio=spr.listen(source)
        voice_data=''
        try:
            voice_data=spr.recognize_google(audio, language='en-in')
        except:
            print("Sorry, Could you repeat that")
        print(voice_data)
r_audio()
root.mainloop()