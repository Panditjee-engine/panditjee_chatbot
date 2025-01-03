import requests
import base64
import json

# Function to get user input
def get_user_input():
    print("Please provide the following details:")
    day = int(input("Day of birth (e.g., 25): "))
    month = int(input("Month of birth (e.g., 10 for October): "))
    year = int(input("Year of birth (e.g., 2001): "))
    hour = int(input("Hour of birth (24-hour format, e.g., 7): "))
    minute = int(input("Minute of birth (e.g., 37): "))
    lat = float(input("Latitude (e.g., 28.534491880873553): "))
    lon = float(input("Longitude (e.g., 77.25222412700371): "))
    tzone = float(input("Time zone (e.g., 5.5 for IST): "))


    return {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": minute,
        "lat": lat,
        "lon": lon,
        "tzone": tzone,
        "planetColor": "#ff0000",
        "signColor": "#00ff00",
        "lineColor": "#0000ff",
         "chartType": "north"
    }

# API and user details
api = 'horo_chart_image/D1'
user_id = '636261'
api_key = '3917aad547a35e0fb3daeec8ec762b2c55e9b964'
language = 'English'  # Default is English

# Authentication
auth = f"Basic {base64.b64encode(f'{user_id}:{api_key}'.encode()).decode()}"

# Headers
headers = {
    "authorization": auth,
    "Content-Type": "application/json",
    "Accept-Language": language,
}

# Collect user input and send API request
data = get_user_input()
url = f"https://json.astrologyapi.com/v1/{api}"
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)
