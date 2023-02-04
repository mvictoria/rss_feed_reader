import feedparser
import click

def read(url: str):
    feed = feedparser.parse(url)
    return feed.feed


@click.command()
@click.argument('url')
def main(url):
    feed = read(url)

    click.echo(f"Title: {feed.title}")
    click.echo(f"Description: {feed.description}")
    click.echo(f"Link: {feed.link}")

if __name__ == "__main__":
    main()