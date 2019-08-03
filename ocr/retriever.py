import praw

reddit = praw.Reddit('retriever', user_agent='retriever user agent')

def get_submissions(subreddit, amount):
    subreddit = reddit.subreddit(subreddit)
    return subreddit.hot(limit=amount)
    
def get_image_submissions(subreddit, amount):
    images = []
    submissions = get_submissions(subreddit, amount)

    for submission in submissions:
        if(str.endswith(submission.url, 'jpg')):
            images.append(submission)

    return images