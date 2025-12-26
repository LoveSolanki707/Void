import speech_recognition as sr
import pyttsx3
import webbrowser
import time
from google import genai
from config import apikey
import os
import re

def clean_for_speech(text):
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    # Remove markdown & special symbols
    text = re.sub(r"[#*_>`~\-]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

chatstr = ""
def chat(query):
    global chatstr
    print(chatstr)
    gemini_client = genai.Client(api_key=apikey)

    chatstr += f"L0ki: {query}\n Void: "
    response = gemini_client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=chatstr
    )

    reply = response.text
    chatstr += f"{reply}\n"

    return reply

# Initialize Gemini client
gemini_client = genai.Client(api_key=apikey)

# ---------- AI Function ----------
def ai(prompt):
    response = gemini_client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text

    # Save response
    with open(f"{prompt}.txt", "w", encoding="utf-8") as f:
        f.write(f"User: {prompt}\nAI: {reply}\n\n")

    return reply


def say(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-IN')
        print("User said:", query)
        return query.lower()
    except: 
        return None

say("Hello bro, I am Void, your personal voice assistant")

while True:
    query = takecommand()
    if query is None:
        say("I didn't catch that. Please say that again.")
        continue 

    if "exit" in query or "quit" in query:
        say("Goodbye. Have a nice day.")
        break

        
    sites = {

    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "amazon": "https://www.amazon.com",
    "flipkart": "https://www.flipkart.com",
    "stackoverflow": "https://stackoverflow.com",
    "github": "https://github.com"
}
    apps = {"notepad": "notepad.exe",
                        "calculator": "calc.exe",
                        "command prompt": "cmd.exe",
                        "paint": "mspaint.exe"
                        }
    if query.startswith("open"):
        name = query.replace("open", "", 1).strip()
        name = name.split()[0]

# Check and open the site 
        if name in sites:
            say(f"Opening {name}")
            webbrowser.open(sites[name])
# Check and open the app
        elif name in apps:
            say(f"Opening {name}")
            os.system(f"start {apps[name]}")
# If not found, search on Google
        else:
            say(f"Searching {name} on Google")
            webbrowser.open(f"https://www.google.com/search?q={name}")
    
    elif query.startswith("ask A.I") or query.startswith("ask ai") or query.startswith("ask Ai"):
        # Remove the trigger phrase and get the actual prompt
        prompt = query.replace("ask A.I", "", 1).replace("ask ai", "", 1).replace("ask Ai", "", 1).strip()
        reply = ai(prompt)
        print("AI thinking:", reply)
        say(reply)

    else: 
        reply = chat(query)
        print("AI thinking:", reply)
        say(reply)

        time.sleep(1)