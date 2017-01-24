# AI Core v3 By Darren Rainey
import os
from time import gmtime, strftime
import random

# Text To Speech Requirments
from espeak import espeak

# Debug Functions
# espeak.synth("Test")

while True:
		Greetings = ['Hello', 'Hey', 'Greetings']
		userInput = raw_input(">>> ")

		# IDA0001 Hello/Greeting Function
		if userInput in ['hi', 'HI', 'Hi', 'Hello', 'hello', 'helo']:
			print (Greetings[int(random.random() * len(Greetings))])
			#print random.choice(Greetings)("AI: ")
			os.system("espeak Hello_$USER >/dev/null 2>&1 &")

		# IDA0002 Time Function	
		elif userInput  in ['time', 'Time', 'TIME']:
			os.system("echo AI: The time is $(date +'%T %p')")
			os.system("espeak The_time_is_$(date +'%T %p') >/dev/null 2>&1 &")

		# IDA0003 Exit Function
		elif userInput in ['exit', 'Exit', 'quit', 'Quit']:
			print("Shutting Down")
			os.system("espeak Shutting_Down_Core_Functions >/dev/null 2>&1 &")
			exit()

		# IDA0004 Help/Guide Function
		elif userInput in ['HELP', 'Help', 'help']:
			print("AI Core V3.0A By Darren Rainey")
			print("Help	-	Displays this menu")
			print("Exit	-	Exits the program")
			print("Hello	-	Greeting")
			print("Time	-	Displays the current time")
			print("Status	-	Displays System Status Report")
			
		# IDA0006 Status Report Function
		elif userInput in ['status', 'Status', 'STATUS']:
			print("Current System Status")
			os.system("sh External/Status.sh")
			
		# IDA0007 Memo Function
		elif userInput in ['memo', 'MEMO', 'Memo']:
			print("Greeting Memo")
			os.system("mkdir Memos/ &2> /dev/null")
			os.system("nano $(echo Memo/$RANDOM.txt")

		# IDA0005 Error Function
		else:
			Error = ['What was that ?', 'I"m sorry I did not understand you', 'Excuse me, What was that ?', 'Please say that again im not sure what you mean']
			print (Error[int(random.random() * len(Error))])
			#print("I did not understand what you said")
