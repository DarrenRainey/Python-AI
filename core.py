# AI Core v3 By Darren Rainey
import os
from time import gmtime, strftime
import random

while True:
	Greetings = ['Hello', 'Hey', 'Greetings']
	userInput = raw_input(">>> ")
	if userInput in ['hi', 'HI', 'Hi', 'Hello', 'hello', 'helo']:
		print (Greetings[int(random.random() * len(Greetings))])
		#print random.choice(Greetings)("AI: ")
		os.system("espeak Hello_$USER >/dev/null 2>&1 &")
    
	elif userInput  in ['time', 'Time', 'TIME']:
		os.system("echo AI: The time is $(date +'%T %p')")
		os.system("espeak The_time_is_$(date +'%T %p') >/dev/null 2>&1 &")
    
	elif userInput in ['exit', 'Exit', 'quit', 'Quit']:
		print("Shutting Down")
		os.system("espeak Shutting_Down_Core_Functions >/dev/null 2>&1 &")
		exit()
    
	elif userInput in ['HELP', 'Help', 'help']:
		print("AI Core V3.0A By Darren Rainey")
		print("Help	-	Displays this menu")
		print("Exit	-	Exits the program")
		print("Hello	-	Greeting")
		print("Time	-	Displays the current time")
    
	else:
		Error = ['What was that ?', 'I"m sorry I did not understand you', 'Excuse me, What was that ?', 'Please say that again im not sure what you mean']
		print (Error[int(random.random() * len(Error))])
		#print("I did not understand what you said")
