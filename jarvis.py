from datetime import datetime          # datetime module supplies classes for manipulating dates and times
import subprocess                      # subprocess module allows you to spawn new processes

import speech_recognition as sr        # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..



# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio)
print(Query)


# Run Application with Voice Command Function
def get_app(Q):
    if Q == "time":
        print(datetime.now())
    elif Q == "notepad":
        subprocess.call(['Notepad.exe'])
    elif Q == "calculator":
        subprocess.call(['calc.exe'])
    elif Q == "sticky note":
        subprocess.call(['StikyNot.exe'])
    elif Q == "shell":
        subprocess.call(['powershell.exe'])
    elif Q == "paint":
        subprocess.call(['mspaint.exe'])
    elif Q == "cmd":
        subprocess.call(['cmd.exe'])
    elif Q == "File Explorer":
        subprocess.call(['explorer.exe'])
    elif Q == "Browser":
        subprocess.call(['C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'])
    else:
        print("Sorry ! Try Again")
    return


get_app(Query)
