# J.A.R.V.I.S (Just A Rather Very Intelligent System)

## About Project 

### Jarvis is a virtual assistant like Siri and Alexa with additional face recognition based secruity mechanism. The assitant recognises speech and face of the user and responds accordingly. 

Various Features and tasks performed by this assistant are:

1. It first wishes and greet the user by it's name according to the face recognized by the face recognizer.
2. It make use of Web Scraping to retreive the information directly from **Wikipedia** and can speak it directly by reading from Wiki.
3. It can report current date and time for you.
4. It can open Google, Youtube, Stackoverflow, Instagram, Facebook, Tinder and other **social media** Web applications for you by directly saying the name of the social media app.
5. It can open Python Interpreter(IDLE), Notepad, Calculator and other **System Softwares** for you.
6. It can open code editor or **IDE** like Vs-Code,Code-Blocks and any other IDE etc of your choice.
7. You can **send Email** to the intended user, It will be sended by personal email of Jarvis which can be configured according to the requirements.
8. Equipped with **face recognition.**
9. You **track prices** of the given product from the **E-Commerce** Websites according to the URL mentioned and can also tell it will be in your budget or not according to the settings done for the program.
10. You can also **track COVID-19 Vaccination Drives** near your location according to the district, state or precisily by updating your pincode in the setting.json file. 


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

4. Change ```budget:0```  value to your budget (Example: ```budget:999```) for price tracking & Update ```pin-code``` value according to your nearby postal code (Example: ```pin-code:161005```).

5. Replace the link in **URL** with your target product link. (Example: ```url:'https://www.amazon.in/G731GT-Graphics-i5-9300H-Windows-G731GT-AU022T/dp/B07S36XJ8Q/'```)

6. Change the **user agent** according to your [**user agent**](https://www.google.com/search?q=my+user+agent&oq=my+user&aqs=chrome.1.69i57j0l5.2294j1j7&sourceid=chrome&ie=UTF-8). (Example: ```headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'} ```). 
To know your user-agent just type the following  on google:
  ```
  my user agent
  ```

7. Now save the file and run **main.py** by typing the following command on your Command Prompt:

```
python main.py
```

**Note:** 1. To open code editor of your choice and python interpreter(IDLE) you have to provide
path of your local directories in the source code to avoid error.
2. If there is any error regarding microphone or related to pyttsx3 or speech_recognition module  follow these steps:
    ```pip install pipwin ```
   then run this command
    ```pip install PyAudio ```

3. In case you receive such errors: 

```
No module named win32com.client
No module named win32
No module named win32api 
```
Then, install pypiwin32 by typing the below command in the terminal :
```
pip install pypiwin32.
```
After successfully installing pyttsx3, import this module into your program.


## Implementation, Tools and Technologies

- We have used ```Co-WIN Public API``` to fetch all the nearby vaccination drive locations and details. Co-WIN Public APIs allow any third-party application to access certain un-restricted information, that can be shared with its users. This is limited only to read access in Co-WIN. The extent of access will be limited and in case of any misuse impacting the performance of Co-WIN solution will result in blocking any such application and entities as per the policies of MoHFW and taking any other appropriate action in accordance with law. The appointment availability data is cached and may be up to 5 minutes old. Further, these APIs are subject to a rate limit of 100 API calls per 5 minutes per IP. Please consider these points while using the APIs in your application.

- We have used ```Speech Recognition``` Library that is used for performing speech recognition, with support for several engines and APIs, both online and offline.

- To make our J.A.R.V.I.S. talk, we will make a function called speak(). This function will take audio as an argument, and then it will pronounce it. We must supply audio so that we can pronounce it using the speak() function we made. For this We are using a module called ```pyttsx3``` It's a python library that will help us to convert text to speech. In short, it is a text-to-speech library.
It works offline, and it is compatible with Python 2 as well as Python 3. In this module we have various TTS engines namely
    - sapi5
    - nsss 
    - espeak. 
We have used ```sapi5``` application programming interface (API). It dramatically reduces the code overhead required for an application to use speech recognition and text-to-speech, making speech technology more accessible and robust for a wide range of applications. It Synthesize text strings and files into spoken audio using synthetic voices. Speech recognizers convert human spoken audio into readable text strings and files.
Applications that use SAPI include Microsoft Office, Microsoft Agent and Microsoft Speech Server.
In general, all versions of the API have been designed such that a software developer can write an application to perform speech recognition and synthesis by using a standard set of interfaces, accessible from a variety of programming languages. In addition, it is possible for a 3rd-party company to produce their own Speech Recognition and Text-To-Speech engines or adapt existing engines to work with SAPI. In principle, as long as these engines conform to the defined interfaces they can be used instead of the Microsoft-supplied engines.

In general, the Speech API is a freely redistributable component which can be shipped with any Windows application that wishes to use speech technology. Many versions (although not all) of the speech recognition and synthesis engines are also freely redistributable.


- To Recognize and manipulate faces from Python or from the command line with the world’s simplest face recognition library ```Face Recognition``` built using dlib’s state-of-the-art face recognition built with deep learning. The model has an accuracy of 99.38% on the Labeled Faces in the Wild benchmark. This also provides a simple face_recognition command line tool that lets
you do face recognition on a folder of images from the command line! Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems. It is used in both industry and academia in a wide range of domains including robotics, embedded devices, mobile phones, and large high performance computing environments. Dlib's open source licensing allows you to use it in any application, free of charge. It internally uses OpenCV and Numpy for performing Image recognition or Processing. 

- For Web Scraping, we have used ```Beautiful Soup``` It is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
-- 


## BiblioGraphy 
- https://pyttsx3.readthedocs.io/en/latest/
- https://apisetu.gov.in/about.php
- https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms723627(v=vs.85)
- https://en.wikipedia.org/wiki/Microsoft_Speech_API
- http://dlib.net/
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/


---

## To Run this program on Startup
### Linux
https://help.ubuntu.com/stable/ubuntu-help/startup-applications.html.en

### Windows
https://support.microsoft.com/en-in/help/4026268/windows-10-change-startup-apps

---

### The Project is now ready to use !!

### [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgjbae1212%2Fhit-counter&count_bg=%23313129&title_bg=%231F1F1F&icon=purescript.svg&icon_color=%23FFDD00&title=Repository+Vists&edge_flat=true)](https://hits.seeyoufarm.com)
=======               

### [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
