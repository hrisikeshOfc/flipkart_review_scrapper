from scraper.logic.business_logic import Scraper
from scraper.exception.exception import FlipkartCustomException
from scraper.data_access.data_access import Database
from scraper.logging.logging import CustomLogger
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse
import pandas as pd
import uvicorn
import sys, os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="css")
templates = Jinja2Templates(directory='templates')
os.makedirs('logs', exist_ok=True)
logger = CustomLogger('endpoint_logs')
database = Database()


@app.get('/')
def index(request: Request):
    """
    API Desc: This api renders main index.html page.
    :return: Response of the page
    """
    logger.info("Index.html page requested")
    return templates.TemplateResponse(name="index.html", context={"request": request})


@app.post('/results')
def results(request: Request, content: str = Form(...)):
    """
    This api gets search result from index.html and query database if that collection not found,
    call scraper class to scrape data from flipkart
    :return: Render results.html
    """
    try:
        search_string = content.replace(" ", "%20")
        logger.info(f"Searching flipkart for {search_string}")
        reviews = database.get_collection(search_string)
        if not reviews.__len__() and search_string != "":
            scrap = Scraper(search_string)
            reviews = scrap.get_data()
            database.create_collection(search_string, reviews)
        return templates.TemplateResponse(name="results.html",
                                          context={"request": request,
                                                   'reviews': reviews[0][list(reviews[0].keys())[1]],
                                                   'list_of_products': list(reviews[0].keys())[1:],
                                                   'search_string': search_string})
    except Exception as e:
        message = FlipkartCustomException(e, sys)
        logger.error(message.error_message)
        return templates.TemplateResponse(name="505.html", context={"request": request})


@app.get('/get_download_csv')
def get_download_csv(request: Request,search_string: str):
    """
    This api asks user to select data to download in csv format
    :return: Renders download_data.html
    """
    try:
        # print(search_string)
        reviews = database.get_collection(search_string.replace(" ", "%20"))
        print(reviews)
        return templates.TemplateResponse(name="download_data.html",
                                          context={"request": request,
                                                   'list_of_products': list(reviews[0].keys())[1:],
                                                   'search_string': search_string})
    except Exception as e:
        message = FlipkartCustomException(e, sys)
        logger.error(message.error_message)
        return templates.TemplateResponse(name="505.html", context={"request": request})


@app.post('/post_download_csv')
def post_download_csv(request: Request, search_string: str = Form(...), product: str = Form(...)):
    """
    This Api downloads selected data into users local system.
    :return: Download data in csv format
    """
    try:
        reviews = database.get_collection(search_string.replace(" ", "%20"))
        print("rc", reviews)
        data = reviews[0][product.strip()]
        df = pd.DataFrame(data)
        df["Product_name"] = df["Product_name"].apply(lambda x: x.replace("%20"," "))
        df.to_csv("static/csv/data.csv", index=False)
        return FileResponse(path="static/csv/data.csv", filename="data.csv")
    except Exception as e:
        message = FlipkartCustomException(e, sys)
        logger.error(message.error_message)
        return templates.TemplateResponse(name="505.html", context={"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
