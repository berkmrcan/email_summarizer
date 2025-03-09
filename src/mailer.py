import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os 

# Create the email
def send_mail(mail):
    load_dotenv(override=True)
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = os.getenv("SMTP_PORT")
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS
    msg["Subject"] = "Paper Automation"

    # Email body
    html_content = process_mail(mail)
    msg.attach(MIMEText(html_content, "html"))

    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()  # Secure connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login

        # Send email
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

def process_mail(mail):
    html_content = "<h2>Research Papers Summary</h2><ul>"

    for title, summary, link in mail:
        html_content += f"""
        <li>
            <strong>{title}</strong><br>
            {summary}<br>
            🔗 <a href="{link}" target="_blank">Read more</a>
        </li><br>
        """

    html_content += "</ul>"
    return html_content