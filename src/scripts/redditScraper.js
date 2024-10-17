require('dotenv').config();
const snoowrap = require('snoowrap');
const fs = require('fs').promises;
const OpenAI = require('openai');

// Initialize Reddit client
const reddit = new snoowrap({
  userAgent: process.env.REDDIT_USER_AGENT,
  clientId: process.env.REDDIT_CLIENT_ID,
  clientSecret: process.env.REDDIT_CLIENT_SECRET,
  refreshToken: process.env.REDDIT_REFRESH_TOKEN
});

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY
});

// Load subreddits from groupsAndSubreddits.json
async function loadSubreddits() {
  const data = await fs.readFile('groupsAndSubreddits.json', 'utf8');
  return JSON.parse(data);
}

// Fetch posts from a subreddit
async function fetchPosts(subreddit, limit = 25) {
  return reddit.getSubreddit(subreddit).getNew({limit: limit});
}

// Analyze post using OpenAI
async function analyzePost(post) {
  const prompt = `Analyze the following Reddit post and classify it into one or more of these categories: Advice Requests, Solution Requests, Pain and Anger, Money Talks. Also, identify the root cause of the problem.

Post Title: ${post.title}
Post Content: ${post.selftext}

Provide the response in JSON format with the following structure:
{
  "categories": ["category1", "category2"],
  "rootCause": "brief description of the root cause",
  "tags": ["relevant", "tags"]
}`;

  const response = await openai.chat.completions.create({
    model: "gpt-3.5-turbo",
    messages: [{ role: "user", content: prompt }],
  });

  return JSON.parse(response.choices[0].message.content);
}

// Main function to orchestrate the scraping process
async function scrapeRedditProblems() {
  const subreddits = await loadSubreddits();
  const problems = [];

  for (const group of subreddits) {
    for (const subreddit of group.subreddits) {
      console.log(`Scraping r/${subreddit}...`);
      const posts = await fetchPosts(subreddit);
      
      for (const post of posts) {
        const analysis = await analyzePost(post);
        problems.push({
          problemName: post.title,
          subreddit: subreddit,
          postUrl: `https://reddit.com${post.permalink}`,
          score: post.score,
          createdAt: new Date(post.created_utc * 1000).toISOString(),
          categories: analysis.categories,
          rootCause: analysis.rootCause,
          tags: analysis.tags
        });
      }
    }
  }

  // Save problems to a JSON file
  await fs.writeFile('redditProblems.json', JSON.stringify(problems, null, 2));
  console.log('Scraping completed. Data saved to redditProblems.json');
}

scrapeRedditProblems().catch(console.error);