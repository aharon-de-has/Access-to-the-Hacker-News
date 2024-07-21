Hacker News Data Collection and Analysis
Write a Python program that interacts with the Hacker News website and its API to perform various data collection and analysis operations. Use the documented API of the site (https://github.com/HackerNews/API) to download details and fields about various articles on the site, saving them in a CSV. The program will also perform analysis on the collected data and plot the results. Your code needs to be saved in a public GitHub repository and handed in via a link by 18/7 at 17:00.
Sub-Tasks:
Fetch and Save Top Stories:
Fetch the IDs of the top stories using the Hacker News API.
For each story ID, fetch the details (e.g., title, URL, score, author, time, and number of comments).
Save the story details in a structured CSV file.
Fetch Comments for Top Stories:
For each top story, fetch the IDs of the top-level comments.
For each comment ID, fetch the details (e.g., author, text, time, and parent story).
Save the comment details in a separate structured CSV file.
Analyze and Plot Data:
Analyze the collected data to generate summary statistics (e.g., average score of top stories, average number of comments per story).
Save these summary statistics in a CSV file.
Plot the analysis results using appropriate visualization libraries.
