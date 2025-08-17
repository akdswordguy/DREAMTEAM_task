import requests
import folium


def get_user_location():
    """
    Fetch the user's current location using IP-based geolocation.

    Returns:
        dict: Dictionary containing latitude, longitude, city, region, and country.
    """
    response = requests.get("http://ip-api.com/json/")
    data = response.json()

    if data["status"] == "fail":
        raise Exception("Unable to fetch location from API.")

    return {
        "lat": data["lat"],
        "lon": data["lon"],
        "city": data["city"],
        "region": data["regionName"],
        "country": data["country"]
    }


def plot_location_on_map(location, filename="user_location.html"):
    """
    Plot the location on an interactive map and save it to an HTML file.

    Args:
        location (dict): User location containing lat, lon, city, region, country.
        filename (str): Output HTML filename.
    """
    user_map = folium.Map(location=[location["lat"], location["lon"]], zoom_start=12)

    folium.Marker(
        [location["lat"], location["lon"]],
        popup=f"{location['city']}, {location['region']}, {location['country']}",
        tooltip="You are here!"
    ).add_to(user_map)


    user_map.save(filename)
    print(f"Map generated and saved as '{filename}'.")


if __name__ == "__main__":
    try:
        loc = get_user_location()
        print(f" Current Location: {loc['city']}, {loc['region']}, {loc['country']}")
        plot_location_on_map(loc)
    except Exception as e:
        print(str(e))
