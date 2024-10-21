import json
from .client import supabase
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def batch_add_reddit_problems(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            posts = json.load(file)
        
        formatted_posts = []
        for post in posts:
            formatted = {
                'source': 'reddit',
                'created_at': datetime.now().isoformat(),
                'id': post.get('id'),
                'title': post.get('title'),
                'content': post.get('selftext'),
                'author': post.get('author'),
                'score': post.get('score'),
                'num_comments': post.get('num_comments'),
                'subreddit': post.get('subreddit'),
                'url': f"https://www.reddit.com{post.get('permalink')}"
            }
            formatted_posts.append({k: v for k, v in formatted.items() if v is not None})
        
        result = supabase.table('problems').insert(formatted_posts).execute()
        logger.info(f"Successfully added {len(formatted_posts)} Reddit posts")
        return result
    except Exception as e:
        logger.error(f"Error adding Reddit posts: {str(e)}")
        raise

def batch_add_appsumo_solutions(json_file_path):
    try:
        with open(json_file_path, 'r') as file:
            products = json.load(file)
        
        formatted_products = []
        for product in products:
            formatted = {
                'source': 'appsumo',
                'created_at': datetime.now().isoformat(),
                'name': product.get('name'),
                'category': product.get('category'),
                'short_description': product.get('short_description'),
                'rating': product.get('rating'),
                'no_of_ratings': product.get('no_of_ratings'),
                'price': product.get('price'),
                'url': product.get('url')
            }
            formatted_products.append({k: v for k, v in formatted.items() if v is not None})
        
        result = supabase.table('solutions').insert(formatted_products).execute()
        logger.info(f"Successfully added {len(formatted_products)} AppSumo products")
        return result
    except Exception as e:
        logger.error(f"Error adding AppSumo products: {str(e)}")
        raise
