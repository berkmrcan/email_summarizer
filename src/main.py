import os
from dotenv import load_dotenv

from email_client import get_mail

def main():
    # Load environment variables
    
    load_dotenv(override=True)
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    get_mail(email,password)


if __name__ == "__main__":
    main()