# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import speech_recognition as sr

with sr.Microphone() as source:
    print("say something")
    audio = sr.Recognizer().listen(source)
    
try :
    text = sr.Recognizer().recognize_google(audio)
    print("you said",text)
except:
    print("Transaction failed")