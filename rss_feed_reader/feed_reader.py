import click
import feedparser


def read(url: str):
    feed = feedparser.parse(url)
    return feed.feed


def attribute(feed, attribute) -> str:
    return feed.get(attribute, f"no {attribute} element")


def read_just_the_stuff_we_want(url: str) -> dict:
    attribs = ("title", "description", "link")
    return {attrib: attribute(read(url), attrib) for attrib in attribs}


@click.command()
@click.argument("urls", nargs=-1)
def main(urls):

    for url in urls:
        
        feed = read_just_the_stuff_we_want(url)
        for attrib, value in feed.items():
            click.echo(f"{attrib}: {value}")
            
    


if __name__ == "__main__":
    main()
