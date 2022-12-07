from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


import base64
from email.message import EmailMessage
import google.auth

from dotenv import load_dotenv
load_dotenv('.env')

# """
# メール作成
# """
# def gmail_create_draft():
#     creds, _ = google.auth.default()

#     try:
#         # create gmail api client
#         service = build('gmail', 'v1', credentials=creds)

#         message = EmailMessage()

#         message.set_content('This is automated draft mail')

#         message['To'] = 'gduser1@workspacesamples.dev'
#         message['From'] = 'gduser2@workspacesamples.dev'
#         message['Subject'] = 'Automated draft'

#         # encoded message
#         encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

#         create_message = {
#             'message': {
#                 'raw': encoded_message
#             }
#         }
#         # pylint: disable=E1101
#         draft = service.users().drafts().create(userId="me",
#                                                 body=create_message).execute()

#         print(F'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

#     except HttpError as error:
#         print(F'An error occurred: {error}')
#         draft = None

#     return draft


# if __name__ == '__main__':
#     gmail_create_draft()



# import base64
# from email.message import EmailMessage

# import google.auth
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# """
# メール送信
# """
# def gmail_send_message():
#     creds, _ = google.auth.default()

#     try:
#         service = build('gmail', 'v1', credentials=creds)
#         message = EmailMessage()

#         message.set_content('This is automated draft mail')

#         message['To'] = 'gduser1@workspacesamples.dev'
#         message['From'] = 'gduser2@workspacesamples.dev'
#         message['Subject'] = 'Automated draft'

#         # encoded message
#         encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
#             .decode()

#         create_message = {
#             'raw': encoded_message
#         }
#         # pylint: disable=E1101
#         send_message = (service.users().messages().send(userId="me", body=create_message).execute())
#         print(F'Message Id: {send_message["id"]}')
#     except HttpError as error:
#         print(F'An error occurred: {error}')
#         send_message = None
#     return send_message


# if __name__ == '__main__':
#     gmail_send_message()


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'gmail.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')
    sender = 'MYMAIL'
    to = 'MYMAIL'
    subject = 'テストメール'
    message_text = 'これはGmail APIによるテストメールです。'



if __name__ == '__main__':
    main()