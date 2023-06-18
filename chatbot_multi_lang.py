from flask import Flask, render_template, request
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
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand you.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

# Function for generating bot responses
def generate_response(user_input, language, communication_type):
    # Handle different language and communication type scenarios here
    if language.lower() == "english":
        if "hello" in user_input.lower():
            return "Hello! Welcome to our Product Authenticity Verification Assistant.I am Zui. How can I assist you today?"
        elif "authenticity" in user_input.lower() or "verify" in user_input.lower() and ("watch" in user_input.lower() or "food" in user_input.lower() or "iphone" in user_input.lower() or "shoes" in user_input.lower()):
            return "Of course! Please provide me with the brand, model, or any unique identifiers on the product, and if possible, upload a photo of it."
        elif ("Nike" in user_input.lower() or "nike" in user_input.lower()) :
            return "Follow the steps:\n 1.Locate the tag inside your shoe. All authentic Nike shoes have a tag sewn into them with their size, barcode and model number on it.\n2.There must be a six digit number followed by a three digit number (Example: AQ3366--601).\n3.Go to this website https://www.nike.com/au/help/a/nike-product-authenticity and enter the no. "
        elif "louis vuitton" in user_input.lower() or "photo" in user_input.lower():
            return "Thank you for the information. Let me analyze the details and check the authenticity of the Louis Vuitton handbag for you."
        elif "iphone" in user_input.lower():
            return "Follow the steps:\n1.Look for the device number\n2.Go to this website https://checkcoverage.apple.com/in/en/ and enter the no."
        elif "food" in user_input.lower() :
            return "Follow the steps:\n1.There must be an FSSAI mark on the food packet.Check for it.\n2."
        elif "thank you" in user_input.lower():
            return "You're welcome! If you have any more questions or need further assistance, please feel free to ask. I'm here to help you."
        elif "goodbye" in user_input.lower() or "thanks" in user_input.lower():
            return "You're welcome! If you ever need assistance in the future, don't hesitate to reach out. Have a great day!"
        elif "quit" in user_input.lower():
            return "Bye!!!:)"
        else:
            return "Sorry, I don't know how to assist with that."
    elif language.lower() == "hindi":
        if "hello" in user_input.lower():
            return "नमस्ते! हमारे प्रोडक्ट सत्यापन सहायता सहायक में आपका स्वागत है। मैं Zui हूँ। आज आपकी कैसे सहायता कर सकता हूँ?"
        elif "authenticity" in user_input.lower() or "verify" in user_input.lower() and ("watch" in user_input.lower() or "food" in user_input.lower() or "iphone" in user_input.lower() or "shoes" in user_input.lower()):
            return "जरूर! कृपया मुझे प्रोडक्ट पर ब्रांड, मॉडल या कोई अद्वितीय पहचानकर्ता दें और यदि संभव हो सके तो उसकी एक फोटो अपलोड करें।"
        elif ("Nike" in user_input.lower() or "nike" in user_input.lower()):
            return "परामर्श का पालन करें:\n 1. अपने जूते में टैग ढूंढें। सभी मान्य नाइकी जूतों में एक टैग बना होता है, जिसमें उनका आकार, बारकोड और मॉडल नंबर होता है।\n 2. उसमें एक छह अंकी संख्या और एक तीन अंकी संख्या होनी चाहिए (उदाहरण: AQ3366-601)।\n 3. इस वेबसाइट पर जाएं https://www.nike.com/au/help/a/nike-product-authenticity और नंबर दर्ज करें।"
        elif "louis vuitton" in user_input.lower() or "photo" in user_input.lower():
            return "जानकारी के लिए धन्यवाद। मैं विवरणों का विश्लेषण करेंगा और आपके लिए लुई विटन हैंडबैग की प्रामाणिकता की जांच करेंगा।"
        elif "iphone" in user_input.lower():
            return "परामर्श का पालन करें:\n 1. उपकरण नंबर देखें।\n 2. इस वेबसाइट पर जाएं https://checkcoverage.apple.com/in/en/ और नंबर दर्ज करें।"
        elif "food" in user_input.lower():
            return "परामर्श का पालन करें:\n 1. खाद्य पैकेट पर FSSAI मार्क होना चाहिए। इसे देखें।\n 2. [खाद्य की प्रामाणिकता के लिए अतिरिक्त चरणों को प्रदान करें।]"
        elif "thank you" in user_input.lower():
            return "आपका स्वागत है! यदि आपके पास कोई और सवाल है या आपकी आवश्यकता के लिए और सहायता चाहिए, तो कृपया पूछें। मैं आपकी सहायता करने के लिए यहाँ हूँ।"
        elif "goodbye" in user_input.lower() or "thanks" in user_input.lower():
            return "आपका स्वागत है! यदि आपको भविष्य में किसी भी सहायता की आवश्यकता हो, तो बेझिझक आपसे संपर्क करें। शुभ दिन हो!"
        else:
            return "क्षमा करें, मुझे उसमें मदद करने का तरीका नहीं पता है।"
    else:
        return "Invalid language preference. Please choose either English or Hindi."


def process():
    language = request.form['language']
    communication_type = request.form['communication_type']
    speak("Welcome! How would you like to communicate? Text or voice?")
    while True:
        user_input = listen()
        if "writing" in user_input.lower():
            print("Great! Let's switch to text-based communication.")
            # Call the generate_response function with the appropriate language and communication type
            response = generate_response(user_input, language, communication_type)
            # Return the response to the frontend
            return response
        elif "voice" in user_input.lower():
            print("Sure! Let's continue with voice-based communication.")
            # Call the voice_interaction function here
            break


