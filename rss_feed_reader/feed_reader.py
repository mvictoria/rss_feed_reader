import click
import feedparser


def read(url: str):
    feed = feedparser.parse(url)
    return feed.feed


def attribute(feed, attribute) -> str:
    return feed.get(attribute, f"no {attribute} element")


@click.command()
@click.argument("url")
def main(url):
    feed = read(url)

    click.echo(f"Title: {attribute(feed, 'title')}")
    click.echo(f"Description: {attribute(feed, 'description')}")
    click.echo(f"Link: {attribute(feed, 'link')}")


if __name__ == "__main__":
    main()
