import requests

def get_random_user():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    data = response.json()
    return {
        "name": data["results"][0]["name"]["first"],
        "email": data["results"][0]["email"]
    }
