import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os 
import smtplib
import secrets
import random
import pyautogui
import keyboard 
import time
import pprint
from gtts import gTTS
import csv 
import codecs 
import urllib.request 
import sys
import warnings
import re
import random
import pywintypes
from win10toast import ToastNotifier

MASTER = "Nini"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')  
engine.setProperty('volume',1.0) 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)
    
    speak("How may I halp you?")

def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening...')
		audio = r.listen(source)
		query = ''
	try:
		query = r.recognize_google(audio, language= 'en-in')
		print('You said :'  +query)
		print('You said :'+query, file=open("D:\\script\\Assistents\\Jarvis\\speechtotype.txt", "a"))
	except sr.UnknownValueError:
		print('Say that again please')
	except sr.RequestError as e:
		print('Say that again please ' +e)

	return query
         
def shutdown():
    shutdown = input("Do you wish to shutdown your computer ? (yes / no): ") 
    if shutdown == 'no': 
        exit() 
    else: 
        os.system("shutdown /s /t 1") 

def tellDay(): 
      
    # This function is for telling the 
    # day of the week 
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number  
    # that will help us in telling the day 
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week) 

speak("I'm  jarvis")
wishMe()
 
while True:
	query = takecommand()

	#Logic for executing task as per the query 
	if 'wikipedia' in query.lower():
		speak('Searching wikipedia...')
		query = query.replace("wikipedia", "")
		results = wikipedia.summary(query, sentences =2)
		print(results)
		speak(results)

#-------------------------------------------------------------------

	elif 'open youtube' in query.lower():
		webbrowser.open_new('http://www.youtube.com') 

	elif 'open google' in query.lower():
		webbrowser.open_new('http://www.google.com') 

	elif 'open netflix' in query.lower():
		webbrowser.open_new('https://www.netflix.com/') 

#-------------------------------------------------------------------

	elif 'play music' in query.lower():
		songs_dir = "D:\\Muzica"
		songs = os.listdir(songs_dir)
		print(songs)
		os.startfile(os.path.join(songs_dir, songs[0]))

#-------------------------------------------------------------------

	elif 'brawlhalla' in query.lower():
		brawlhalla_dir = "D:\\steam\\steamapps\\common\\Brawlhalla\\Brawlhalla.exe"
		os.startfile(os.path.join(brawlhalla_dir))

	elif 'close brawlhalla' in query.lower():
		os.system("taskkill /f /im Brawlhalla.exe")

#====================================================================

	elif 'open cs go' in query.lower():
		cs_dir = "D:\steam\steamapps\common\Counter-Strike Global Offensive\csgo.exe"
		os.startfile(os.path.join(cs_dir))

	elif 'close cs go' in query.lower():
		os.system("taskkill /f /im csgo.exe")

#====================================================================

	elif 'open spotify' in query.lower():
		spotify_dir = "C:\\Users\\ninii\\AppData\\Roaming\\Spotify\\Spotify.exe"
		os.startfile(os.path.join(spotify_dir))

	elif 'close spotify' in query.lower():
		os.system("taskkill /f /im Spotify.exe")

#====================================================================

	elif 'open teams' in query.lower():
		teams_dir = "C:\\Users\\ninii\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
		os.startfile(os.path.join(teams_dir))

	elif 'close team' in query.lower():
		os.system("taskkill /f /im Teams.exe")

#====================================================================

	elif 'open discord' in query.lower():
		discord_dir = "C:\\Users\\ninii\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
		os.startfile(os.path.join(discord_dir))

	elif 'close discord' in query.lower():
		os.system("taskkill /f /im Discord.exe")

#====================================================================

	elif 'open payday' in query.lower():
		payday2_dir = "D:\\steam\\steamapps\\common\\PAYDAY 2\\payday2_win32_release.exe"
		os.startfile(os.path.join(payday2_dir))

	elif 'close payday' in query.lower():
		os.system("taskkill /f /im Discord.exe")

#-------------------------------------------------------------------

	elif 'time' in query.lower():
		strTime = datetime.datetime.now().strftime("%H:%M:%S")
		speak(f"{MASTER} the time is {strTime}")
		print(strTime)

	elif 'who are you' in query.lower():
		speak("I am javis assistent virtual")

	elif "what day it is" in query: 
		tellDay() 

	elif 'joke' in query.lower():
		joke = ['One joke, coming up! What is a sea monster’s favorite snack? Ships and dip.', 
		'This might make you laugh. How do robots eat guacamole? With computer chips.',
		'Why did the Clydesdale give the pony a glass of water? Because he was a little horse.',
		'What do you call an alligator detective? An investi-gator.',
		'There are two muffins baking in the oven. One muffin says to the other, “Phew, is it getting hot in here or is it just me?” The other muffin says, “AAAAHHH!! A TALKING MUFFIN!”',
		'What lights up a soccer stadium? A soccer match.']
		speak(random.choice(joke))

	# elif 'shut down' or 'shutdown' in query.lower():
	# 	shutdown()

	elif 'exit' in query.lower():
		break
		
	else:
		pass
