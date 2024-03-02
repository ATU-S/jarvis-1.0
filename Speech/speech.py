import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time
import requests
import shutil
import subprocess
from twilio.rest import Client
from ecapture import ecapture as ec
from urllib.request import urlopen
import pyautogui
import openai
import psutil
import socket
import platform

openai.api_key = 'API_KEY'
assname = ''

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 1 for female voice and 0 for male voice


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !") 

    else:
        speak("Good Evening Sir !") 

    assname =("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
	speak("What should i call you sir")
	uname = takeCommand()
	if uname == 'anandhu':
		speak("Welcome Back Master")
	else:
		speak("Welcome Mister")
		speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e) 
		print("Unable to Recognize your voice.")
		return "None"
	
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com") 

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "C:\\Users\\ananthu\\Music"
			songs = os.listdir(music_dir)
			print(songs) 
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M:%S")
			speak(f"Sir, the time is {strTime}")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query: 
			speak("I have been created by Ananthu.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "") 
			query = query.replace("play", "")		 
			webbrowser.open(query) 

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to Ananthu. further It's a secret")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Ananthu ")

		elif 'reason for you' in query:
			speak("I was created as a project of Ananthu ")

		elif 'news' in query:
			
			try: 
				jsonObj = urlopen('''https://timesofindia.indiatimes.com/city/kozhik''')
				data = json.load(jsonObj)
				i = 1
				
				speak('here are some top news from the times of india')
				print('''=============== TIMES OF INDIA ============'''+ '\n')
				
				for item in data['articles']:
					
					print(str(i) + '. ' + item['title'] + '\n')
					print(item['description'] + '\n')
					speak(str(i) + '. ' + item['title'] + '\n')
					i += 1
			except Exception as e:
				
				print(str(e))

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query or "locate" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl/maps/place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")
		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r") 
			print(file.read())
			speak(file.read(6))
					
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 1 point o in your service Mister")
			speak(assname)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather 
			api_key = "API_KEY"
			base_url = "http://api.openweathermap.org/data/2.5/weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appi d =" + api_key + "&q =" + city_name
			response = requests.get(complete_url) 
			x = response.json() 
			
			if "code" in x and x["code"] != "404": 
				y = x["main"] 
				current_temperature = y["temp"] 
				current_pressure = y["pressure"] 
				current_humidiy = y["humidity"] 
				z = x["weather"] 
				weather_description = z[0]["description"] 
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
			
			else: 
				speak(" City Not Found ")
			

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)

		elif "how are you" in query:
			speak("I'm fine, glad you me that")


		elif "what is" in query or "who is" in query:
			
			# Use the same API key 
			# that we have generated earlier
			client = wolframalpha.Client("API_KEY")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		elif "random number" in query:
			num = random.randint(0,100)
			speak("A random number is " + str(num))

		elif "open instagram profile" in query:
			speak("Opening instagram")
			webbrowser.open("https://www.instagram.com/ananthus.1?igsh=MXMxcGcwemw3cDd4bw==")


		if 'hi' in query or "hey" in query:
			speak("Hi there im your virtual assistance created for assist you")

		elif 'open website' in query:
			query = query.replace("open website", "")
			speak(f"opening {query}")
			webbrowser.open(query)

		elif 'search on google' in query:
			query = query.replace("search on google", "")
			speak(f"Searching on Google for {query}")
			webbrowser.open(f"https://www.google.com/search?q={query}")

		elif 'youtube' in query:
			query = query.replace("youtube", "")
			speak(f"Searching on YouTube for {query}")
			webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

		elif 'open file' in query:
			file_name = query.replace("open file", "")
			try:
				os.startfile(file_name)
				speak(f"Opening {file_name}")
			except Exception as e:
				print(f"Error opening the file: {str(e)}")
				speak("Sorry, I couldn't open the file.")

		elif 'calculate' in query:
			try:
				calculation = query.replace("calculate", "")
				result = eval(calculation)
				speak(f"The result is {result}")
			except Exception as e:
				print(f"Error performing the calculation: {str(e)}")
				speak("Sorry, I couldn't perform the calculation.")

		elif 'ask for gpt' in query:
			query = query.replace("ask for gpt", "")
			
			# Call the OpenAI GPT-3 API
			response = openai.Completion.create(
				engine="text-davinci-002",
				prompt=query,
				max_tokens=50
			)
			
			chatgpt_response = response.choices[0].text.strip()
			speak(chatgpt_response)

		elif 'battery status' in query:
			try:
				battery = psutil.sensors_battery()
				percent = battery.percent
				speak(f"The battery is at {percent} percent.")
			except Exception as e:
				print(f"Error checking battery status: {str(e)}")
				speak("Sorry, I couldn't check the battery status.")

		elif 'take screenshot' in query:
			try:
				screenshot = pyautogui.screenshot()
				screenshot.save("screenshot.png")
				speak("Screenshot taken and saved as screenshot.png")
			except Exception as e:
				print(f"Error taking screenshot: {str(e)}")
				speak("Sorry, I couldn't take a screenshot.")

		elif 'internet status' in query:
			try:
				socket.create_connection(("www.google.com", 80), timeout=5)
				speak("Internet is connected.")
			except OSError:
				speak("Internet is not connected.")

		elif 'list files' in query or 'list folders' in query:
			speak("Which directory do you want to list?")
			dir_path = takeCommand()
			
			try:
				contents = os.listdir(dir_path)

				if contents:
					speak(f"Here are the contents of {dir_path}:")
					for item in contents:
						speak(item)
						print(item)
				else:
					speak(f"The directory {dir_path} is empty.")
			
			except Exception as e:
				speak(f"Error listing files/folders: {str(e)}")
				print(f"Error listing files/folders: {str(e)}")

		elif 'system information' in query:
			try:
				system_info = platform.system()
				version_info = platform.version()
				architecture_info = platform.architecture()
				speak(f"System: {system_info}, Version: {version_info}, Architecture: {architecture_info}")
			except Exception as e:
				print(f"Error checking system information: {str(e)}")
				speak("Sorry, I couldn't retrieve system information.")

		elif 'list drives' in query:
			try:
				import psutil
				drives = [drive.device for drive in psutil.disk_partitions()]
				speak("Available drives are:")
				for drive in drives:
					speak(drive)
					print(drive)
			except Exception as e:
				print(f"Error listing drives: {str(e)}")
				speak("Sorry, I couldn't list the drives.")

		elif 'memory usage' in query:
			try:
				memory_info = psutil.virtual_memory()
				speak(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB, Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
			except Exception as e:
				print(f"Error checking memory usage: {str(e)}")
				speak("Sorry, I couldn't check memory usage.")

