import requests
import base64
import json

def call_astrology_api(day, month, year, hour, min, lat, lon, tzone):
    url = "https://json.astrologyapi.com/v1/horo_chart/D1"
    
    # API and user details
    api = 'horo_chart_image/D1'
    user_id = '636261'
    api_key = '3917aad547a35e0fb3daeec8ec762b2c55e9b964'
    language = 'English'  # Default is English

    # Authentication
    auth = f"Basic {base64.b64encode(f'{user_id}:{api_key}'.encode()).decode()}"
    payload = {
        "day": day,
        "month": month,
        "year": year,
        "hour": hour,
        "min": min,
        "lat": lat,
        "lon": lon,
        "tzone": tzone
    }
    
    # Headers
    headers = {
    "authorization": auth,
    "Content-Type": "application/json",
    "Accept-Language": language,
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()  # Astrology API response
    else:
        return {"error": response.text}
