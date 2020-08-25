import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('22WY98-272495KEAV')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)
def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')
greetMe()
speak('Hello Sir, I am your digital assistant sweety')
speak('How may I help you?')
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    return query
if __name__ == '__main__':
    while True:
        query = myCommand();
        query = query.lower()
        if 'open youtube' in query:
            speak('okay,opening youtube')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay,opening gmail')
            webbrowser.open('www.gmail.com')
        elif 'open facebook' in query:
            speak('okay,opening facebook')
            webbrowser.open('www.facebook.com')
        elif 'open control panel' in query:
            speak('okay,opening control panel')
            os.startfile('C:\\Users\\Default\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk')
        elif 'Notepad' in query:
            speak('okay,opening Notepad')
            os.startfile('C:\\Users\\Default\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk')
        elif 'open command prompt' in query:
            speak('okay,opening command prompt')
            os.startfile('C:\\Users\\Default\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\command prompt.lnk')
        elif 'who made you' in query:
            speak('I was made by pujitha')
        elif "play movie" in query:
            speak("playing movie")
            Movie_folder = 'D:\\movies\\'
            movie = ['MMC','SAV','AVL','BH']
            random_movie = Movie_folder + random.choice(movie) + '.mkv'
            os.system(random_movie)
            speak('okay,here is your movie enjoy')
        elif "what doing" in query or 'how are ystMsgs' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'hello' in query:
            speak('Hey!!,Hello Sir')
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'play music' in query:
            music_folder = 'C:\\Users\\puj\\Music\\'
            music = ['Dj','L-D','Fri','Rb']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
            speak('Okay, here is your music! Enjoy!')
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                webbrowser.open('www.google.com')
        speak('Next Command! Sir!')
        
