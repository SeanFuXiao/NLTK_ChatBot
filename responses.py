from gpt_integration import get_gpt_response
import random


responses = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! Need any help?",
        "Good to see you! How can I help?"
    ],
    "farewell": [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! Let me know if you need anything else.",
        "Take care! Talk to you soon."
    ],
    "thanks": [
        "You're welcome!",
        "No problem at all!",
        "My pleasure!",
        "Glad I could help!"
    ],
    "help": [
        "Sure! What do you need help with?",
        "Of course! Feel free to ask me anything.",
        "I'm here to help. What can I do for you?",
        "Let me know how I can assist you."
    ],
    "weather": [
        "I'm not sure about the weather. You might want to check your weather app.",
        "It looks cloudy today. Maybe carry an umbrella, just in case!",
        "It's always sunny in my world! 😎",
        "I don't know the weather, but I hope it's nice where you are!"
    ],
    "joke": [
        "Why don’t scientists trust atoms? Because they make up everything! 😂",
        "What do you call fake spaghetti? An impasta! 🍝",
        "Why couldn’t the bicycle stand up by itself? It was two tired! 🚴",
        "Want to hear a joke about construction? Oh wait, I’m still working on it. 🛠️"
    ],
    "news": [
        "I don't have the latest news, but you can check your favorite news website!",
        "There's always something interesting happening. Maybe look at CNN or BBC?",
        "Sorry, I’m not updated with the news right now. Try checking Google News.",
        "I don't have news updates, but I’m here if you want to chat about anything else!"
    ],
    "food": [
        "How about trying pasta tonight? It's easy and delicious!",
        "You could order pizza, or maybe try cooking something new.",
        "I love desserts! How about some ice cream?",
        "A nice salad or soup could be great for dinner!"
    ],
    "time": [
        "It's always time to chat with me! 😊",
        "I’m sorry, I can’t tell the exact time. Check your clock!",
        "Time flies when you’re having fun, doesn’t it?"
    ],
    "date": [
        "I’m not sure about today’s date. Maybe check your calendar?",
        "Every day is a great day, don't you think?",
        "Sorry, I don’t have a calendar handy!"
    ],
    "motivation": [
        "Believe in yourself! Every day is a new opportunity. 🌟",
        "You are capable of amazing things!",
        "Don’t watch the clock; do what it does. Keep going. ⏰",
        "Hard work beats talent when talent doesn’t work hard!"
    ],
    "health": [
        "Drink plenty of water and stay active! 💧",
        "Eat more vegetables and get enough sleep. 🥗",
        "Take breaks and don’t forget to exercise!",
        "Health is wealth. Take care of your body and mind. 🧘"
    ],
    "unknown": [
        "I'm not sure I understand that.",
        "Can you rephrase your question?",
        "I'm sorry, I don't have an answer for that.",
        "That's an interesting question. Let me think about it!"
    ]
}


def get_response(intent, user_input):
 
    if intent == "unknown":
    
        return get_gpt_response(user_input)
    else:
    
        return random.choice(responses.get(intent, ["I'm not sure how to respond to that."]))