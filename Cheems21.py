import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import smtplib
import time
from selenium import webdriver
name_list=['ravi','kesav','sidhant','hrithik','likith','chinmayi','chethan','divya','sanjay','valli','bhavesh']
email_list=['ajravikumar12@gmail.com','kranjan5679@gmail.com','siddhantsamastx@gmail.com',"neymarhrithik11@gmail.com",'likhithds2001@gmail.com','chinmayeechavan@gmail.com','dgod11001@gmail.com','trnt.divya17@gmail.com','sanjaypandaj90@gmail.com','walihaider111@gmail.com','bhaveshrex007@gmail.com']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning')

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak('Good Evening')

    speak("Hello i am your computer assistant. How may i help u")
def take_Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User told : {query}\n")

    except Exception as e:

        print("Can you repeat it please")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('ar9631247743@gmail.com','Aditya@1439')
    server.sendmail('ar9631247743@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wish_user()
    while True:

        query = take_Command().lower()

        if 'wikipedia' in query:
            speak('Please wait while I am searching in wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif ("access" in query) :
            speak("Opening MICROSOFT ACCESS")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//MSACCESS.exe")
        elif ("open excel" in query) :
            speak("Opening MICROSOFT EXCEl")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//EXCEL.exe")
        elif ("open publisher" in query) :
            speak("Opening MICROSOFT PUBLISHER")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//MSPUB.exe")
        elif ("open one note" in query or "one note"in query ) :
            speak("Opening MICROSOFT ONENOTE")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//ONENOTE.exe")
        elif ("open powerpoint" in query) :
            speak("Opening MICROSOFT POWERPOINT")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//POWERPNT.exe")
        elif ("open v i s i o" in query) :
            speak("Opening MICROSOFT VISIO")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//VISIO.exe")
        elif ("open  word "in query):
            speak("Opening MICROSOFT WORD")
            subprocess.call("C://Program Files//Microsoft Office//root//Office16//WINWORD.exe")
        elif ("open itunes" in query):
            speak("Opening itunes")
            subprocess.call("C://Program Files//iTunes//iTunes.exe")
        elif ("open vscode" in query or "visual studio code" in query or "open vs code" in query):
            speak("Opening Visual Studio Code")
            subprocess.call("C://Users//ar963//AppData//Local//Programs//Microsoft VS Code//Code.exe")
        elif ("open pycharm" in query or "pycharm" in query or "open pychamp" in query):
            speak("Opening Pycharm")
            subprocess.call("C://Program Files//JetBrains//PyCharm Community Edition 2021.2.3//bin\pycharm64.exe")
        elif ("open chrome" in query):
            speak("Opening google chrome")
            subprocess.call("C://Program Files//Google//Chrome//Application//chrome.exe")
        elif ("chrome" in query and "search " in query or "find" in query or "show" in query) :
            text = query
            word = "chrome"
            word1 = "search"
            word2 = "on"
            word3 = "in"
            text = text.replace(word, "")
            text = text.replace(word1, "")
            text = text.replace(word2, "")
            text = text.replace(word3, "")
            webbrowser.open(f"https://www.google.com/search?q={text}")
        elif ("search " in query and "youtube" in query) :
            text1 = query
            words = "youtube"
            word1 = "search"
            word2 = "on"
            word3 = "in"
            text1 = text1.replace(words, "")
            text1 = text1.replace(word1, "")
            text1 = text1.replace(word2, "")
            text1 = text1.replace(word3, "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text1}")
        elif ("play music" in query):
            speak("wait till processing")
            subprocess.call("C://Users//ar963//AppData//Roaming//Spotify//Spotify.exe")
        elif ("spotify" in query):
            speak("wait till processing")
            subprocess.call("C://Users//ar963//AppData//Roaming//Spotify//Spotify.exe")
        elif ("irctc" in query):
            speak("wait till processing")
            webbrowser.open("https://www.irctc.co.in/nget/train-search")
        elif ("booking" in query or "book" in query and "train" in query or "flight" in query or "hotel" in query):
            speak("wait till processing")
            webbrowser.open("https://www.makemytrip.com/")
        elif ("time" in query):
            time1=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time1}")
        elif ('send email' in query or 'send mail' in query or'send a email' in query or 'send a mail' in query) :
             try:
                 speak("enter the email address to whome u want to send mail")
                 to=input("sender's email address :-")
                 speak("do you want to write or speak the message ")
                 content1 = take_Command()
                 if "write" in content1:
                     print("Write the message below")
                     speak("write the message below")
                     abcd=input()
                     speak("wait for confirmation")
                     sendEmail(to,abcd)
                 else:
                     content=take_Command()
                     sendEmail(to,content)
                 speak('Email has been sent')
             except Exception as e:
                 speak("Sorry mail cant be sent")
        elif 'exit' in query or 'none' in query :
            speak('Bye ..........have a good day')
            exit()
        elif "open whatsapp" in query:
            speak("wait till processing")
            webbrowser.open("https://web.whatsapp.com/")
        elif "open my instagram profile" in query:
            speak("please enter your login details")
            time.sleep(1)
            speak("please enter your username below")
            a=input("Username/Phone no./email_address:-")
            time.sleep(0.5)
            speak("please enter your password below")
            b=input("Password:-")
            speak("please wait while u r redirected to instagram page and logged in")
            browsers = webdriver.Chrome("C://Users//ar963//chromedriver//chromedriver.exe")
            browsers.get('https://www.instagram.com/')
            time.sleep(1)
            search_input = browsers.find_element_by_name("username")
            search_input.send_keys(a)
            time.sleep(1)
            search_input = browsers.find_element_by_name("password")
            search_input.send_keys(b)
            time.sleep(2)
            select_plans = browsers.find_elements_by_xpath('.//*[@id="loginForm"]/div/div[3]/button')
            if len(select_plans) > 0:
                select_plans[0].click()
            '''<button type="submit" class="btn btn-primary btn-block customB">Login</button>'''
            '''<button type="submit" class="btn btn-primary btn-block customB">Login</button>'''
        elif "open my erp profile" in query:
            speak("please enter your login details")
            time.sleep(1)
            speak("please enter your username ")
            a=input("Username/Phone no./email_address:-")
            time.sleep(0.5)
            speak("please enter your password ")
            b=input("Password:-")
            speak("please wait while u r redirected to Reva University page and logged in")
            browsers = webdriver.Chrome("C://Users//ar963//chromedriver//chromedriver.exe")
            browsers.get("https://erp.reva.edu.in/login.htm;jsessionid=411E66C8693267F08115F3DA881CAAE1")
            time.sleep(1)
            search_input = browsers.find_element_by_name("j_username")
            search_input.send_keys(a)
            time.sleep(1)
            search_input = browsers.find_element_by_name("j_password")
            search_input.send_keys(b)
            time.sleep(2)
            select_plans = browsers.find_elements_by_xpath('.//*[@id="form-sign-up"]/button')
            if len(select_plans) > 0:
                select_plans[0].click()
        elif "open my erp profile" not in query and  "open my instagram profile" not  in query and "open whatsapp" not in query and  "open instagram" not in query and  "open aditya instagram" not  in query and "reva erp" not  in query and "open erp" not  in query and 'exit' not  in query and 'send email' not  in query and 'send mail' not in query and  'send a email' not in query and  'send a mail' not in query and "booking" not in query and  "book" not in query and  "train" not  in query and "flight" not in query and  "hotel" not in query and  "irctc" not in query and  "spotify" not  in query and "play music" not in query and  "search " not in query and  "youtube" not in query and  "chrome" not in query and  "find" not in query  and "show" not in query and  "open chrome" not in query and "open pycharm" not in query and  "pycharm" not in query and  "open pychamp" not in query and  "open vs code" not in query and  "visual studio code" not in query and  "open vscode" not in query and  "open itunes" not in query and  "open  word " not in query and  "open v i s i o" not in query and  "open powerpoint" not in query and  "open one note" not in query and  "open publisher" not in query and  "open excel" not in query and  "access" not in query and  'open google' not in query  and 'open youtube' not in query and  'wikipedia' not in query :
            speak("Please wait i am searching it for u")
            webbrowser.open(f"https://www.google.com/search?q={query}")











