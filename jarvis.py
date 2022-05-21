import pyttsx3
import speech_recognition as sr
import datetime
# import time
import wikipedia
import webbrowser
import os
import random
import pywhatkit
# import pyjokes
import playsound
# import google_alerts
import pyautogui
import weather_forecast
# from pygame import mixer

file1 = 'access_denied.mp3'
file2 = 'jarvis_access.mp3'
file3 = 'jarvis_beep.mp3'
file4 = 'jarvis_disconnected.mp3'
file5 = 'password.mp3'
file6 = 'welcome_home_jarvis.mp3'


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("volume", 1.0)
engine.setProperty("rate", 160)
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def putPassword():
    count = 0
    while count < 3:
        passWord = "admin"
        playsound.playsound(file5)
        givenPass = takeCommand()

        if givenPass == passWord:
            playsound.playsound(file2)
            break

        else:
            playsound.playsound(file1)
            count = count + 1
            while count == 3:
                speak("Sorry Sir. It seems you are not the owner of this machine. Nice try anyway!")
                playsound.playsound(file4)
                exit()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, Sir. Please tell me how may I help you.")



def takeCommand():
    r = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold = 300
        # r.pause_threshold = 0.5
        playsound.playsound(file3)
        print("listening... ")
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print("User said:", query)
            return query
        except:
            # print("Please, say again.")
            # speak("Please, say again.")
            # takeCommand()

            speak("Sorry Sir. You didn't say anything. Thanks for your time.")
            playsound.playsound(file4)
            exit()


def ytSpecial():
    engine.runAndWait()
    ytQuery = takeCommand().lower()
    speak("Sure Sir, as you wish.")

    if "pause" in ytQuery:
        pyautogui.press("space")
        return

    elif "play next" in ytQuery:
        pyautogui.hotkey("shift", "n")
        return

    elif "full screen" in ytQuery:
        pyautogui.press("f")
        return

    elif "theatre mode" in ytQuery:
        pyautogui.press("t")
        return

    else:
        return runJarvis()


def runJarvis():
    query = takeCommand().lower()


    if "wiki" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=4)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")

    elif "date" in query:
        strDate = datetime.date.today().strftime("%b-%d-%Y")
        print(f"Sir, today is {strDate}")
        speak(f"Sir, today is {strDate}")

    elif "weather in" in query:
        place = query.replace("weather in", "")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.date.today().strftime("%Y-%m-%d")
        weather_forecast.forecast(place, time, date, forecast="daily")

    elif "open youtube" in query:
        speak("opening youtube")
        webbrowser.open("youtube.com")

    elif "open google" in query:
        speak("opening google")
        webbrowser.open("google.com")

    elif "close" in query:
        speak("closing current window")
        pyautogui.hotkey("alt", "f4")

    elif "play music" in query:
        speak("Sure Sir, I am opening your music folder")
        music_dir = "I:\\Songs"
        songs = os.listdir(music_dir)
        n = random.randint(0, (len(songs)-1))
        print(f"Playing {songs[n]}")
        speak(f"Playing {songs[n]}")
        os.startfile(os.path.join(music_dir, songs[n]))

    elif "play" in query:
        query = query.replace("play", "")
        print(f"Playing {query}")
        speak(f"Playing {query}")
        pywhatkit.playonyt(query)

    elif "google" in query:
        query = query.replace("google", "")
        print(f"Google is searching about {query}")
        speak(f"Google is searching about {query}")
        pywhatkit.search(query)

    elif "handwriting" in query:
        speak("Sir, please say the text to create a handwritten note.")
        textToWrite = takeCommand()
        pywhatkit.text_to_handwriting(textToWrite, rgb=[0, 0, 0])

    elif "whatsapp" in query:
        speak("Sure Sir, I am preparing WhatsApp for you.")
        speak("Sir, please enter phone number of recipient.")
        onlyNumber = str(takeCommand())
        codeWithNumber = "+91" + onlyNumber
        speak("Sir, enter the time when i will send the message.")
        speak("enter sending hour")
        sendingHourStr = takeCommand()
        sendingHour = int(sendingHourStr)
        speak("enter sending minute")
        sendingMinStr = takeCommand()
        sendingMin = int(sendingMinStr)
        speak("enter AM or PM")
        defineAMorPM = str(takeCommand().lower())
        if sendingHour < 12 and defineAMorPM == "pm":
            sendingHour12 = sendingHour + 12
        else:
            sendingHour12 = sendingHour
        # sendingTime = input("Time (Hour, Minute): ")
        # speak(f"Sir, your message will be sent at {sendingHour}:{sendingMin} {defineAMorPM}")
        print(f"Message Sending Time is {sendingHour}:{sendingMin} {defineAMorPM}")
        speak("Sir, please say what to send.")
        sendMessage = takeCommand()
        speak(f"Sir, I will send your message to this number {onlyNumber} at {sendingHour}:{sendingMin} {defineAMorPM}.")
        pywhatkit.sendwhatmsg(codeWithNumber, sendMessage, sendingHour12,sendingMin)


    elif "open pycharm" in query:
        speak("opening pycharm")
        codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
        os.startfile(codePath)

    elif "open chrome" in query:
        speak("opening google chrome")
        codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)

    elif "open sublime" in query:
        speak("opening sublime text 3")
        codePath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(codePath)

    # elif "joke" in query:
        # randJoke = pyjokes.get_joke(category="all")
        # print(randJoke)
        # speak(randJoke)

    elif "bye" in query:
        speak("Thanks for your time, Sir. Hope to see you again!")
        playsound.playsound(file4)
        exit()

    else:
        speak(f"Sir, you said {query}")

    return runJarvis()


playsound.playsound(file6)
putPassword()
wishMe()
# time.sleep(1)
# speak("listening")
runJarvis()