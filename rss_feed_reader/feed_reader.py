import feedparser


def read(url: str):
    feed = feedparser.parse(url)
    return feed.feed
