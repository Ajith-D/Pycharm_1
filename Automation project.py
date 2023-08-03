import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    """
    12:00 - noon
    1:00 pm - morning / 13:00 - afternoon
    18:00 - evening
    """
    if hour >= 0 and hour <= 12:
        speak("Good Morning Ajith")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon Ajith")
    else:
        speak("Good Evening Ajith")

    speak("Let me know How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your Voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Hey! You said: {query}\n")
    except Exception as ex:
        print("Ajith, Can you say that again?")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajith.2007@gmail.com', 'automation')
    server.sendmail('ajith.d2007@gmail.com', to, content)
    server.close()





