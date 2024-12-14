import re


# Simulated payment processing function
def process_payment(card_number, amount):
    """
    Simulate a payment processing function.
    - In real-world use, integrate with payment gateway APIs like Stripe, PayPal, etc.
    """
    if len(card_number) == 16 and amount > 0:
        return True, "Payment successful."
    else:
        return False, "Payment failed. Please check the card number or amount."


# Function to generate chatbot responses
def chatbot_response(user_input):
    """
    Handle chatbot logic with responses and payment processing simulation.
    """
    # Predefined patterns and responses
    patterns = {
        r'hello|hi|hey': 'Hello! How can I help you today?',
        r'how are you': 'I am just a bot, but I am doing fine! How can I assist you?',
        r'what is your name': 'I am a chatbot created by OpenAI.',
        r'bye|goodbye': 'Goodbye! Have a great day!',
        r'help': 'Sure! How can I help you? Ask me anything.',
        r'thank you|thanks': 'You are welcome!',
        r'payment': 'Would you like to proceed with payment? (yes/no)'
    }

    # Match user input with patterns
    for pattern, response in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # Default response
    return "I'm sorry, I don't understand that. Could you rephrase it?"


# Simulate a payment flow
def payment_flow():
    """
    Simulate a payment flow with user input for card number and payment amount.
    """
    print("\nPlease enter your card details to process payment.")
    
    while True:
        # Ask for card number
        card_number = input("Enter your 16-digit card number: ")
        
        if not card_number.isdigit() or len(card_number) != 16:
            print("Invalid card number. Please ensure it's a 16-digit number.")
            continue
        
        # Ask for payment amount
        try:
            amount = float(input("Enter the amount to pay: "))
            if amount <= 0:
                print("Amount must be greater than zero. Please try again.")
                continue
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue

        # Process the payment
        success, message = process_payment(card_number, amount)
        print(message)

        if success:
            break
        else:
            print("Let's try again.\n")


# Main chatbot loop
def main():
    print("Chatbot: Hello! I am your AI-powered assistant. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")

        # Handle exit
        if re.search(r'bye|goodbye', user_input, re.IGNORECASE):
            print("Chatbot: Goodbye!")
            break

        # Handle payment flow
        if re.search(r'payment', user_input, re.IGNORECASE):
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}")
            user_choice = input("You: ").strip().lower()
            
            if user_choice == 'yes':
                payment_flow()
            else:
                print("Chatbot: Okay. If you change your mind, let me know.")

        # Regular chatbot response
        else:
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}")


# Run the chatbot
if __name__ == "__main__":
    main()
