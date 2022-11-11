import imaplib # a way to open up your inbox
import email
import config

host = 'imap.gmail.com'
username = config.EMAIL
password = config.EMAIL_PASSWORD

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select('inbox')

_, search_data = mail.search(None, 'UNSEEN')


def get_inbox():
    my_messages = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        _, b = data[0]
        email_msg = email.message_from_bytes(b)
        
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_msg[header]))
            email_data[header] = email_msg[header]
        
        for part in email_msg.walk():
            if part.get_content_type() == "text/plain" or part.get_content_type() == "html":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode().strip()

        my_messages.append(email_data)
        
    return my_messages
            
    

if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)