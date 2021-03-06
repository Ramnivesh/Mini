# Importing required modules

# importing pyttsx3

# pyttsx3 is used to TEXT TO SPEECH CONVERSION

import pyttsx3

# importing speech_recognition

# speech_recognition is used to RECOGNISE YOUR VOICE

import speech_recognition as sr

# importing os module

# os is linking

import os


# creating take_commands() function which

# can take some audio, Recognize and return

# if there are not any errors

def take_commands():

    # initializing speech_recognition

    r = sr.Recognizer()

    # opening physical microphone of computer

    with sr.Microphone() as source:

        print('Listening')

        r.pause_threshold = 0.7

        # storing audio/sound to audio variable

        audio = r.listen(source)

        try:

            print("Recognizing")

            # Recognizing audio using google api

            Query = r.recognize_google(audio)

            print("the query is printed='", Query, "'")

        except Exception as e:

            print(e)

            print("Say that again sir")

            # returning none if there are errors

            return "None"

    # returning audio as text

    import time

    time.sleep(2)

    return Query


# creating Speak() function to giving Speaking power

# to our voice assistant

def Speak(audio):

    # initializing pyttsx3 module

    engine = pyttsx3.init()

    # anything we pass inside engine.say(),

    # will be spoken by our voice assistant

    engine.say(audio)

    engine.runAndWait()

Speak("Do you want to Restart your computer sir?")

while True:

    command = take_commands()

    if "no" in command:

        Speak("Thank you I will not restart the computer")

        break

    if "yes" in command:

        # Shutting down


        Speak("Restarting the computer")

        os.system("shutdown /r /t 30")

        break

Speak("Can't Recognise your voice, Say that again")
