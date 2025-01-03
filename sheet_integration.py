from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def append_to_google_sheet(sheet_id, data):
    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = 'service.json'
    
    # Specify the scopes
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    
    # Authenticate and create the Sheets API service
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    
    # Prepare the data to append
    body = {'values': [data]}
    
    # Append data to the Google Sheet
    sheet_range = 'Sheet1!A1'  # Change 'Sheet1' to your desired sheet name
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=sheet_range,
        valueInputOption='USER_ENTERED',
        insertDataOption='INSERT_ROWS',
        body=body
    ).execute()
    return result
