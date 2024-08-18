import requests

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Error fetching data from API: {response.status_code}")
        return None