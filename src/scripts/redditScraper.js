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
  apiKey: process.env.OPENAI_API_KEY || 'Your-API-Key-Here'
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
  try {
    const response = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        { role: "system", content: "You are a helpful assistant that analyzes Reddit posts. Respond in JSON format with 'problem' and 'question' fields." },
        { role: "user", content: `Analyze this Reddit post and identify any problems or questions the user might have. Respond in JSON format: ${post.title}\n${post.selftext}` }
      ],
    });

    const content = response.choices[0].message.content;
    
    console.log('Raw API response content:', content);

    try {
      // Attempt to parse the JSON
      const parsedContent = JSON.parse(content);
      return parsedContent;
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
      console.error('Problematic content:', content);
      
      // Attempt to extract problem and question using regex
      const problemMatch = content.match(/problem["\s:]+(.+?)[",$\n]/i);
      const questionMatch = content.match(/question["\s:]+(.+?)[",$\n]/i);
      
      return {
        problem: problemMatch ? problemMatch[1].trim() : 'Unable to parse problem',
        question: questionMatch ? questionMatch[1].trim() : 'Unable to parse question',
        rawContent: content
      };
    }
  } catch (error) {
    console.error('Error in API call:', error);
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
            const analysis = await analyzePost(post);
            if (analysis) {
              problems.push({
                subreddit,
                title: post.title,
                url: post.url,
                problem: analysis.problem,
                question: analysis.question,
                rawContent: analysis.rawContent
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
  fs.writeFile('scraped_problems.json', JSON.stringify(problems, null, 2), (err) => {
    if (err) throw err;
    console.log('Results saved to scraped_problems.json');
  });
}).catch(error => {
  console.error('Error in scraping process:', error);
});
