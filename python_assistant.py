import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hay Madhav, Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shyamendra99@gmail.com', 'g_mail.com@123')
    server.sendmail('sengarsp98@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("Okay, i'm launching it for you.")

        elif 'google' in query:
            webbrowser.open("www.google.com")
            speak("Okay, i'm launching it for you.")

        elif ("chrome" in query):
            speak("Okay, i'm launching it for you.")
            os.system("chrome")
        elif ("date" in query):
            os.system("date")
            speak("Okay, i'm launching it for you.")
        elif ("Notepad" in query):
            os.system("notepad")
            speak("Okay, i'm launching it for you.")
        elif "virtualbox" in query:
            os.system("virtualbox")
            speak("Okay, i'm launching it for you.")
        elif "open spotify" in query:
            os.system("start spotify")
            speak("Okay, i'm launching it for you.")
        elif ("open vlc" in query):
            os.system("start vlc")
            speak("Okay, i'm launching it for you.")
        elif ("window media player" in query):
            os.system("wmplayer")
            speak("Okay, i'm launching it for you.")
        elif ("excel" in query):
            os.system("excel")
            speak("Okay, i'm launching it for you.")
        elif ("word" in query):
            os.system("winword")
            speak("Okay, i'm launching it for you.")
        elif "open PowerPoint" in query or "open ppt" in query or "open powerpoint" in query:
            os.system("start powerpnt")
            speak("Okay, i'm launching it for you.")
        elif (("open virtual" in query) and ("box" in query)) or ("vbox" in query):
            os.system("start virtualbox")
            speak("Okay, i'm launching it for you.")
        elif "open email" in query:
            webbrowser.open("https://mail.google.com")
            speak("Okay, i'm launching it for you.")
        elif ("open YouTube" in query) or ("open youtube" in query):
            webbrowser.open("https://www.youtube.com")
        elif ("open Telegram" in query) or ("tele" in query):
            os.system("start telegram")
        elif ("video punjabi songs" in query):
            webbrowser.open("https://www.youtube.com/watch?v=GjvEzkg27F4&list=RDGjvEzkg27F4&start_radio=1")
            speak("Okay, i'm playing it for you.")
        elif ("video bollywood songs" in query):
            webbrowser.open("https://www.youtube.com/watch?v=6wNFJIbTxNk&list=PLO7-VO1D0_6NmK47v6tpOcxurcxdW-hZa")
            speak("Okay, i'm playing it for you.")
        elif ("video english songs" in query):
            webbrowser.open("https://www.youtube.com/watch?v=zlJDTxahav0&list=PL6CTrxW12Bre4kny-OhqOEQwNjso0VKPc")
            speak("Okay, i'm playing it for you.")
        elif ("audio bollywood songs" in query):
            webbrowser.open("https://gaana.com/playlist/gaana-dj-bollywood-high-voltage")
            speak("Okay, i'm playing it for you.")
        elif ("audio punjabi songs" in query):
            webbrowser.open("https://gaana.com/playlist/gaana-dj-trending-around-you")
            speak("Okay, i'm playing it for you.")
        elif ("audio english songs" in query):
            webbrowser.open("https://gaana.com/playlist/gaana-dj-international-weekly-hot-20")
            speak("Okay, i'm playing it for you.")
        elif ("open WhatsApp" in query):
            os.system("start whatsapp")
            speak("Okay, i'm launching it for you.")

        elif "email to madhav" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "madhavku248@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend madhav bhai. I am not able to send this email")
        elif (("exit" in query) or ("stop" in query) or ("quit" in query)) or (("done" in query) or ("out" in query)):
            speak("Thank you for using it. Have a good day.")
            break
        elif (("thank you" in query) or ("thanks" in query)):
            speak("it's my job.")
            speak("Thank you for using it. Have a good day.")
    
