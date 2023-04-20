# RSS Feed Reader
RSS feed reader in terminal for Code Mentor.  RSS Feed Reader will take a url and return title, description, and link of the original content

# Installation
Install with pip

`python -m pip install git+https://github.com/mvictoria/rss_feed_reader`

# Usage
`rss_feed_reader [RSS URL LIST]`

example:

`rss_feed_reader https://talkpython.fm/episodes/rss https://realpython.com/podcasts/rpp/feed`

# Run with Docker
Build docker image

`sudo docker build --tag rss-feed-reader .`
`sudo docker container run --publish 80:80 --name rss-container rss-feed-reader`

Conect to [localhost](localhost/docs#/)

Shut it down with

```bash
sudo docker stop rss-container
sudo docker rm rss-container
```

# Links
[Code Mentor Project](https://www.codementor.io/projects/tool/rss-feed-reader-in-terminal-atx32jp82q)
