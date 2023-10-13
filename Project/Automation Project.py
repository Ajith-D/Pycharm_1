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
    if 0 <= hour <= 12:
        speak("Good Morning Ajith")
    elif 12 <= hour <= 18:
        speak("Good Afternoon Ajith")
    else:
        speak("Good Evening Ajith")

    speak("Let me know How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing your Voice...")
        Query = r.recognize_google(audio, language='en-in')
        print(f"Hey! You said: {Query}\n")

    except Exception:
        print("Ajith, Can you say that again?")
        return "None"

    return Query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ajith.2007@gmail.com', 'automation')
    server.sendmail('ajith.d2007@gmail.com', to, content)
    server.close()



if __name__ == '__main__':
    wishme()

    while True:
        query = take_command().lower()

        if 'open wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)

        if 'open notepad' in query:
            note_path = r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2305.18.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe"
            os.startfile(note_path)

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hey Ajith, the time is {strTime}")

        elif 'open terminal' in query:
            t_path = r"C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\System Tools\Command Prompt.lnk"
            os.startfile(t_path)

        elif 'open Great Learning' in query:
            webbrowser.open("https://www.mygreatlearning.com/academy")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open great learning youtube channels' in query:
            webbrowser.open("https://www.youtube.com/user/beaconelearning")

        elif 'open Linkedin' in query:
            webbrowser.open("www.linkedin.com")

        elif 'email to other friend' in query:
            try:
                speak("What should I send ?")
                content = take_command()
                to = "ajith.d2007@gmail.com"
                sendMail(to, content)
                speak("your email has benn sent successfully")

            except Exception as ex:
                print(ex)
                speak('Unable to send the mail')