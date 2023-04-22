from fastapi import FastAPI, Form, Request
from starlette.templating import Jinja2Templates

from rss_feed_reader import feed_reader

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def root():
    return "Hello there"


@app.get("/read/{url:path}")
async def read_rss_feed(url: str):
    return feed_reader.read_just_the_stuff_we_want(url)


@app.get("/reader")
async def form_get(request: Request):
    result = "Enter an RSS Feed "
    return templates.TemplateResponse(  
        "form.html", context={"request": request, "result": result}
    )


@app.post("/reader")
async def form_post(request: Request, url: str = Form(...)):
    feed = feed_reader.read_just_the_stuff_we_want(url)
    return templates.TemplateResponse("form.html", context={"request": request, **feed})
