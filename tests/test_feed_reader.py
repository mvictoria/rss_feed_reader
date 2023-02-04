import http.server
import threading
from pathlib import Path

import feedparser

from rss_feed_reader import feed_reader


class MockServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(Path("tests/test_valid_feed.xml").read_bytes())


def test_valid_feed():
    server = http.server.ThreadingHTTPServer(("127.0.0.127", 9999), MockServer)

    with server:
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        test_feed = feed_reader.read("http://127.0.0.127:9999/")
        server.shutdown()
    assert test_feed.title == "title test"
    assert test_feed.description == "description test"
    assert test_feed.link == "https://www.urltest.com"


def test_attribute_when_it_exists():
    test_rss = feedparser.FeedParserDict(
        {"link": "mylink", "description": "mydesc", "title": "mytitle"}
    )
    assert feed_reader.attribute(test_rss, "description") == "mydesc"


def test_attribute_when_it_doesnt_exists():
    test_rss = feedparser.FeedParserDict(
        {"link": "mylink", "description": "mydesc", "title": "mytitle"}
    )
    assert feed_reader.attribute(test_rss, "doesnt_exist") == "no doesnt_exist element"
