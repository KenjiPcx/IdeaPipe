from ideagen.db.operations import batch_add_reddit_problems, batch_add_appsumo_solutions
from fastapi import FastAPI
from app.api import matching

def process_reddit_data():
    batch_add_reddit_problems('ideagen/scrape_pipelines/reddit/refined_reddit_posts.json')

def process_appsumo_data():
    batch_add_appsumo_solutions('ideagen/scrape_pipelines/appsumo/setup/appsumo-products.json')

if __name__ == "__main__":
    process_reddit_data()
    process_appsumo_data()

app = FastAPI()

app.include_router(matching.router, prefix="/api")
