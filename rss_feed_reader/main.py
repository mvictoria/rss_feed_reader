import feedparser
from fastapi import FastAPI, Form, Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return "Hello there"


@app.get("/read/{url:path}")
def read_rss_feed(url: str):
    feed = feedparser.parse(url).feed

    return {
        "Title": feed.get("title", "No title"),
        "Description": feed.get("description", "No description"),
        "Link": feed.get("link", "No link"),
    }


@app.get("/reader")
def form_get(request: Request):
    result = "Enter an RSS Feed "
    return templates.TemplateResponse(
        "form.html", context={"request": request, "result": result}
    )


@app.post("/reader")
def form_post(request: Request, num: str = Form(...)):
    feed = feedparser.parse(num).feed

    return templates.TemplateResponse(
        "form.html",
        context={
            "request": request,
            "title": feed.get("title", "No title"),
            "link": feed.get("link", "No link"),
            "description": feed.get("description", "No description"),
        },
    )
