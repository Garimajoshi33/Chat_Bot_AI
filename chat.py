import nltk
import random
import string  
import requests
from nltk.chat.util import Chat, reflections

# Defining the chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, how about you?", "I'm fine, thanks for asking!"]
    ],
    [
        r"(.*) your name ?",
        ["I am a chatbot, you can call me ChatBot.", "I’m ChatBot, your virtual assistant!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, tell jokes, fetch weather updates, and more!"]
    ],
    [
        r"tell me a joke",
        ["Why did the scarecrow win an award? Because he was outstanding in his field!", "I told my wife she should embrace her mistakes. She gave me a hug!"]
    ],
    [
        r"hahaha",
        ["Well i can make some really good jokes,hahaha"]
    ],
    [
        r"tell me a fact",
        ["Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly good to eat.", "Bananas are berries, but strawberries are not!"]
    ],
    [
        r"waaooo",
        ["i'm smart you know :)"]
    ],
    [
        r"weather in (.*)",
        ["Let me check the weather for you!"]
    ],
    [
        r"you are pretty good",
        ["yeah i know, '>'"]
    ],
    [
        r"quit",
        ["Goodbye!", "See you later!", "Bye, take care!"]
    ]
]

chatbot = Chat(pairs, reflections)
memory = []    ## Tracking up the memory

def get_weather(city):
    api_key = "8025cd789f3a486392172935250203" ## API key for the weather
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url).json()
        return f"The temperature in {city} is {response['current']['temp_c']}°C with {response['current']['condition']['text']}."
    except:
        return "Sorry, I couldn't fetch the weather right now."

## Analysing the moods
def analyze_sentiment(text):
    positive_words = ["good", "great", "happy", "awesome", "fantastic", "love"]
    negative_words = ["sad", "bad", "angry", "upset", "terrible", "hate"]
    score = sum(1 for word in text.lower().split() if word in positive_words) - sum(1 for word in text.lower().split() if word in negative_words)
    if score > 0:
        return "You seem happy! 😊"
    elif score < 0:
        return "I'm sorry to hear that. 😟"
    else:
        return ""

def chatbot_response():
    print("ChatBot: Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("ChatBot: Goodbye!")
            break
        memory.append(user_input)

        if "weather in" in user_input.lower():  ## For weather reports
            city = user_input.split("weather in ")[-1]
            response = get_weather(city)
        else:
            response = chatbot.respond(user_input) or "I'm not sure about that!"
        
        sentiment = analyze_sentiment(user_input)
        
        print("ChatBot:", response)
        if sentiment:
            print("ChatBot:", sentiment)

if __name__ == "__main__":
    chatbot_response()
