from __future__ import print_function

import json
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
# Store spreadsheet_id as env variable on Heroku
SAMPLE_SPREADSHEET_ID = os.environ.get('token')
SAMPLE_RANGE_NAME = 'Sheet1'


class GoogleSheetsDataProvider:

    def authenticate(self):
        """Shows basic usage of the Sheets API.
            Prints values from a sample spreadsheet.
            """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        # This part is used to authenticate from Heroku. Comment this part of the code out to run on local
        # environment or to get token.json file prior to running on Heroku.
        # token = os.environ.get('token')
        # token_json = json.loads(token)
        # creds = Credentials.from_authorized_user_info(token_json, SCOPES)

        # Comment the above part of the code.
        # Uncomment and run this part of the code prior to running it on Heroku to get the credentials.
        # Open the token.json file, copy and save the content as an env variable on Heroku.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    def get_jobs(self, creds):
        try:
            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range=SAMPLE_RANGE_NAME,
                                        valueRenderOption='FORMULA').execute()
            values = result.get('values', [])
            if not values:
                print('No data found.')
                return

            return values
        except HttpError as err:
            print(err)