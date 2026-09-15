# this is just nakli stuff. it works for working

import re
import webbrowser
from pathlib import Path

SITEMAP = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "chatgpt": "https://chat.openai.com",
    "spotify": "https://open.spotify.com",
    "instagram": "https://www.instagram.com",
    "reddit": "https://www.reddit.com",
    "netflix": "https://www.netflix.com",
    "github": "https://www.github.com",
    "whatsapp": "https://web.whatsapp.com",
    "amazon": "https://www.amazon.in",
}


def open_website(query: str) -> str:
    query_lower = query.lower()
    for keyword, url in SITEMAP.items():
        if keyword in query_lower:
            webbrowser.open(url)
            return f"Opened {keyword} ({url})"
    return "couldn't figure out which website to open."


def get_weather(query: str) -> str:
    return "call weather api here"


def create_file(query: str) -> str:
    match = re.search(r"(?:called|named)\s+([a-zA-Z0-9_.-]+)", query.lower())
    filename = match.group(1) if match else "new_file.txt"
    if "." not in filename:
        filename += ".txt"

    path = Path(filename)
    path.touch(exist_ok=True)
    return f"created {path.resolve()}"


def search_web(query: str) -> str:
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    return f"opened search results for: {query}"


TOOLMAP = {
    "OPEN_WEBSITE": open_website,
    "WEATHER": get_weather,
    "CREATE_FILE": create_file,
    "SEARCH_WEB": search_web,
}
