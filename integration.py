from call_astrology import call_astrology_api
from interpretation import call_openai_api
import json
from immanuel.classes.serialize import ToJSON
from immanuel import charts
def get_interpretation(query,day, month, year, hour, min, lat, lon, tzone):
    astrology_data = call_astrology_api(day, month, year, hour, min, lat, lon, tzone)
    
    
    date_time = f"{year}-{month:02d}-{day:02d} {hour:02d}:{min:02d}"
    
    native = charts.Subject(
        date_time=date_time,
        latitude=str(lat),
        longitude=str(lon)
    )
    
    
    natal = charts.Natal(native)
    
    # astrology_data=json.dumps(natal.objects, cls=ToJSON, indent=4)
    
    if "error" in astrology_data:
        return f"Astrology API Error: {astrology_data['error']}"
    
    interpretation = call_openai_api(query,astrology_data)
    return interpretation
