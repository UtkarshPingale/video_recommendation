import os
import requests
import json
from datetime import datetime
from app.config import settings

headers = {"Flic-Token": settings.flic_token}

def get_data(endpoint: str, page: int = 1, page_size: int = 1000):
    url = f"{settings.api_base_url}/{endpoint}?page={page}&page_size={page_size}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {"error": response.text}

def download_all_posts():
    """Download all post-related data and save it locally."""
    endpoints = [
        "posts/view",
        "posts/like",
        "posts/inspire",
        "posts/rating",
        "posts/summary/get",
        "users/get_all"
    ]

    saved_files = []
    os.makedirs("downloads", exist_ok=True)

    for ep in endpoints:
        data = get_data(ep)
        filename = f"downloads/{ep.replace('/', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        saved_files.append(filename)

    return saved_files

def list_downloaded_files():
    os.makedirs("downloads", exist_ok=True)
    return os.listdir("downloads")

def read_saved_file(filename: str):
    path = os.path.join("downloads", filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"error": "File not found"}
