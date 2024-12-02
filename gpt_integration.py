import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def get_gpt_response(prompt):
 
    try:
       
        chat_history.append({"role": "user", "content": prompt})

        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            max_tokens=150,
            temperature=0.7
        )

    
        reply = response['choices'][0]['message']['content'].strip()

        chat_history.append({"role": "assistant", "content": reply})

        return reply
    except Exception as e:
        return "I'm sorry, I couldn't process your request right now."