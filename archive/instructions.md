# Project Overview
An app that presents a gallery of startup ideas based on matching products and services to problems found in social media like reddit and x (twitter).

Stack: Next.js 14 App Router, Shadcn UI, Tailwind CSS, Supabase

# Core Features
1. AI chatbot that takes in a user problem they want to solve and usesRAG search to find the most relevant products and services that can solve the user's problem.
    - It will create not just suggest products, but also a plan and instructions on how these tools can be used in parallel to solve the user's problem.
2. Gallery of startup ideas based on matching products and services to problems found in social media like reddit and x (twitter). 
3. Users can click on a startup idea, in that page, it will show the idea category (The categories are fixed from groupsAndSubreddits.json), the tools that can be used to solve the problem, the total cost to use the tools, the team required to use the tools, and the steps to start the business. It will also show the posts from reddit that led to the idea, and users can click on those reddit posts to contact the original poster.

# Implementation Plan
1. Data pipeline to fetch posts from reddit based on groupsAndSubreddits.json
    - Focus on Ecommerce, Productivity, Notion Users and Influencers groups for now.
    - For each fetched post, use an AI agent to classify the labels for the post. Here is the list of labels:
        - Advice Requests (People asking for advice and resources)
        - Solution Requests (People asking for tools and solutions)
        - Pain and Anger (People expressing pain points and frustrations)
        - Money Talks (People talking about spending money)
    - Also extract the post title, post url, score and date created.
    - Based on the labels, additional pipelines are run:
        - Advice Requests:
            - Use an AI agent to write a response to the post.
            - Store the post, response and the labels in a database.
        - Solution Requests:
            - Use an AI agent to write a response to the post.
            - Store the post, response and the labels in a database.
        - Pain and Anger:
            - Use an AI agent to write a response to the post.
            - Store the post, response and the labels in a database.

# Documentation
How to fetch posts from reddit:

# File Structure