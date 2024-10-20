import asyncio
import json
import os
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
import asyncpraw
from tqdm import tqdm
import ssl
import certifi
import aiohttp
import logging
import traceback
from dotenv import load_dotenv
import asyncprawcore
from dataclasses import dataclass, asdict

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['SSL_CERT_DIR'] = os.path.dirname(certifi.where())

# Pydantic model for refined Reddit post info
@dataclass
class RefinedRedditPost:
    id: str
    title: str
    content: str
    author: str
    score: int
    num_comments: int
    created_utc: float
    subreddit: str
    refined_content: str
    main_topics: List[str]
    sentiment: str
    key_insights: List[str]
    potential_impact: str
    tags: List[str]
    entities: List[str]
    keywords: List[str]

    def dict(self):
        return asdict(self)

async def scrape_subreddit(reddit: asyncpraw.Reddit, subreddit: str, limit: int = 10) -> List[str]:
    subreddit_name = subreddit.replace('r/', '')
    try:
        subreddit = await reddit.subreddit(subreddit_name)
        post_ids = [post.id async for post in subreddit.new(limit=limit)]
        logger.info(f"Fetched {len(post_ids)} post IDs from r/{subreddit_name}")
        return post_ids
    except Exception as e:
        logger.error(f"Error scraping subreddit r/{subreddit_name}: {str(e)}")
        return []

async def process_post(reddit: asyncpraw.Reddit, post_id: str) -> RefinedRedditPost:
    try:
        logger.info(f"Processing post {post_id}")
        submission = await reddit.submission(id=post_id)
        await submission.load()

        prompt = f"""
        Analyze the following Reddit post and provide the requested information in the exact format specified below:

        Title: {submission.title}
        Content: {submission.selftext}
        Subreddit: {submission.subreddit.display_name}

        Please respond using only the following format, filling in the information for each field:

        Refined Content: [Provide a 2-3 sentence summary of the post]
        Main Topics: [List 3-5 main topics, separated by commas]
        Sentiment: [State either 'positive', 'negative', or 'neutral']
        Key Insights: [List 3-5 key insights, separated by commas]
        Potential Impact: [Briefly describe the potential impact in 1-2 sentences]
        Tags: [List 3-5 relevant tags, separated by commas]
        Entities: [List any named entities mentioned, separated by commas]
        Keywords: [List 5-7 keywords, separated by commas]

        Do not include any additional text or explanations outside of these fields.
        """

        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes Reddit posts."},
                {"role": "user", "content": prompt}
            ]
        )
        
        ai_response = response.choices[0].message.content
        logger.info(f"OpenAI response for post {post_id}:\n{ai_response}")
        
        parsed_response = parse_ai_response(ai_response)
        
        refined_post = RefinedRedditPost(
            id=submission.id,
            title=submission.title,
            content=submission.selftext,
            author=submission.author.name if submission.author else '[deleted]',
            score=submission.score,
            num_comments=submission.num_comments,
            created_utc=submission.created_utc,
            subreddit=submission.subreddit.display_name,
            refined_content=parsed_response.get('refined_content', ''),
            main_topics=parsed_response.get('main_topics', []),
            sentiment=parsed_response.get('sentiment', ''),
            key_insights=parsed_response.get('key_insights', []),
            potential_impact=parsed_response.get('potential_impact', ''),
            tags=parsed_response.get('tags', []),
            entities=parsed_response.get('entities', []),
            keywords=parsed_response.get('keywords', [])
        )

        return refined_post

    except Exception as e:
        logger.error(f"Error processing post {post_id}: {str(e)}")
        logger.error(traceback.format_exc())
        return None

def parse_ai_response(response: str) -> dict:
    lines = response.split('\n')
    parsed = {}
    current_key = None
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            current_key = key.strip().lower().replace(' ', '_')
            parsed[current_key] = value.strip()
        elif current_key and line.strip():
            parsed[current_key] += ', ' + line.strip()
    
    # Convert comma-separated strings to lists where appropriate
    list_fields = ['main_topics', 'key_insights', 'tags', 'entities', 'keywords']
    for field in list_fields:
        if field in parsed:
            parsed[field] = [item.strip() for item in parsed[field].split(',')]
    
    return parsed

class CustomRequestor(asyncprawcore.Requestor):
    def __init__(self, user_agent, *args, **kwargs):
        super().__init__(user_agent, *args, **kwargs)
        self.session = None
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def __aenter__(self):
        connector = aiohttp.TCPConnector(ssl=self.ssl_context)
        self.session = aiohttp.ClientSession(connector=connector)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def close(self):
        if self.session:
            await self.session.close()

    async def request(self, *args, **kwargs):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return await super().request(*args, **kwargs)

async def main(subreddits: List[str], posts_per_subreddit: int = 10):
    print(f"SSL cert file: {ssl.get_default_verify_paths().cafile}")
    print(f"Certifi cert file: {certifi.where()}")

    user_agent = os.getenv("REDDIT_USER_AGENT")
    requestor = CustomRequestor(user_agent)
    
    try:
        async with requestor:
            reddit = asyncpraw.Reddit(
                requestor=requestor,
                client_id=os.getenv("REDDIT_CLIENT_ID"),
                client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                user_agent=user_agent
            )
            
            try:
                all_post_ids = []
                for subreddit in subreddits:
                    logger.info(f"Fetching posts from r/{subreddit}")
                    try:
                        subreddit_post_ids = await scrape_subreddit(reddit, subreddit, posts_per_subreddit)
                        all_post_ids.extend(subreddit_post_ids)
                        logger.info(f"Fetched {len(subreddit_post_ids)} posts from r/{subreddit}")
                    except Exception as e:
                        logger.error(f"Error fetching posts from r/{subreddit}: {str(e)}")

                logger.info(f"Total post IDs fetched: {len(all_post_ids)}")

                results = []
                failed_posts = []
                for post_id in tqdm(all_post_ids, desc="Processing posts"):
                    try:
                        result = await process_post(reddit, post_id)
                        if result:
                            results.append(result)
                            logger.info(f"Successfully processed post {post_id}")
                        else:
                            failed_posts.append(post_id)
                            logger.warning(f"Failed to process post {post_id}")
                    except Exception as e:
                        logger.error(f"Error processing post {post_id}: {str(e)}")
                        failed_posts.append(post_id)

                logger.info(f"Total successfully processed posts: {len(results)}")
                logger.info(f"Total failed posts: {len(failed_posts)}")
                return results, failed_posts
            finally:
                await reddit.close()
    finally:
        await requestor.close()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_subreddits(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    target_groups = ["Ecommerce", "Marketers"]
    subreddits = []
    
    for group in data:
        if group["groupName"] in target_groups:
            subreddits.extend(group["subreddits"])
    
    return subreddits

if __name__ == "__main__":
    file_path = "scrape_scripts/reddit/groupsAndSubreddits.json"
    subreddits = load_subreddits(file_path)
    logger.info(f"Loaded {len(subreddits)} subreddits")
    
    async def run_main():
        try:
            results, failed_posts = await main(subreddits)
            logger.info(f"Final number of results: {len(results)}")
            logger.info(f"Number of failed posts: {len(failed_posts)}")
            
            if results:
                with open('refined_reddit_posts.json', 'w') as f:
                    json.dump([post.dict() for post in results], f, indent=2)
                logger.info(f"Scraping completed. {len(results)} posts saved to refined_reddit_posts.json")
            else:
                logger.warning("No successful results to save. The refined_reddit_posts.json file will be empty.")
            
            if failed_posts:
                with open('failed_posts.json', 'w') as f:
                    json.dump(failed_posts, f, indent=2)
                logger.warning(f"{len(failed_posts)} failed posts saved to failed_posts.json")
            
        except Exception as e:
            logger.error(f"Error in main execution: {str(e)}")
            logger.error(traceback.format_exc())

    asyncio.run(run_main())
