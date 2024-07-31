import smtplib
from email.message import EmailMessage
import os

def send_email(sender, password, recipient, subject, body, attachment_path):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    print(f"Attachment path: {attachment_path}")
    if os.path.exists(attachment_path):
        print("Attachment found.")
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        print(f"Attached file: {file_name}")
    else:
        print("Attachment not found.")

    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    import sys
    print("Sending email with the following parameters:")
    print(f"Sender: {sys.argv[1]}")
    print(f"Recipient: {sys.argv[3]}")
    print(f"Subject: {sys.argv[4]}")
    print(f"Body: {sys.argv[5]}")
    print(f"Attachment: {sys.argv[6]}")
    send_email(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
