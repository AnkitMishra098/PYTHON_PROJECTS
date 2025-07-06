import pyttsx3 # text to speech
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import subprocess
import random
import psutil

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

    speak("I am jarvis . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('ankit8706@gmail.com', 'ankit123#@.')
#     server.sendmail('ankit8706@gmail.com', to, content)
#     server.close()

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
            
        elif 'hello' in query:
            speak('hello sir.......how can i help u')

        elif 'hi' in query:
            speak('hi sir.......how can i help u')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google is opened")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Stack overflow is opened")
        
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            if battery:
                print(f"Battery Percentage: {battery.percent}%")
                speak(f"Battery Percentage: {battery.percent}%")
                print(f"Power Plugged In: {'Yes' if battery.power_plugged else 'No'}")
                speak(f"Power Plugged In: {'Yes' if battery.power_plugged else 'No'}")
                print(f"Time Left: {battery.secsleft // 60} minutes" if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Unlimited")
                speak(f"Time Left: {battery.secsleft // 60} minutes" if battery.secsleft != psutil.POWER_TIME_UNLIMITED else "Unlimited")
                speak('anything else sir')
            else:
                speak("No battery is detected on this device.")
            
        elif 'open chat gpt' in query:
            webbrowser.open("chatgpt.com")
            speak("chat GPT is opened")  

        elif 'open erp' in query:
            webbrowser.open("https://erp.rkgit.edu.in/")
            speak("ERP is opened")

        elif 'open whatsapp' in query:
            webbrowser.open("C:\\Users\\asus\\OneDrive\\Desktop\\WhatsApp Web.lnk")
            speak("whatsapp is opened")

        elif 'open typing master' in query:
            webbrowser.open("c:\\Users\\Public\\Desktop\\Typing Master 11.lnk") 
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = "C:\\Users\\asus\\Music\\music_dir"
            songs = os.listdir(music_dir)
            rand=random.randint(1,7)  
            speak("Enjoy our playlist") 
            os.startfile(os.path.join(music_dir, songs[rand]))
        
        elif 'set alarm' in query:
            try:
                speak("What time should i set the alarm")
                time=takeCommand()
                speak(f"your alarm is set succesfully  at {time}")
            except Exception as e:
                print(e)
        elif 'open calculator' in query:
            webbrowser.open('https://www.online-calculator.com//')
            speak("calculator is opened")

        elif 'open score' in query:
            webbrowser.open('https://www.cricbuzz.com//')
            speak("cricbuzz is opened")


        elif 'thank 'in query:
            speak('my pleasure sir !!have a nice day !!! ')

    

        # elif 'email to ankit' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "ankitmishra8706@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend ankit bhai. I am not able to send this email")    
