import ephem

def get_moon_phase(lat, lon, date):
    # Set the observer's location
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)

    # Set the date for which to calculate the moon phase
    observer.date = date

    # Calculate the moon phase
    moon = ephem.Moon(observer)
    phase = moon.phase

    # Determine the moon phase based on the calculated value
    if phase < 0.01 or phase > 99.99:
        return "New Moon"
    elif phase < 25.00:
        return "Waxing Crescent"
    elif phase < 50.00:
        return "First Quarter"
    elif phase < 75.00:
        return "Waxing Gibbous"
    elif phase < 99.99:
        return "Full Moon"
    else:
        return "Error: Invalid Moon Phase Value"

# Example usage
lat = 40.7128  # latitude of New York City
lon = -74.0060  # longitude of New York City
date = '2023/03/11'  # today's date
moon_phase = get_moon_phase(lat, lon, date)
print("The moon phase on", date, "at", lat, "latitude and", lon, "longitude is:", moon_phase)
