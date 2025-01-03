from call_astrology import call_astrology_api
from interpretation import call_openai_api
from sheet_integration import append_to_google_sheet

def main_workflow(query, day, month, year, hour, min, lat, lon, tzone, feedback, sheet_id):
    # Call Astrology API
    astrology_data = call_astrology_api(day, month, year, hour, min, lat, lon, tzone)
    if "error" in astrology_data:
        return f"Error: {astrology_data['error']}"

    # Call OpenAI API for interpretation
    interpretation = call_openai_api(query, astrology_data)

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
        interpretation,
        query
    ]

    # Save data and feedback to Google Sheet
    result = append_to_google_sheet(sheet_id, data)

    return interpretation

if __name__ == "__main__":
    # Take inputs from the user
    query = input("Enter your query: ")
    day = int(input("Enter day of birth (DD): "))
    month = int(input("Enter month of birth (MM): "))
    year = int(input("Enter year of birth (YYYY): "))
    hour = int(input("Enter hour of birth (HH in 24-hour format): "))
    min = int(input("Enter minute of birth (MM): "))
    lat = float(input("Enter latitude of birthplace: "))
    lon = float(input("Enter longitude of birthplace: "))
    tzone = float(input("Enter timezone of birthplace: "))
    feedback = "Ok"
    sheet_id = "10UpkQKtkqDX4-PD0nh900ENd7Dj09AmQJrbeFOgKRYw"  # Replace with your Google Sheet ID

    # Run the workflow and print interpretation
    interpretation = main_workflow(query, day, month, year, hour, min, lat, lon, tzone, feedback, sheet_id)
    print("Interpretation:", interpretation)
