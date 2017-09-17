def recording(): # Initializes a function definition
	import speech_recognition as sr # Imports speech recognition library in "short hand" to access recognizer objects
	import pyaudio # Imports pyaudio library to allow access to microphone object
	
	reco = sr.Recognizer() # Create a recognizer object
	mic = sr.Microphone() # Create a microphone object

	with mic as source:	# Sets the microphone object as source variable
		reco.adjust_for_ambient_noise(source) # Accesses system's microphone to determine background noise level and feeds value back to recognizer
		print("The energy level has been set to " + str(reco.energy_threshold)) # Displays background noise level in console
		
	with mic as source: # Sets the microphone object as source variable
		print("Recording...") # Shows that its recording in console
		aud = reco.listen(source) # Uses microphone to listen to source and stores input as variable aud
		print("End of Recording")

	try:
		return(reco.recognize_google(aud))# Sends audio data in aud to the google recognizer api and returns string if understood
	except sr.UnknownValueError:# If the recognizer cannot discern words, returns that it can't
		return("Google Speech could not understand audio")
	except sr.RequestError as e: # States request error if applicable Ex: failure to connect to api
		return("Could not request results from Google Speech service; {0}".format(e))
		
