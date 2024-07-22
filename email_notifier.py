import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    """
    Sends an email notification.
    
    :param subject: The subject of the email
    :param body: The body of the email
    :param to_email: Recipient's email address
    """
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'your_email@example.com'
        msg['To'] = to_email

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login('your_email@example.com', 'your_password')
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_email('Test Subject', 'This is a test email.', 'recipient@example.com')
