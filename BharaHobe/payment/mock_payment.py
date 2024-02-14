import random

class MockPaymentGateway:
    @staticmethod
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
