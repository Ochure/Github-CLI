import sys
import requests

BASE_URL ="https://api.github.com"

def get_user_events(username):
    BASE_URL = "https://api.github.com"
    input_url = f"{BASE_URL}/users/{username}/events/public"
    response = requests.get(input_url)

    if response.status_code == 200:
        activities = response.json()
        for event in activities:
            print(f"Event: {event['type']} - Repo: {event['repo']['name']}")
    else:
        print("Could not retrieve user activity")

def get_user_info(username):
    url = f"{BASE_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_info = response.json()
        print(f"User: {user_info['login']}")
        print(f"Name: {user_info.get('name', 'N/A')}")
        print(f"Public Repos: {user_info['public_repos']}")
        print(f"Followers: {user_info['followers']}")
        print(f"Following: {user_info['following']}")
    else:
        print("User not found")

def get_repos(username):
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(f"Repo: {repo['name']} - URL: {repo['html_url']}")
    else:
        print("Could not retrieve repositories")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_user_events(username)
    get_user_info(username)
    get_repos(username)
