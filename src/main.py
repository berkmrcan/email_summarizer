import os

from email_client import connect_to_gmail, fetch_emails

from dotenv import load_dotenv

def main():
    # Load environment variables
    load_dotenv()
    email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")


if __name__ == "__main__":
    main()