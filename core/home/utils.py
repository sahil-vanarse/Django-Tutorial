from home.models import Student
import time
from django.core.mail import send_mail, EmailMessage #type: ignore
from django.conf import settings #type: ignore

sender_email = settings.EMAIL_HOST_USER

def run_this_function():
    print("Function Started")
    time.sleep(30)
    print("Function Executed")


def send_email_to_client():
    subject = "This email is from the Django Server"
    message = "This is the test email from the Django server"
    from_sender = sender_email
    recipients_list = ["sahilvanarse4@gmail.com"]
    send_mail(subject, message, from_sender, recipients_list)


def send_email_with_attachment(subject, message, receipients_list, filepath):
    mail = EmailMessage(subject=subject,
                        body=message,
                        from_email=sender_email ,
                        to=receipients_list)
    
    mail.attach_file(filepath)
    mail.send()