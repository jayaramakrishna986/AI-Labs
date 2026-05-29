import requests

def get_traffic_flow(api_key, latitude, longitude):
    # Base URL for TomTom Flow Segment Data API
    base_url = f"https://api.tomtom.com/traffic/services/4/incidentViewport/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/-939584.4813015489,-23954526.723651607,14675583.153020501,25043442.895825107/2/true/xml?key={API_KEY}"
    
    # Query parameters
    params = {
        "key": api_key,
        "point": f"{latitude},{longitude}",
        "unit": "KMPH",  # Options: KMPH or MPH
        "thickness": 10
    }
    
    try:
        response = requests.get(base_url, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            flow_info = data.get("flowSegmentData", {})
            
            print(f"Current Speed: {flow_info.get('currentSpeed')} km/h")
            print(f"Free Flow Speed: {flow_info.get('freeFlowSpeed')} km/h")
            print(f"Current Travel Time: {flow_info.get('currentTravelTime')} seconds")
            return data
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Example usage (Replace with your actual TomTom API key)
API_KEY = "6ZATwMeyF9cDSu9EXqpRzVS9T2Tgcsop"
LAT = 52.41072  # Example: Amsterdam
LON = 4.84239

traffic_data = get_traffic_flow(API_KEY, LAT, LON)
