Void — AI Voice Assistant

Void is a Python-based intelligent voice assistant powered by Google Gemini 2.5 Flash.
It enables real-time voice interaction, contextual conversations, system and browser automation, and natural text-to-speech responses—while intelligently filtering special characters for smooth and human-like speech output.

Designed for learning, productivity, and experimentation, Void is lightweight, modular, and beginner-friendly.

Features
 Voice Input using SpeechRecognition
Natural Voice Output using pyttsx3
 Conversational Memory (context-aware AI chat)
 Powered by Google Gemini 2.5 Flash
 Open Websites (Google, YouTube, GitHub, etc.)
 Open System Apps (Notepad, Calculator, CMD, Paint)
 Cleans Markdown & Special Characters before speaking
Saves AI Responses to Files (formatted text preserved)
 Graceful Error Handling (no crashes on silence or recognition failure)

Tech Stack
Python 3.10+
Google Gemini API
speech_recognition
pyttsx3
pyaudio
google-genai

 Project Structure Void
│
├── Void.py            # Main voice assistant script
├── config.py          # Stores Gemini API key
├── ai_response.txt    # Fallback response storage
├── Openai/            # Auto-created AI response files
└── README.md

 Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/void-ai-assistant.git
cd void-ai-assistant

2️. Install Dependencies
pip install speechrecognition pyttsx3 pyaudio google-genai


Windows users:
Make sure PyAudio is installed correctly. Precompiled wheels are recommended.

3️. Get Gemini API Key

Visit 👉 https://aistudio.google.com/app/apikey

Create an API key

Create a config.py file in the project root:

apikey = "YOUR_GEMINI_API_KEY"

4️. Run the Assistant
python Void.py

 Usage Examples
You can speak commands like:
“ask ai what is machine learning”
“what is artificial intelligence”
“open youtube”
“open notepad”
“exit”

Void will:
Respond using voice
Print responses in the terminal
Save AI outputs to files automatically

 How It Works
Captures user voice input using speech recognition
Sends prompts to Gemini 2.5 Flash
Maintains conversation history for contextual replies
Cleans AI output before speaking to avoid reading symbols
Saves formatted responses for later reference

 Use Cases
Personal AI voice assistant
Learning & study companion
Hands-free system control
AI experimentation with conversational memory
Beginner-to-intermediate AI / ML projects

 Future Improvements
 Wake word detection (“Hey Void”)
Background listening mode
 GUI (Jarvis-style interface)
Offline fallback using local models
Emotion & tone-based speech responses

Author
Love Solanki
B.Tech CSE (Data Science)
Aspiring Data Scientist & AI Developer

 License
This project is open-source and available for learning, experimentation, and personal use.
