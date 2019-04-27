#! /usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
import os
import cloudconvert

import sys
import pyaudio


def talk(words):
    print(words)
    os.system("say "+words)


talk("Hellow")


def recognize():
    r = sr.Recognizer()
    talk("Talk something")
    with sr.Microphone() as source:
        print('Say something')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        usertext = r.recognize_google(audio, language="ru_RU").lower()
        print(format(usertext))
    except sr.UnknownValueError:
        print("Скаже еще")
        usertext = recognize()

    return usertext

while True:
    recognize()
