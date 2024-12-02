from model import train_model, extract_features
from responses import get_response

def chatbot_response(user_input, classifier):
  
    features = extract_features(user_input)
    intent = classifier.classify(features)
    return get_response(intent, user_input)

if __name__ == "__main__":
    print("Training chatbot...")
    classifier = train_model()

    print("Chatbot ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input, classifier)
        print(f"Chatbot: {response}")