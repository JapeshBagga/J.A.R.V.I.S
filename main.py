import cv2
import numpy as np
import face_recognition
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

#Initializing Speech Recognition variables 
engine = pyttsx3.init('sapi5') # object creation
voices = engine.getProperty('voices') #getting details of current voice
engine.setProperty('rate', 185)     # setting up new voice rate; Default is 200
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
    speak("Jarvis Here, Please tell me, how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Okay")
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

def giveCommand():
    while True:
        query = takeCommand().lower()
        if 'bye' or 'turn off' or 'exit' in query:
            speak("Thank You Sir, have a nice day")
            exit()
            break
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")

        elif 'open gne website' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("www.gndec.ac.in")

        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")

        elif 'open w3schools' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("w3schools.com")

        elif 'the weather' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/search?q=weather")

        elif 'open notepad' in query:
            os.system('notepad')

        elif 'open calculator' in query:
            os.system('start Calculator:')

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)

        elif 'open gallery' in query:
            codePath = "D:\\Pins"
            os.startfile(codePath)
        
        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            randomsongs = random.choice(songs)
            os.startfile(os.path.join(music_dir, randomsongs))
        
        elif query.startswith('google'):
            speak('Searching google...')
            query1 = query.replace("google ", "")
            query2 = query1.replace(" ","+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query2}")

        elif query.startswith('translate'):
            query1 = query.replace(" ","+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query1}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "f:\\daman project\\jarvis.py"
            os.startfile(codePath)
        
        elif 'send email to' or 'email' in query:
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
        else:
            speak('Searching google...')
            query2 = query.replace(" ", "+")
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(f"https://www.google.com/search?q={query2}")

        speak("Anything else? ")

#Initializing Face Recognition variables 
#Face Recognization Code
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('C:/Users/japba/Desktop/Jarvis1/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()

        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

        #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
        # def captureScreen(bbox=(300,300,690+300,530+300)):
        #     capScr = np.array(ImageGrab.grab(bbox))
        #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
        #     return capScr

 
if __name__ == "__main__":
    path = 'C:/Users/japba/Desktop/Jarvis1/Training_images'
    images = []
    classNames = []
    myList = os.listdir(path)
    #print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findEncodings(images)
    cap = cv2.VideoCapture(0)
    print("Recognizing Face...")

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                #markAttendance(name)
                print("Matched")
                wishMe(name)
                giveCommand()

        #cv2.imshow('Webcam', img)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #   break
   

