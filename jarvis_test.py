import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, I am Jarvis running in VS Code.")
engine.runAndWait()
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Make Jarvis speak"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen through microphone and convert speech to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Speech service is down."

# Main loop
speak("Hello ghous sir, I am Jarvis. Say something.")
while True:
    command = listen()

    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        import datetime
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye sir!")
        break
    else:
        speak("You said " + command)