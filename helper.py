import os.path
import base64
import re
from bs4 import BeautifulSoup
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email import message_from_bytes

# If modifying these SCOPES, delete the token.json file first
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/userinfo.profile',"https://www.googleapis.com/auth/gmail.compose"]


def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If no valid credentials are available, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds),build('people', 'v1', credentials=creds)

import base64

def get_message_body(payload):
    if 'body' in payload and 'data' in payload['body']:
        data = payload['body']['data']
        decoded_bytes = base64.urlsafe_b64decode(data.encode('UTF-8'))
        return decoded_bytes.decode('UTF-8')
    elif 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body']['data']
                decoded_bytes = base64.urlsafe_b64decode(data.encode('UTF-8'))
                return decoded_bytes.decode('UTF-8')
    return None


def get_unread_messages(max_results=10):
    service,peop = get_gmail_service()
    results = service.users().messages().list(userId='me', labelIds=['INBOX', 'UNREAD'],
                                              maxResults=max_results).execute()
    profile = peop.people().get(
        resourceName='people/me',
        personFields='names'
    ).execute()
    if 'names' in profile and profile['names']:
        display_name = profile['names'][0].get('displayName')
        # print(f"User's name: {display_name}")
    else:
        # print("User's name not found.")
        display_name = ""
    messages = results.get('messages', [])

    if not messages:
        print("No unread messages.")
        return
    res = []
    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        msg_data1 = service.users().messages().get(userId='me', id=msg['id'], format='raw').execute()
        # print(msg_data["payload"])
        body = get_message_body(msg_data['payload'])
        raw_msg = base64.urlsafe_b64decode(msg_data1['raw'].encode('ASCII'))
        email_msg = message_from_bytes(raw_msg)

        subject = email_msg.get('Subject')
        sender = email_msg.get('From')
        # print(f"From: {sender}")
        # print(f"Subject: {subject}")
        # print("-" * 40)
        res.append([sender,subject,body])
    return res,display_name

def generate_draft(to,body,subject):
    service,_ = get_gmail_service()
    message = EmailMessage()
    message.set_content(body)
    message['To'] = to
    message['Subject'] = subject
    message['From'] = 'me'  # Gmail API recognizes 'me' as the authenticated user

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_draft_request_body = {
        'message': {
            'raw': encoded_message
        }
    }

    draft = service.users().drafts().create(userId='me', body=create_draft_request_body).execute()
    print(f"Draft created with ID: {draft['id']}")

# if __name__ == '__main__':
    # generate_draft("anandhappriya@gmail.com","I LOVE YOU","PROPOSAL")
