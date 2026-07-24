import webbrowser
import urllib.parse


def open_website(url: str):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    webbrowser.open(url)
    return f"Opened {url}"


def google_search(query: str):
    url = (
        "https://www.google.com/search?q="
        + urllib.parse.quote(query)
    )

    webbrowser.open(url)

    return f"Searching Google for: {query}"