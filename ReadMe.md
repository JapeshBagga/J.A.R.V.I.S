# J.A.R.V.I.S (Just A Rather Very Intelligent System)

## About Project 

### Jarvis is a virtual assistant like Siri and Alexa with additional face recognition based secruity mechanism. The assitant recognises speech and face of the user and responds accordingly. 

Various Features and tasks performed by this assistant are:

1. It first wishes and greet the user according to the person recognized by the face recognizer.
2. It can retreive the information from **Wikipedia**.
3. It can report current date and time to the you.
4. It can open Google, Youtube, Stackoverflow, Instagram, Facebook, Tinder and other **social media** apps for you.
5. It can open Python Interpreter(IDLE), Notepad, Calculator and other **System Softwares** for you.
6. It can open code editor or **IDE** like Vs-Code,Code-Blocks and any other IDE etc of your choice.
7. It can **send Email** to the intended user for you.
8. Equipped with **face recognition.**
9. You track prices of the given product from the **E-Commerce** Websites according to the URL mentioned and can also tell it will be in your budget or not according to the settings done for the program.
10. 


## How to Use

To use this project on your system, follow these steps:

1.Clone this repository onto your system by typing the following command on your Command Prompt:
```
git clone https://github.com/JapeshBagga/J.A.R.V.I.S.git
```
followed by:

```
cd J.A.R.V.I.S
```

2. Download all libaries using::
```
pip install -r requirements.txt
```

3.  Now edit the **settings.json** file using your favorite code editor(Example: Sublime text editor, VSCode, Vim).

4. Change ```budget:0```  value to your budget. (Example: ```budget:999```)

5. Replace the link in **URL** with your link. (Example: ```url:'https://www.amazon.in/G731GT-Graphics-i5-9300H-Windows-G731GT-AU022T/dp/B07S36XJ8Q/'```)

6. Change the **user agent** according to your [**user agent**](https://www.google.com/search?q=my+user+agent&oq=my+user&aqs=chrome.1.69i57j0l5.2294j1j7&sourceid=chrome&ie=UTF-8). (Example: ```headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'} ```)

7. Now save the file and run **main.py** by typing the following command on your Command Prompt:

```
python main.py
```

4.

Note: 1. To open code editor of your choice and python interpreter(IDLE) you have to provide
path of your local directories in the source code to avoid error.
2. If there is any error regarding microphone or related to pyttsx3 or speech_recognition module do follow this step:
    ```pip install pipwin ```
   then run this command
    ```pip install PyAudio ```

---

## To Run this program on Startup
### Linux
https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html.en

### Windows
https://support.microsoft.com/en-in/help/4026268/windows-10-change-startup-apps

---

### The Project is now ready to use !!
                                                [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgjbae1212%2Fhit-counter)](https://hits.seeyoufarm.com)                    
### [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
