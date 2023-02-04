import click
import feedparser


def read(url: str):
    feed = feedparser.parse(url)
    return feed.feed


def title(feed) -> str:
    return feed.get("title", "no title element")


def description(feed) -> str:
    return feed.get("description", "no description element")


def link(feed) -> str:
    return feed.get("link", "no link element")


@click.command()
@click.argument("url")
def main(url):
    feed = read(url)

    click.echo(f"Title: {title(feed)}")
    click.echo(f"Description: {description(feed)}")
    click.echo(f"Link: {link(feed)}")


if __name__ == "__main__":
    main()
