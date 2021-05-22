import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random 
import price_tracker

#Initializing Speech Recognition variables 
engine = pyttsx3.init('sapi5') # object creation
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('rate', 175)     # setting up new voice rate; Default is 200
engine.setProperty('voice', voices[1].id) #changing voices[index] change voice tune o for male and 1 for female

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishMe(name):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+name)

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+name)

    else:
        speak("Good Evening! "+name)
    speak("Hi, Jarvis Here, How may I help You?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm Listening...")
        r.energy_threshold=800
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Okay! ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'your-password')
    server.sendmail('email@gmail.com', to, content)
    server.close()

def listenCommand():
    while True:
        query = takeCommand().lower()
        # Change the browser path according to your PC
        web_browser_path= "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
        if "bye" in query:
            speak("Thank You Sir, have a nice day")
            exit()
        if 'open youtube' in query:
            webbrowser.get(web_browser_path).open("youtube.com")

        elif 'open g n e website' in query:
            webbrowser.get(web_browser_path).open("www.gndec.ac.in")

        elif 'open it department website' in query:
            webbrowser.get(web_browser_path).open("it.gndec.ac.in")

        elif 'open google' in query:
            webbrowser.get(web_browser_path).open("google.com")

        elif 'open w3schools' in query:
            webbrowser.get(web_browser_path).open("w3schools.com")

        elif 'the weather' in query:
            webbrowser.get(web_browser_path).open("https://www.google.com/search?q=weather")

        elif 'open notepad' in query:
            os.system('notepad')

        elif 'open calculator' in query:
            os.system('start Calculator:')

        elif 'open edge' in query:
            codePath = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
            os.startfile(codePath)

        elif 'open gallery' in query:
            codePath = "D://Pins"
            os.startfile(codePath)
        
        elif 'play music' in query:
            music_dir = 'D://Music'
            songs = os.listdir(music_dir)
            randomsongs = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomsongs))
        
        elif query.startswith('google'):
            speak('Searching google...')
            query1 = query.replace("google ", "")
            query2 = query1.replace(" ","+")
            webbrowser.get(web_browser_path).open(f"https://www.youtube.com/search?q={query2}")

        elif query.startswith('youtube'):
            speak('Searching YouTube...')
            query1 = query.replace("youtube ", "")
            query2 = query1.replace(" ","+")
            webbrowser.get(web_browser_path).open(f"https://www.youtube.com/results?search_query={query2}")

        elif query.startswith('wikipedia'):
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif query.startswith('translate'):
            query1 = query.replace(" ","+")
            webbrowser.get(web_browser_path).open(f"https://www.google.com/search?q={query1}")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'date and time' in query:
            strDate = datetime.datetime.now.strftime("%m/%d/%Y, %H:%M:%S")
            speak(f"Sir, the date and time is {strDate}")
            
        elif 'open code' in query:
            codePath = "f://project//jarvis.py"
            os.startfile(codePath)

        elif 'price tracker' in query:
            try:
                result = price_tracker.run()
                speak(result)
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to run price tracker!")

        elif 'send email to' in query:
            try:
                speak("To whom? ")
                to = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! I am not able to send this email")
        elif "none" in query:
            continue
        else:
            speak('I\'m not aware, Should I Search it on google?')
            cmd = takeCommand()
            if "yes" in cmd:
                speak('Googling'+query)
                query2 = query.replace(" ", "+")
                webbrowser.get(web_browser_path).open(f"https://www.google.com/search?q={query2}")
        speak("Anything else? ")

# Main function
if __name__ == '__main__':
    wishMe("") # Give your name
    listenCommand()