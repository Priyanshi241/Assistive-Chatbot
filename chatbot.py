import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-GB")
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

# Function for generating bot responses
# Function for generating bot responses
def generate_response(user_input):
    if "switch" in user_input.lower() or "written communication" in user_input.lower():
        return text_interaction();
    elif "hello" in user_input.lower():
        return "Hello! Welcome to our Product Authenticity Verification Assistant.I am Zui. How can I assist you today?"
    elif "authenticity" in user_input.lower() and ("watch" in user_input.lower() or "food" in user_input.lower() or "iphone" in user_input.lower() or "shoes" in user_input.lower()):
        return "Of course! Please provide me with the brand, model, or any unique identifiers on the product, and if possible, upload a photo of it."
    elif ("Nike" in user_input.lower() or "nike" in user_input.lower()) :
        return "Follow the steps:\nStep 1:Locate the tag inside your shoe. All authentic Nike shoes have a tag sewn into them with their size, barcode and model number on it.\nStep 2:There must be a six digit number followed by a three digit number (Example: AQ3366--601).\nStep 3:Go to this website https://www.nike.com/au/help/a/nike-product-authenticity and enter the no. "
    elif "louis vuitton" in user_input.lower() or "photo" in user_input.lower():
        return "Thank you for the information. Let me analyze the details and check the authenticity of the Louis Vuitton handbag for you."
    elif "iphone" in user_input.lower():
        return "Follow the steps:\nStep 1: Look for the device number\nStep 2:.Go to this website https://checkcoverage.apple.com/in/en/ and enter the no."
    elif "verify the food" in user_input.lower() :
        return "Follow the steps:\nStep 1:There must be an FSSAI mark on the food packet.Check for it.\n2.What is the food item?"
    elif("milk" in user_input.lower()):
        return "1.It should  smell good or normal no pungent smell.\n2.The difference between the manufacturing date and expiry date should atmost 2-3 days"
    elif("cookies" in user_input.lower()):
        return "To verify the safety of the cookies, could you please provide me with some additional information? Specifically, I'll need the ingredients list, any allergen warnings, and the expiration date, if available."
    elif("milk" in user_input.lower() or "egg" in user_input.lower() or "choco chips" in user_input.lower()):
        return "Thank you for providing the details. Based on the information you've provided, the cookies contain wheat, eggs, and there don't seem to be any additional allergens mentioned.\n *The expiry date must be atmost six-seven months."
    elif "thank you" in user_input.lower():
        return "You're welcome! If you have any more questions or need further assistance, please feel free to ask. I'm here to help you."
    elif "goodbye" in user_input.lower() or "thanks" in user_input.lower():
        return "You're welcome! If you ever need assistance in the future, don't hesitate to reach out. Have a great day!"
    elif "quit" in user_input.lower():
        return "Bye!!!:)"
    else:
        return "Sorry, I don't know how to assist with that."
    


# Function for text-based interaction
def text_interaction():
    print("Zui:Hello! Welcome to our Product Authenticity Verification Assistant.I am Zui. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = generate_response(user_input)
        print("Zui:", response)
        if "quit" in user_input.lower():
            break

# Function for voice-based interaction
def voice_interaction():
    speak("Hello! Welcome to our Product Authenticity Verification Assistant. I am Zui. How can I assist you today?")
    speak("Please speak clearly and provide relevant information for accurate assistance.")
    while True:
        user_input = listen()
        response = generate_response(user_input)
        speak("Zui: " + response)
        if "quit" in user_input.lower():
            break

# Starting point of the program
speak("Welcome! How would you like to communicate? in writing or voice?")
while True:
    user_input = listen()
    if "writing" in user_input.lower():
        speak("Great! Let's switch to text-based communication.")
        text_interaction()
        break
    elif "voice" in user_input.lower():
        speak("Sure! Let's continue with voice-based communication.")
        voice_interaction()
        break