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
import JarvisAI
import re
import pprint
import random
import pywhatkit as kit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path='D:\\script\\Assistents\\Jarvis\\chromedriver.exe')
#driver = webdriver.Chrome()
#driver.get("https://www.google.com/")


sys.path.append("D:\\script\\Assistents")

MASTER = "Nini"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')  
engine.setProperty('volume',1.0) 




#Speak funtion will pronouce the string 
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
		print('You said :'+query)
		
	except sr.UnknownValueError:
		print('Say that again please')
	except sr.RequestError as e:
		print('Say that again please ' +e)



	return query



def closeb():
    os.system("taskkill /f /im Brawlhalla.exe")

def closec():
    os.system("taskkill /f /im csgo.exe")
            
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

def closet():
	os.system("taskkill /f /im Teams.exe")

def closed():
	os.system("taskkill /f /im Discord.exe")

def playmusiconyt():
    kit.playonyt()

#def opentab():
	#driver = webdriver.Chrome(executable_path='D:\\script\\Assistents\\Jarvis\\chromedriver.exe')
	#open tab
#	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	# You can use (Keys.CONTROL + 't') on other OSs

#def closetab():
#	driver = webdriver.Chrome(executable_path='D:\\script\\Assistents\\Jarvis\\chromedriver.exe')
	# close the tab
	# (Keys.CONTROL + 'w') on other OSs.
#driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 

speak("I'm  javis")
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

	elif 'open youtube' in query.lower():
		playmusiconyt()

	elif 'open google' in query.lower():
		webbrowser.open_new('http://www.google.com') 

	elif 'new tab' in query.lower():
		keyboard.press('ctrl' + 't')

	elif 'close tab' in query.lower():
		closetab()


	elif 'play music' in query.lower():
		songs_dir = "https://www.youtube.com/playlist?list=PLG-mTtNbMVGO7roi4Q_Sn8Tnn-FB5TDXA"
		songs = os.listdir(songs_dir)
		print(songs)
		os.startfile(os.path.join(songs_dir, songs[0]))

	elif 'brawlhalla' in query.lower():
		brawlhalla_dir = "D:\\steam\\steamapps\\common\\Brawlhalla\\Brawlhalla.exe"
		os.startfile(os.path.join(brawlhalla_dir))

	elif 'close b' in query.lower():
		closeb()

	elif 'cs go' in query.lower():
		#csgo_dir = "D:\\steam\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe"
		#os.startfile(os.path.join(csgo_dir))
		cs_dir = "D:\\steam\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe"
		os.startfile(os.path.join(cs_dir))

	elif 'close c' in query.lower():
		closec()

	elif 'open teams' in query.lower():
		teams_dir = "C:\\Users\\ninii\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
		os.startfile(os.path.join(teams_dir))

	elif 'close team' in query.lower():
		closet()

	elif 'open discord' in query.lower():
		discord_dir = "C:\\Users\\ninii\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe"
		os.startfile(os.path.join(discord_dir))

	elif 'close discord' in query.lower():
		closed()

	elif 'time' in query.lower():
		strTime = datetime.datetime.now().strftime("%H:%M:%S")
		speak(f"{MASTER} the time is {strTime}")
		print(strTime)

	#elif 'watch' in query.lower():

#	obj = JarvisAI.JarvisAssistant()
#	query = obj.mic_input()

#	elif 'wall hack' or 'wallhack' in query.lower():
#		os.system('cd D:\\script\\Assistents\\javis') 
#		os.system('py glow.py')
#		import glow
#		glow.main()

#	if 'weather' in query.lower():
#		city = query.split(' ')[-1]
#		weather_query = obj.weather(city = Bucuresti)
#		print(weather_query)
#		speak(weather_query)

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


	elif 'shut down' in query.lower():
		shutdown()

	elif 'shutdown' in query.lower():
			shutdown()

	elif 'exit' in query.lower():
		break

	else:
		pass

