import os
import sys
from dotenv import load_dotenv

from summarizer import summarize
from mailer import send_mail
from email_client import get_mail

def main():
    # Load environment variables
    
    load_dotenv(override=True)
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    mail = get_mail(email,password)
    if not mail:
        print("No mail today")
        sys.exit(0)
    contents = mail[1]
    summaries = summarize(contents) # Change the contents to summaries
    #send_mail(zip(mail[0],summaries,mail[2]))

if __name__ == "__main__":
    main()