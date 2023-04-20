import feedparser
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Hello": "world"}


@app.get("/read/{url:path}")
def read_rss_feed(url: str):
    feed = feedparser.parse(url).feed

    return {
        "Title": feed.get("title", "No title"),
        "Description": feed.get("description", "No description"),
        "Link": feed.get("link", "No link"),
    }
