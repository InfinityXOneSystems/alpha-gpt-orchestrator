import logging

        logging.info(f'[TWILIO CALL] {number}: {message}')
    def call(self, number: str, message: str):
        logging.info(f'[TWILIO CALL] {number}: {message}')

class TwilioSMSAgent:
    def send(self, number: str, message: str):
        logging.info(f'[TWILIO SMS] {number}: {message}')
