import smtplib
from email.message import EmailMessage
import dotenv
import os

class NotificationManager:
    def __init__(self):
        dotenv.load_dotenv()

    def send_email(self, price, departure, arrival, outbound_date, inbound_date):
        sender_email = os.getenv(key="EMAIL")
        receiver_email = os.getenv(key="EMAIL")
        password = os.getenv(key="PASSWORD_EMAIL")

        subject = "✈️ Cheap Flight Alert!"
        body = f"""
        Low price alert!

        Flight from {departure} to {arrival}

        Price: ${price}
        Departure date: {outbound_date}
        Land date: {inbound_date}

        Book quickly before the price increases!
        """

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(body)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(sender_email, password)
            connection.send_message(msg)

            print("Successfully sent an email")