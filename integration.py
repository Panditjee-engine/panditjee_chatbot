from call_astrology import call_astrology_api
from interpretation import call_openai_api
def get_interpretation(query,day, month, year, hour, min, lat, lon, tzone):
    astrology_data = call_astrology_api(day, month, year, hour, min, lat, lon, tzone)
    
    if "error" in astrology_data:
        return f"Astrology API Error: {astrology_data['error']}"
    
    interpretation = call_openai_api(query,astrology_data)
    return interpretation
