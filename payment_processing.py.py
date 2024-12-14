import uuid
import time

# Example class for payment processing
class PaymentProcessor:
    def __init__(self):
        self.transactions = {}

    def generate_transaction_id(self):
        return str(uuid.uuid4())

    def process_payment(self, card_number, expiry_date, cvv, amount):
        """Simulate payment processing"""
        if not self.validate_card(card_number, expiry_date, cvv):
            return "Payment failed: Invalid card details"

        if amount <= 0:
            return "Payment failed: Invalid amount"

        transaction_id = self.generate_transaction_id()
        print("Processing payment...")
        time.sleep(2)  # Simulating processing time

        # For simulation, assume payment is always successful
        self.transactions[transaction_id] = {
            "status": "success",
            "amount": amount,
            "timestamp": time.time()
        }

        return f"Payment successful! Transaction ID: {transaction_id}"

    def validate_card(self, card_number, expiry_date, cvv):
        """Basic validation for demonstration purposes"""
        if len(card_number) != 16 or not card_number.isdigit():
            return False

        if len(cvv) != 3 or not cvv.isdigit():
            return False

        # Here, you could add more checks for expiry date and other details
        return True

    def get_transaction_status(self, transaction_id):
        """Retrieve transaction details"""
        return self.transactions.get(transaction_id, "Transaction not found")

# Example usage
def main():
    processor = PaymentProcessor()

    print("Welcome to the Payment System")
    card_number = input("Enter card number (16 digits): ")
    expiry_date = input("Enter expiry date (MM/YY): ")
    cvv = input("Enter CVV (3 digits): ")
    amount = float(input("Enter payment amount: "))

    result = processor.process_payment(card_number, expiry_date, cvv, amount)
    print(result)

    if "Transaction ID" in result:
        transaction_id = result.split(": ")[1]
        print("Fetching transaction status...")
        time.sleep(1)
        status = processor.get_transaction_status(transaction_id)
        print("Transaction Status:", status)

if __name__ == "__main__":
    main()
