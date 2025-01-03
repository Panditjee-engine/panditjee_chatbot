from call_astrology import call_astrology_api
from interpretation import call_openai_api
from sheet_integration import append_to_google_sheet

def main_workflow(day, month, year, hour, min, lat, lon, tzone, feedback, sheet_id):
    # Call Astrology API
    astrology_data = call_astrology_api(day, month, year, hour, min, lat, lon, tzone)
    if "error" in astrology_data:
        return f"Error: {astrology_data['error']}"
    
   
    
    # Call OpenAI API for interpretation
    interpretation = call_openai_api(astrology_data)
    
    
    
     # Data to append (modify as needed)
    data = [
        day,  # Column 1
        month,
        year,
        hour,
        min,
        lat,
        lon,
        tzone,
        feedback,
        interpretation
        # Column 3
    ]
    
    # Save data and feedback to Google Sheet
    result = append_to_google_sheet(sheet_id, data)
    
    return f"Data saved successfully: {result}"


if __name__ == "__main__":
    # Example user inputs
    day, month, year, hour, min, lat, lon, tzone = 25, 10, 1998, 7, 37, 25.7464, 82.6837, 5.5
    feedback = "Not Ok"  # Feedback from the user
    sheet_id = "10UpkQKtkqDX4-PD0nh900ENd7Dj09AmQJrbeFOgKRYw"  # Replace with your Google Sheet ID

    # Run the workflow
    print(main_workflow(day, month, year, hour, min, lat, lon, tzone, feedback, sheet_id))

