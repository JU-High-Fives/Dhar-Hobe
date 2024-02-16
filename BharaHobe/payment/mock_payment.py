import random

class MockPaymentGateway:
    """
    Process a mock payment with a specified amount and credit card token. This function simulates a payment process, where there is an 80% chance of success and a 20% chance of encountering various payment errors.

    Args:
        amount (float): The amount to be processed in the payment.
        credit_card_token (str): The token representing the credit card.

    Returns:
        bool: True if the payment is successful, False otherwise.

    Raises:
        MockPaymentError: If the payment encounters an error
    """

    
    def process_payment(amount, credit_card_token):
        success_probability = 0.8

        if random.random() < success_probability:
            return True
        else:
            error_messages = [
                "Insufficient funds",
                "Invalid credit card number",
                "Card expired",
                "Transaction declined",
                "Gateway error",
            ]
            error_message = random.choice(error_messages)
            raise MockPaymentError(error_message)

class MockPaymentError(Exception):
    pass
