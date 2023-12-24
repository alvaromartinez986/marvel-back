import os
import requests
import hashlib
import time
import sys
import django
from requests.exceptions import SSLError
import urllib3

urllib3.disable_warnings()



project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marvel_backend.settings')

# Configure Django
django.setup()



from dotenv import load_dotenv
from marvel_api.models import Character, Comic



# Load environment variables from .env file
load_dotenv()

PUBLIC_KEY = os.getenv('MARVEL_PUBLIC_KEY')
PRIVATE_KEY = os.getenv('MARVEL_PRIVATE_KEY')
BASE_URL = 'https://gateway.marvel.com:443/v1/public'
CHARACTERS_ENDPOINT = '/characters'
COMICS_ENDPOINT = '/comics'
LIMIT = 20  # Adjust the limit based on your needs


def generate_hash(ts):
    hash_md5 = hashlib.md5()
    print(PRIVATE_KEY)
    print(PUBLIC_KEY)
    hash_md5.update(f'{ts}{PRIVATE_KEY}{PUBLIC_KEY}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def fetch_marvel_data(endpoint, option=None):
    ts = int(time.time())
    hash_value = generate_hash(ts)
    params = {
        'ts': ts,
        'apikey': PUBLIC_KEY,
        'hash': hash_value,
    }
    option.update(params)
    
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=option,verify=False, headers = {'User-agent': 'your bot 0.1'})
        response.raise_for_status()  # Raise an error for HTTP errors (4xx and 5xx)
    except SSLError as ssl_error:
    # Handle SSL errors here
        print(f"SSL Error: {ssl_error}")
    # Log the error, retry, or take other appropriate action
    except requests.RequestException as request_error:
    # Handle other request-related errors
        print(f"Request Error: {request_error}")
    # Log the error or take other appropriate action
    else:
    # Continue with the script if there are no errors
        print(response.json())

    return {}

def fetch_and_store_characters():
    data = fetch_marvel_data(CHARACTERS_ENDPOINT, {'name':'spectrum'})
    # characters = data['data']['results']


    # for character_data in characters:
    #     character, created = Character.objects.get_or_create(
    #         name=character_data['name'],
    #         defaults={'description': character_data.get('description', '')}
    #     )
    #     if not created:
    #         # If the character already exists, update the description
    #         character.description = character_data.get('description', '')
    #         character.save()

""" def fetch_and_store_comics():
    data = fetch_marvel_data(COMICS_ENDPOINT)
    comics = data['data']['results']

    for comic_data in comics:
        comic, created = Comic.objects.get_or_create(
            title=comic_data['title'],
            defaults={'description': comic_data.get('description', '')}
        )
        if not created:
            # If the comic already exists, update the description
            comic.description = comic_data.get('description', '')
            comic.save() """

if __name__ == '__main__':
    fetch_and_store_characters()
    # fetch_and_store_comics()
