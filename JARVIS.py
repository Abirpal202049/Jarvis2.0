import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests,json
import vlc
import random
from keyboard import press_and_release
# Making google crome as the browser to open the content 
chrome_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("I am Jarvis. I am your personal assistant. How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        # speak("Listening Sir")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # speak("Recognizing Sir...")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        # speak("Sorry Sir, Please Repeat ")
        print("Say that again please...")  
        return "None"
    return query

def takeCommando():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # speak("Listening Sir")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        # speak("Recognizing Sir...")
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        # speak("Sorry Sir, Please Repeat ")
        print("Say that again please...")  
        return "None"
    return query


def musicchanger():
    music = ["35.O Mere Dil Ke Chain.mp3", "36.Yeh Sham Mastani.mp3", "BANG.mp3", "song1.m4a", "song2.mp3", "song3.mp3"]
    temp = random.choice(music)
    print("Temp : ",temp)

    if temp == random.choice(music):
        musicchanger()
    player = vlc.MediaPlayer(temp)
    print("Player :",player)
    return player

# all the command that are to pass to get asuitable result 
def command():
    strTime = datetime.datetime.now().strftime("%H")   
    strTime2=datetime.datetime.now().strftime("%M")
    strTime=int(strTime)
    strTime2=int(strTime2)
    if(strTime>12):
        strTime=strTime-12
    speak(f"and Sir, right now the time is {strTime} {strTime2}")


    player = musicchanger()
    # music = ["35.O Mere Dil Ke Chain.mp3", "36.Yeh Sham Mastani.mp3", "BANG.mp3"]
    
    # player = vlc.MediaPlayer(random.choice(music))
    # print(player)

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try :
                speak('Searching sir...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Me")
                print(results)
                speak(results)
            except:
                print("Some error occured")
        

        #Greeting 
        elif 'hello' in query:
            try :
                speak('Hello Sir, How may I help you')
            except:
                print("Some error occured")

        elif 'thank you' in query:
            try :
                speak("Thank you sir Please Let me Know When You need me again")  
            except:
                print("Some error occured")  
        
        elif 'how are you' in query:
            try :
                speak("I am fine Sir")
                speak("What about you Sir?")
            except:
                print("Some error occured")

        elif 'great' in query:
            try:
                speak("Thank you Sir ")
                speak("I will try to impress you in future")
            except:
                print("Some error occured")

        elif 'fine' in query :
            try :
                speak("wow, thats Great Sir! ")
            except:
                print("Some error occured")


        elif 'temperature' in query :
            try:
                api_key = "e342367614d61e912d92e29103041f54"
                complete_url = 'http://api.openweathermap.org/data/2.5/weather?'+'q='+'Asansol'+'&appid='+api_key
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404": 
                    y = x["main"]
                    current_temperature = y["temp"]
                    speak(" Sir the Temperature is " + str(round(current_temperature-273.15,0)) + 'degree Celsius Outside')
                else: 
                    speak(" City Not Found ")
            except:
                print("Some error occured")


        elif 'weather' in query :
            try :
                speak('Sir, which place weather you want know')
                query_new = takeCommand().lower()

                api_key = "e342367614d61e912d92e29103041f54"
                complete_url = 'http://api.openweathermap.org/data/2.5/weather?'+'q='+query_new+'&appid='+api_key
                response = requests.get(complete_url)
                speak(f'Here is the weather Sir')
                x = response.json()
                if x["cod"] != "404": 
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"] 
                    current_humidiy = y["humidity"]
                    z = x["weather"] 
                    weather_description = z[0]["description"]
                    speak(f" Sir, the Weather is {weather_description}")
                    speak(" The Temperature is " + str(round(current_temperature-273.15,0)) + 'degree Celsius ')
                    speak(f" The Humidity is {current_humidiy} grams per kg " )
                    speak(f"And Sir, the Air Presser is {current_pressure} pascal ")
                else: 
                    speak(" City Not Found ")
            except:
                print("Some error occured")



        elif 'news' in query :
            try:
                complete_url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=dd4c42a274c14a0587f6225427ad4b6b'
                response = requests.get(complete_url)
                speak("Here are some of the latest News")
                x = response.json()
                table = ['The First One is : ', 'The Second One is : ', 'The Third One is : ', 'The Fourth is : ', 'The Fifth One is : ']
                if x['status'] == 'ok':
                    y = x["articles"]
                    for value in range(5):
                        d = y[value]["title"]
                        print(d)
                        speak(table[value])
                        speak(d)
                print(x["status"])
            except:
                print("Some error occured")


        # Lets google do it
        elif 'open youtube' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open("youtube.com")
            except:
                print("Some error occured")

        elif 'open google' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open('google.com')
            except:
                print("Some error occured")


        #Open vs code for me 
        elif 'open vs code' in query:
            try:
                speak('opening vs code sir..')
                codePath = "C:\\Users\\Abir Pal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            except:
                print("Some error occured")
        



        #My classroom section
        elif'open my classroom' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open("classroom.google.com")
            except:
                print("Some error occured")


        elif 'close' in query and 'tab' in query or 'close the tab' in query:
            try :
                speak('closing sir..')
                press_and_release('ctrl + w')
            except:
                print("Some error occured")


        # My social account and other resourses 
        elif 'open my github' in query:
            try:
                speak('Opening sir..')
                webbrowser.get('chrome').open("github.com")
            except:
                print("Some error occured")
        
        elif 'open my gmail' in query or 'open my email' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open("gmail.com")
            except:
                print("Some error occured")

        elif 'open my LinkdIn' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open("linkdin.com")
            except:
                print("Some error occured")

        elif 'open my college website' in query:
            try :
                speak('Opening sir..')
                webbrowser.get('chrome').open("http://www.aecwb.edu.in/?pn=94728362228456373")
            except:
                print("Some error occured")



        # Search operation using google by opening the google browser   
        elif 'open' in query:
            try:
                speak("searching sir...")
                try: 
                    from googlesearch import search 
                except ImportError:  
                    print("No module named 'google' found") 
    
                query = query.replace("search", "")
                query = query.replace("jarvis", "")

                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    break
                print(j)
                webbrowser.get('chrome').open(j)
            except:
                print("Some error occured")

        # ? youtube play
        elif 'play' in query and 'youtube' in query:
            try :
                speak("Playing sir...")
                try: 
                    from googlesearch import search 
                except ImportError:  
                    print("No module named 'google' found") 
    
                query = query.replace("play", "")
                query = query.replace("youtube", "")

                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    break
                print(j)
                webbrowser.get('chrome').open(j)
            except:
                print("Some error occured")


        # Music player system     
        elif 'any music' in query or 'some music' in query or 'a song' in query:
            try :
                player.stop()
                player = musicchanger()
                speak('Playing sir..')
                player.play()
            except:
                print("Some error occured")

        elif 'pause' in query:
            try :
                speak('Music Paused')
                player.pause()
            except:
                print("Some error occured")

        elif 'play' in query or 'resume' in query:
            try :
                speak('Resuming the music')
                player.play()
            except:
                print("Some error occured")

        elif 'stop' in query:
            try :
                speak('Music Stopped')
                player.stop()
            except:
                print("Some error occured")

        elif 'change the music' in query or 'change the song' in query:
            try :
                player.stop()
                speak("Changing the music")
                player = musicchanger()
                player.play()
            except:
                print("Some error occured")
        
                


        #Time teller
        elif 'time' in query:
            try :
                strTime = datetime.datetime.now().strftime("%H")   
                strTime2=datetime.datetime.now().strftime("%M")
                strTime=int(strTime)
                strTime2=int(strTime2)
                if(strTime>12):
                    strTime=strTime-12
                speak(f"Sir, the time is {strTime} {strTime2}")
            except:
                print("Some error occured")

        elif 'close google' in query or 'close the google' in query:
            try :
                speak('closing google sir..')
                codePath = "C:\\Users\\Abir Pal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.system("taskkill /f /im chrome.exe")
            except:
                print("Some error occured")



        # Exit from the program
        elif 'sleep' in query :
            try :
                speak('Sir I am going to sleep, You can call me anytime')
                break
            except:
                print("Some error occured")
            

def initial(speak, wishMe, takeCommando, command):
    wishMe()
    while True:
        w=takeCommando()
        w.lower
        if 'wake up' in w:
            speak('Yes sir. I woke up. I am redy to help you')
            command()
        elif 'exit' in w:
            speak("Thank You sir , and Have a Good day ")
            break



if __name__ == "__main__":
    initial(speak, wishMe, takeCommando, command)



# There ias a problem in the code so i acant do this currewntly there the music player is not working currently so it need to be solve but i dont no what to change vecause according to me the cose is all right but the code is actuallly not tracking the codes path                 