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
  const data = await fs.readFile('scrape_scripts/reddit/groupsAndSubreddits.json', 'utf8');
  return JSON.parse(data);
}

// Fetch posts from a subreddit
async function fetchPosts(subreddit, limit = 25) {
  return reddit.getSubreddit(subreddit).getNew({limit: limit});
}

// Analyze post using OpenAI
async function analyzePost(post, subreddit) {
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        { 
          role: "system", 
          content: "You are an assistant that analyzes Reddit posts to extract problem information. Respond with a JSON object only, no additional text or formatting." 
        },
        { 
          role: "user", 
          content: `Analyze this Reddit post from r/${subreddit}. Extract the following information:
            1. The main problem
            2. Root cause of the problem
            3. Main stakeholders affected
            4. Problem severity (on a scale of 1-5, where 1 is minor and 5 is critical)
            5. Relevant tags (choose from: money talks, solution request, advice request, pain and anger, or create new relevant tags)

            Respond with a JSON object only, no additional text or formatting.

            Post content:
            ${post.title}
            ${post.selftext}`
        }
      ],
    });

    const content = response.choices[0].message.content;
    
    // Remove any markdown formatting or extra text
    const jsonString = content.replace(/^```json\s*/, '').replace(/\s*```$/, '').trim();
    
    return JSON.parse(jsonString);
  } catch (error) {
    console.error('Error in API call:', error);
    console.error('API response content:', response.choices[0].message.content);
    return null;
  }
}

// Main function to orchestrate the scraping process
async function scrapeRedditProblems() {
  const problems = [];
  const groupsAndSubreddits = await loadSubreddits();
  
  for (const group of groupsAndSubreddits) {
    for (const subreddit of group.subreddits) {
      console.log(`Scraping r/${subreddit}...`);
      try {
        const posts = await fetchPosts(subreddit);
        for (const post of posts) {
          try {
            const analysis = await analyzePost(post, subreddit);
            if (analysis) {
              problems.push({
                subreddit: subreddit,
                problem_name: analysis.problem,
                root_cause: analysis.root_cause,
                stakeholders: analysis.stakeholders,
                severity: analysis.severity,
                tags: analysis.tags,
                post_url: post.url,
                score: post.score,
                comment_count: post.num_comments,
                created_date: new Date(post.created_utc * 1000).toISOString(),
              });
            } else {
              console.log(`Skipping post in r/${subreddit} due to null analysis`);
            }
          } catch (postError) {
            console.error(`Error analyzing post in r/${subreddit}:`, postError);
          }
        }
      } catch (subredditError) {
        console.error(`Error fetching posts from r/${subreddit}:`, subredditError);
      }
    }
  }
  return problems;
}

scrapeRedditProblems().then(problems => {
  console.log('Number of problems scraped:', problems.length);
  fs.writeFile('scraped_reddit.json', JSON.stringify(problems, null, 2), (err) => {
    if (err) throw err;
    console.log('Results saved to scraped_problems.json');
  });
}).catch(error => {
  console.error('Error in scraping process:', error);
});