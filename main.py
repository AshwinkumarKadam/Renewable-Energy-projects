import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import sys
import requests
from openai import OpenAI
#pip install pocketsphinx



recognizer = sr.Recognizer()
engine =  pyttsx3.init()
newsapi ="2f78f41dc0ac4f2086ec2aa356f081a2"


def speak(text):
    engine.say(text)
    engine.runAndWait()

# def aiProcess(command):
    
#     client = OpenAI(
#         api_key="sk-abcdijkl1234uvwxabcdijkl1234uvwxabcdijkl",
#     )

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role":"system","content":"you are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#             {"role": "user", "content": command }
#         ]
#     )
#     return completion.choices[0].message.content

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif c.lower().startswith('play'):
        song = c.lower().split(" ")[1]
        link= musiclibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        # Parse the JSON response
        if r.status_code == 200:  # Check if the request was successful
            data = r.json()
            
            # Extract and print headlines
            articles = data.get('articles', [])

            for article in articles:
                speak(article.get('title'))

    elif "sleep jarvis" in c.lower():
        sys.exit()
    # else:
    #     output= aiProcess(c)
    #     speak(output)

if __name__ ==  "__main__":
    speak("Initializing Jarvis......")
    while True:
        #Listen for the wake word "jarvis"
        #obtain audion from the microphone
        r= sr.Recognizer()
        
  
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source)

            word=r.recognize_google(audio)
            # if(word.lower() == "jarvis"):
            if "jarvis" in word.lower():
                speak("boaliye!")
                #listen for command
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processcommand(command)

        except sr.UnknownValueError:
            print("could not understand ")

        except sr.RequestError as e:
            print("Error;{0}".format(e))

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for speech")


        