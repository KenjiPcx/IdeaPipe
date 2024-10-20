#!/bin/bash

# Set OpenAI API Key
export OPENAI_API_KEY="your_openai_api_key_here"

# Set any other environment variables your script might need
# For example:
export REDDIT_CLIENT_ID=wGL7v2wpRk2J-K-AH7Z-cA
export REDDIT_CLIENT_SECRET=Og0hOdrcz8se85mnDRTs4L6HiJA2vQ
export REDDIT_USER_AGENT=ideagen

# Print a message to confirm the variables are set
echo "Environment variables for Reddit scraper have been set."

# Optionally, run the Python script
# Uncomment the following line if you want to run the script automatically
# python3 scrape_scripts/reddit/reddit_scraper_pipeline.py
