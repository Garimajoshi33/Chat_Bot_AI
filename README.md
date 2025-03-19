# Chatbot AI

## Overview
Chatbot AI is an intelligent conversational agent designed to simulate human-like interactions. Powered by natural language processing (NLP) techniques, it can understand and respond to a variety of user queries. This project demonstrates how to build an AI-driven chatbot that can handle a wide range of tasks.

## Key Features
- **Basic Conversations**: The chatbot can respond to common queries such as greetings, asking its name, and telling jokes.
- **Weather Information**: The chatbot fetches weather data from the WeatherAPI (you'll need an API key for it).
- **Sentiment Analysis**: It can detect positive or negative sentiment in the user's messages and respond accordingly.
- **Memory**: The chatbot remembers previous user inputs during the session (stored in memory).

## How It Works
- The chatbot responds based on predefined patterns (stored in the `pairs` variable).
- If the user asks about the weather, it fetches current weather data for the specified city using the WeatherAPI.
- The sentiment analysis function checks if the user's input contains positive or negative words and provides appropriate feedback based on that.

## Suggested Improvements
- **Weather API**: You should replace the `api_key` with your own key from [WeatherAPI](https://www.weatherapi.com/) to make it work.
- **Error Handling**: The API call could fail, so it's a good idea to improve error handling for better user experience.
- **Extend Sentiment Analysis**: More sophisticated sentiment analysis models (like VADER or machine learning models) can be integrated to improve accuracy.
- **Memory Feature**: If you want the chatbot to remember details between sessions, you can store the `memory` in a file or database.

## Technologies Used
- Python 3
- NLTK (Natural Language Toolkit)
- WeatherAPI (for weather data)
- Requests (for API calls)

## Installation

### Prerequisites
- Python 3.6+ installed
- `pip` (Python package manager)

