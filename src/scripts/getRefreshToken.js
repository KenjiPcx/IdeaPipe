require('dotenv').config();
const snoowrap = require('snoowrap');
const readlineSync = require('readline-sync');

// Debug logs for all environment variables
console.log('REDDIT_CLIENT_ID:', process.env.REDDIT_CLIENT_ID);
console.log('REDDIT_CLIENT_SECRET:', process.env.REDDIT_CLIENT_SECRET ? '[REDACTED]' : 'undefined');
console.log('REDDIT_USER_AGENT:', process.env.REDDIT_USER_AGENT);

// Check if required environment variables are set
if (!process.env.REDDIT_CLIENT_ID || !process.env.REDDIT_CLIENT_SECRET || !process.env.REDDIT_USER_AGENT) {
  console.error('Error: Missing required environment variables. Please check your .env file.');
  process.exit(1);
}

const authUrl = snoowrap.getAuthUrl({
  clientId: process.env.REDDIT_CLIENT_ID,
  scope: ['identity', 'read', 'submit'],
  redirectUri: 'http://localhost:8080/callback',
  permanent: true,
  state: 'fe211bebc52eb3da9bef8db6e63104d3'
});

console.log('Auth URL:', authUrl);

console.log('Please visit this URL to authorize the application:', authUrl);
console.log('After authorizing, you\'ll be redirected to a localhost URL. Copy the "code" parameter from the URL and paste it here:');

const authorizationCode = readlineSync.question('Enter the code: ');

snoowrap.fromAuthCode({
  code: authorizationCode,
  userAgent: process.env.REDDIT_USER_AGENT,
  clientId: process.env.REDDIT_CLIENT_ID,
  clientSecret: process.env.REDDIT_CLIENT_SECRET,
  redirectUri: 'http://localhost:8080/callback'
}).then(r => {
  console.log('Your refresh token is:', r.refreshToken);
  console.log('Please add this to your .env file as REDDIT_REFRESH_TOKEN');
}).catch(error => {
  console.error('Error:', error);
});
