import imaplib
import email
from datetime import datetime, timedelta

def get_mail(username,password):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username,password)
    mail.select("inbox")
    today_date = (datetime.now() - timedelta(2)).strftime("%d-%b-%Y") 
    status, messages = mail.search(None, f"FROM @arxiv.org ON {today_date}")
    if status == "OK" and messages[0] != b'':
        num = messages[0]
        _ , data = mail.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        # Assert it is the right sender
        assert f"From: {msg['from']}" == "From: send mail ONLY to cs <no-reply@arXiv.org>"

        to_parse = msg.get_payload(decode=True).decode()

        # Parse the mail
        return parse_mail(to_parse)
    else:
        return None
    
def parse_mail(mail):
    papers = mail.split("%%--%%--%%")[0]
    papers = papers.split(r"\\")[1:]
    titles = papers[::3] # Get titles
    contents = papers[1::3] # Get contents
    links = papers[2::3] # Get links

    # Process titles
    for i in range(len(titles)):
        titles[i] = titles[i].split("Title:")[1]
        titles[i] = titles[i].split("Authors")[0]
        titles[i] = titles[i].rstrip()
        
    # Process links

    for i in range(len(links)):
        links[i] = links[i].split("(")[1]
        links[i] = links[i].split(" ,")[0]
        
    return titles, contents, links