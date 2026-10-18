
import requests
import pandas as pd

BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_data(endpoint):
    """Download data from a JSONPlaceholder endpoint."""
    url = f"{BASE_URL}/{endpoint}"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    return response.json()


def load_all_data():
    """Download all datasets used in the dashboard."""
    users = pd.DataFrame(fetch_data("users"))
    posts = pd.DataFrame(fetch_data("posts"))
    comments = pd.DataFrame(fetch_data("comments"))
    todos = pd.DataFrame(fetch_data("todos"))

    return users, posts, comments, todos
