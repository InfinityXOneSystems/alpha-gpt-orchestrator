import logging

        logging.info(f'[SENDGRID EMAIL] To={to} | Subject={subject}')
    def send_email(self, to: str, subject: str, body: str):
        logging.info(f'[SENDGRID EMAIL] To={to} | Subject={subject}')
