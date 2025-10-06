import pyttsx3

# Initialize Windows voice engine
engine = pyttsx3.init(driverName='sapi5')

# Pick first available voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)  # Speech speed

# Speak a test sentence
engine.say("Hello! This is a test of Jarvis speaking on Windows.")
engine.runAndWait()
print("✅ Finished speaking")