import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ssl import create_default_context

from ...mail_templates.templates import MailBuilder

SMTP_SERVER = os.getenv("MAIL_HOST")
SMTP_PORT = int(os.getenv("MAIL_PORT", 465))
SENDER_EMAIL = os.getenv("MAIL_USER")
SENDER_PASSWORD = os.getenv("MAIL_PASS")
SENDER_NAME = os.getenv("MAIL_NAME")

class MailNotification:
    def __init__(self):
        self.smtp_server = SMTP_SERVER
        self.smtp_port = SMTP_PORT
        self.sender_email = SENDER_EMAIL
        self.sender_password = SENDER_PASSWORD
        self.sender_name = SENDER_NAME

    def send_notification(self, recipient_email, subject, message):
        try:
            msg = MIMEMultipart()
            msg["From"] = f"{self.sender_name} <{self.sender_email}>"
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "html"))

            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=create_default_context()) as server:
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())

        except Exception as e:
            print(f"Failed to send email: {e}")

class ResetPasswordNotification(MailNotification):
    def send_notification(self, recipient_email, recipient_name, reset_password_link):
        builder = MailBuilder()
        subject = "Reset Password Notification"
        message = builder.reset_password(recipient_name=recipient_name, reset_password_link=reset_password_link)
        
        super().send_notification(recipient_email, subject, message)

class ActivationNotification(MailNotification):
    def send_notification(self, recipient_email, recipient_name, activation_link):
        builder = MailBuilder()
        subject = "Activation Notification"
        message = builder.verify_email(recipient_name=recipient_name, activation_link=activation_link)
        super().send_notification(recipient_email, subject, message)

