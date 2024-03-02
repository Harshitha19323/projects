import random

# Define responses for different types of user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm good, thanks for asking!", "All good, thanks!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"]
}

# Function to generate a response based on user input
def get_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()
    
    # Check if user input matches any predefined responses
    for key in responses:
        if user_input in key:
            return random.choice(responses[key])
    
    # If no predefined response matches, return a default response
    return "I'm sorry, I don't understand that."

# Main function to handle the chatbot interaction
def chat():
    print("Chatbot: Hi! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        # Exit the loop if user says "bye"
        if user_input.lower() == "bye":
            print("Chatbot:", get_response(user_input))
            break
        
        # Generate and print response based on user input
        print("Chatbot:", get_response(user_input))

# Start the chatbot
if __name__ == "__main__":
    chat()
