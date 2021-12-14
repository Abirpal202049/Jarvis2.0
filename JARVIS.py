import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import requests,json

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




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anish28032002@gmail.com', '########')
    server.sendmail('anish28032002@gmail.com', to, content)
    server.close()




# all the command that are to pass to get asuitable result 


def command():


    strTime = datetime.datetime.now().strftime("%H")   
    strTime2=datetime.datetime.now().strftime("%M")
    strTime=int(strTime)
    strTime2=int(strTime2)
    if(strTime>12):
        strTime=strTime-12
    speak(f"and Sir, right now the time is {strTime} {strTime2}")

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Me")
            print(results)
            speak(results)
        

        #Greeting 
        elif 'hello' in query:
            speak('Hello Sir, How may I help you')

        elif 'thank you' in query:
            speak("I am always there with you sir")
        
        elif 'how are you' in query:
            speak("I am fine Sir")
            speak("What about you Sir?")

        elif 'fine' in query or 'great' in query :
            speak("wow, thats Great Sir! ")

        elif 'temperature' in query :
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
        elif 'weather' in query :
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




        # Lets google do it
        elif 'open youtube' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open('google.com')



        # Search operation using google by opening the google browser   
        elif 'search' in query:
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



        # Educational purpose site
        elif 'open udemy' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open('udemy.com')

        elif 'open coursera' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open('coursera.com')
        



        #My classroom section
        elif'open my classroom' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("classroom.google.com")
        
        elif'open my maps classroom' in query or'open my maths classroom' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("https://classroom.google.com/u/0/c/MTUzNDAxMTA4OTQ4")

        elif'open my physics classroom' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("https://classroom.google.com/u/0/c/NTQwOTQxNjY2Nzla")

        elif'open my electrical classroom' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("https://classroom.google.com/u/0/c/MjE1MTExNjM1OTIx")



        # My social account and other resourses 
        elif 'open my github' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("github.com")
        
        elif 'open my gmail' in query or 'open my email' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("gmail.com")

        elif 'open my LinkdIn' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("linkdin.com")

        elif 'open my college website' in query:
            speak('Opening sir..')
            webbrowser.get('chrome').open("http://www.aecwb.edu.in/?pn=94728362228456373")
 


        # Music player system     
        elif 'my music' in query:
            webbrowser.open("https://youtu.be/D8ksFyjTCp0")   
        
        

        elif 'music' in query:
            speak("Playing Sir, Enjoy....")
            playsound('./BANG.mp3')
            
        

        elif 'old song' in query:
            speak('which one sir ')
            arr=['O Mere Dil Ke Chain','Yeh Sham Mastani']
            query_new = takeCommand().lower()

            if 'list' in query_new:
                speak('Here is the list Sir...') 
                print(arr)
                speak(arr)
                speak('which one sir ')
                song=takeCommand().lower()

                if 'first' in song:
                    speak('Enjoy sir...')
                    playsound('35.O Mere Dil Ke Chain.mp3')

                    
                elif 'second' in song:
                    speak('Enjoy sir...')
                    playsound('36.Yeh Sham Mastani.mp3')
                

            
        


        #Time teller
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H")   
            strTime2=datetime.datetime.now().strftime("%M")
            strTime=int(strTime)
            strTime2=int(strTime2)
            if(strTime>12):
                strTime=strTime-12
            speak(f"Sir, the time is {strTime} {strTime2}")


        #Open vs code for me 
        elif 'open vs code' in query:
            speak('opening vs code sir..')
            codePath = "C:\\Users\\Abir Pal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        # Exit from the program
        elif 'sleep' in query :
            speak('Sir I am going to sleep, You can call me anytime')
            break
        


        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anish28032002@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir . I am not able to send this email. Due to some issue ")    




def boom(speak, wishMe, takeCommando, command):
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
    boom(speak, wishMe, takeCommando, command)



# There ias a problem in the code so i acant do this currewntly there the music player is not working currently so it need to be solve but i dont no what to change vecause according to me the cose is all right but the code is actuallly not tracking the codes path                 