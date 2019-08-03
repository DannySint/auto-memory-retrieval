import praw

reddit = praw.Reddit('retriever', user_agent='retriever user agent')

def get_submissions(subreddit, amount):
    subreddit = reddit.subreddit(subreddit)
    return subreddit.hot(limit=amount)
    
def get_image_submissions(subreddit, amount):
    images = []
    submissions = get_submissions(subreddit, amount)
    
    #if submission has a date/time that matches the url in the db then take from db
    for submission in submissions:
        if(str.endswith(submission.url, 'jpg')):
            images.append(submission)

    return images