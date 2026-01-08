import requests

def get_random_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()

    return {
        "name": data["results"][0]["name"]["first"],
        "email": data["results"][0]["email"]
    }
