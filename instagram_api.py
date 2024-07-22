import requests

# Access token for Instagram Graph API
ACCESS_TOKEN = 'your_instagram_access_token'
BASE_URL = 'https://graph.instagram.com/'

def get_user_data(user_id):
    """
    Fetches user data from Instagram.
    
    :param user_id: The ID of the user
    :return: JSON response from the API
    """
    try:
        url = f'{BASE_URL}{user_id}?fields=id,username,media_count&access_token={ACCESS_TOKEN}'
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching user data: {e}")
        return {}

def get_user_media(user_id):
    """
    Fetches media data for the user from Instagram.
    
    :param user_id: The ID of the user
    :return: JSON response from the API
    """
    try:
        url = f'{BASE_URL}{user_id}/media?fields=id,caption,media_type,media_url,thumbnail_url,timestamp&access_token={ACCESS_TOKEN}'
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching media data: {e}")
        return {}

if __name__ == "__main__":
    user_id = 'your_user_id'  # Replace with your user ID
    user_data = get_user_data(user_id)
    print("User Data:", user_data)
    media_data = get_user_media(user_id)
    print("Media Data:", media_data)
